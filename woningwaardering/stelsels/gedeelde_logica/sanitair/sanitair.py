import warnings
from collections import Counter
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels.builders import (
    WaarderingBuilder,
    WaarderingsgroepBuilder,
)
from woningwaardering.stelsels.criterium import maximering_naam
from woningwaardering.stelsels.utils import (
    gedeeld_met_adressen,
    gedeeld_met_onzelfstandige_woonruimten,
    rond_af,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    Referentiedata,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Installatiesoort,
    InstallatiesoortReferentiedata,
    Meeteenheid,
    Ruimtedetailsoort,
    RuimtedetailsoortReferentiedata,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
    WoningwaarderingstelselReferentiedata,
)
from woningwaardering.vera.utils import get_bouwkundige_elementen

# Op maximaal één niet-badkamer-ruimte die zelf met >= 8 onzelfstandige
# woonruimten is gedeeld, wordt geen wastafel-maximering toegepast. Dat is de
# kandidaat waar de maximering de meeste punten zou afsnijden.
_PUNTEN_WASTAFEL = Decimal("1")
_PUNTEN_MEERPERSOONSWASTAFEL = Decimal("1.5")

_BADKAMERACHTIGE_RUIMTES: tuple[RuimtedetailsoortReferentiedata, ...] = (
    Ruimtedetailsoort.badkamer,
    Ruimtedetailsoort.badkamer_met_toilet,
    Ruimtedetailsoort.doucheruimte,
)
_BAD_OF_DOUCHE_INSTALLATIES: tuple[InstallatiesoortReferentiedata, ...] = (
    Installatiesoort.bad,
    Installatiesoort.douche,
    Installatiesoort.drempelloze_inrijdouche,
    Installatiesoort.bad_en_douche,
)
# 2.6.1 Punten voor sanitaire basisvoorzieningen — Toilet
_TOILET_PUNTEN_TOILETRUIMTE: dict[InstallatiesoortReferentiedata, float] = {
    Installatiesoort.hangend_toilet: 3.75,
    Installatiesoort.staand_toilet: 3.0,
}
_TOILET_PUNTEN_BADKAMER: dict[InstallatiesoortReferentiedata, float] = {
    Installatiesoort.hangend_toilet: 2.75,
    Installatiesoort.staand_toilet: 2.0,
}
# 2.6.1 Punten voor sanitaire basisvoorzieningen — Wastafel
_WASTAFEL_PUNTEN: dict[InstallatiesoortReferentiedata, float] = {
    Installatiesoort.wastafel: 1.0,
    Installatiesoort.meerpersoonswastafel: 1.5,
}
# 2.6.1 Punten voor sanitaire basisvoorzieningen — Bad en douche
_BAD_EN_DOUCHE_PUNTEN_ZELFSTANDIG: dict[InstallatiesoortReferentiedata, float] = {
    Installatiesoort.douche: 4.0,
    # VERA-drempelloze inrijdouche telt als Douche.
    Installatiesoort.drempelloze_inrijdouche: 4.0,
    Installatiesoort.bad: 6.0,
    Installatiesoort.bad_en_douche: 7.0,
}
_BAD_EN_DOUCHE_PUNTEN_ONZELFSTANDIG: dict[InstallatiesoortReferentiedata, float] = {
    Installatiesoort.douche: 3.0,
    # VERA-drempelloze inrijdouche telt als Douche.
    Installatiesoort.drempelloze_inrijdouche: 3.0,
    Installatiesoort.bad: 5.0,
    Installatiesoort.bad_en_douche: 6.0,
}
# 2.6.2 Punten voor extra sanitaire voorzieningen
_EXTRA_VOORZIENINGEN_PUNTEN: dict[InstallatiesoortReferentiedata, float] = {
    Installatiesoort.bubbelfunctie_van_het_bad: 1.5,
    Installatiesoort.douchewand: 1.25,
    Installatiesoort.handdoekenradiator: 0.75,
    Installatiesoort.ingebouwd_kastje_met_in_of_opgebouwde_wastafel: 1,
    Installatiesoort.kastruimte: 0.75,
    Installatiesoort.stopcontact_bij_wastafel: 0.25,
    Installatiesoort.eenhandsmengkraan: 0.25,
    Installatiesoort.thermostatische_mengkraan: 0.5,
}


def _ruimte_gedeeld(ruimte: EenhedenRuimte) -> bool:
    return gedeeld_met_adressen(ruimte) or gedeeld_met_onzelfstandige_woonruimten(
        ruimte
    )


def _is_badkamerachtige_ruimte(ruimte: EenhedenRuimte) -> bool:
    return ruimte.detail_soort in _BADKAMERACHTIGE_RUIMTES


def _vrijstellingskandidaat(ruimte: EenhedenRuimte) -> bool:
    # Wij interpreteren de 8+-uitzondering op ruimteniveau: alleen niet-badkamer-
    # ruimten met gedeeld_met_aantal_onzelfstandige_woonruimten >= 8 kunnen
    # de uitzonderingsruimte zijn waar de wastafel-maximering niet geldt.
    return (
        not _is_badkamerachtige_ruimte(ruimte)
        and (ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 0) >= 8
    )


def _toilet_punten(
    ruimte: EenhedenRuimte,
) -> dict[InstallatiesoortReferentiedata, float] | None:
    if ruimte.detail_soort == Ruimtedetailsoort.toiletruimte:
        return _TOILET_PUNTEN_TOILETRUIMTE

    if _is_badkamerachtige_ruimte(ruimte):
        return _TOILET_PUNTEN_BADKAMER

    return None


def _bad_en_douche_punten(
    stelsel: WoningwaarderingstelselReferentiedata,
) -> dict[InstallatiesoortReferentiedata, float]:
    if stelsel == Woningwaarderingstelsel.zelfstandige_woonruimten:
        return _BAD_EN_DOUCHE_PUNTEN_ZELFSTANDIG
    return _BAD_EN_DOUCHE_PUNTEN_ONZELFSTANDIG


def _aantal_douches(installaties: Counter[Referentiedata]) -> int:
    return sum(
        installaties[installatiesoort]
        for installatiesoort in (
            Installatiesoort.douche,
            Installatiesoort.drempelloze_inrijdouche,
        )
    )


def _heeft_bad_of_douche(installaties: Counter[Referentiedata]) -> bool:
    return any(
        installaties[installatiesoort]
        for installatiesoort in _BAD_OF_DOUCHE_INSTALLATIES
    )


def waardeer_sanitair(
    ruimte: EenhedenRuimte,
    stelsel: WoningwaarderingstelselReferentiedata,
    *,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
    deler: int = 1,
) -> list[WaarderingBuilder]:
    if ruimte.detail_soort is None:
        warnings.warn(f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen detailsoort.")
        return []

    _bouwkundige_elementen_naar_installaties(ruimte)

    ruimte_criterium = waarderingsgroep_builder.met_subgroep(
        id=ruimte.id,
        naam=ruimte.naam
        or ruimte.id
        or (ruimte.detail_soort.naam if ruimte.detail_soort else ""),
    )

    detail_waarderingen: list[WaarderingBuilder] = [
        *list(_waardeer_toiletten(ruimte, ruimte_criterium)),
        *list(_waardeer_wastafels(ruimte, ruimte_criterium)),
    ]

    baden_en_douches_waarderingen = list(
        _waardeer_baden_en_douches(ruimte, stelsel, ruimte_criterium)
    )
    totaal_punten_bad_en_douche = Decimal(
        sum(
            Decimal(str(woningwaardering.punten))
            for woningwaardering in baden_en_douches_waarderingen
            if woningwaardering.punten is not None
        )
    )
    detail_waarderingen.extend(baden_en_douches_waarderingen)

    voorziening_waarderingen = list(
        _waardeer_installaties(
            ruimte,
            ruimte_criterium,
            totaal_punten_bad_en_douche=totaal_punten_bad_en_douche,
        )
    )
    detail_waarderingen.extend(voorziening_waarderingen)

    if not detail_waarderingen:
        return []

    # De punten van een gedeelde ruimte worden gedeeld door het aantal woonruimten
    # waarmee de ruimte gedeeld wordt.
    if deler > 1:
        for woningwaardering in detail_waarderingen:
            if woningwaardering.punten is not None:
                woningwaardering.punten = float(
                    rond_af(
                        Decimal(str(woningwaardering.punten)) / Decimal(deler),
                        decimalen=2,
                    )
                )

    return [ruimte_criterium, *detail_waarderingen]


def _bouwkundige_elementen_naar_installaties(ruimte: EenhedenRuimte) -> None:
    ruimte.installaties = ruimte.installaties or []
    # Backwards compatibiliteit voor bouwkundige elementen
    for bouwkundigelementdetailsoort, installatiesoort in {
        Bouwkundigelementdetailsoort.wastafel: Installatiesoort.wastafel,
        Bouwkundigelementdetailsoort.douche: Installatiesoort.douche,
        Bouwkundigelementdetailsoort.bad: Installatiesoort.bad,
        Bouwkundigelementdetailsoort.kast: Installatiesoort.kastruimte,
        Bouwkundigelementdetailsoort.closetcombinatie: Installatiesoort.staand_toilet,
        Bouwkundigelementdetailsoort.fontein: Installatiesoort.wastafel,
    }.items():
        bouwkundige_elementen = list(
            get_bouwkundige_elementen(ruimte, bouwkundigelementdetailsoort)
        )
        if bouwkundige_elementen:
            warnings.warn(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft een {bouwkundigelementdetailsoort.naam} als bouwkundig element. Dit dient als `Installatiesoort` '{installatiesoort}' op de ruimte onder `installaties` gespecificeerd te worden."
            )
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}): {bouwkundigelementdetailsoort.naam} wordt als {installatiesoort.naam} toegevoegd aan installaties"
            )
            ruimte.installaties.extend(
                [installatiesoort for _ in bouwkundige_elementen]
            )


def _waardeer_toiletten(
    ruimte: EenhedenRuimte,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
) -> Iterator[WaarderingBuilder]:
    installaties = Counter([installatie for installatie in ruimte.installaties or []])
    toilet_punten = _toilet_punten(ruimte)
    # Toiletten buiten toiletruimten en badkamers komen niet in aanmerking voor
    # waardering. Doucheruimte telt hierbij mee als badkamer.
    if toilet_punten is not None:
        for toiletsoort in [
            Installatiesoort.hangend_toilet,
            Installatiesoort.staand_toilet,
        ]:
            aantal_toiletten = installaties[toiletsoort]

            if aantal_toiletten > 0:
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}): {aantal_toiletten}x een {toiletsoort.naam} voor {Woningwaarderingstelselgroep.sanitair.naam}."
                )
                yield waarderingsgroep_builder.met_onderliggend(
                    id=toiletsoort.name,
                    naam=toiletsoort.naam,
                    meeteenheid=Meeteenheid.stuks,
                    punten=rond_af(
                        Decimal(str(toilet_punten[toiletsoort]))
                        * Decimal(str(aantal_toiletten)),
                        decimalen=2,
                    ),
                    aantal=aantal_toiletten,
                )


def _waardeer_wastafels(
    ruimte: EenhedenRuimte,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
) -> Iterator[WaarderingBuilder]:
    installaties = Counter([installatie for installatie in ruimte.installaties or []])

    totaal_aantal_wastafels = 0

    for wastafelsoort in [
        Installatiesoort.wastafel,
        Installatiesoort.meerpersoonswastafel,
    ]:
        aantal_wastafels = installaties[wastafelsoort]

        # Een aanrecht met spoelbak, waarvan de lengte minder bedraagt dan 1 m,
        # voldoet dus niet aan de eis van 1 m en wordt daarom niet als aanrecht gewaardeerd,
        # maar als wastafel.
        aantal_spoelbakken = 0
        if wastafelsoort == Installatiesoort.wastafel and ruimte.detail_soort in (
            Ruimtedetailsoort.keuken,
            Ruimtedetailsoort.woonkamer_en_of_keuken,
            Ruimtedetailsoort.woonkamer,
            Ruimtedetailsoort.woon_en_of_slaapkamer,
            Ruimtedetailsoort.slaapkamer,
        ):
            for element in ruimte.bouwkundige_elementen or []:
                if element.detail_soort == Bouwkundigelementdetailsoort.aanrecht:
                    if element.lengte is not None and element.lengte < 1000:
                        logger.info(
                            f"Ruimte '{ruimte.naam}' ({ruimte.id}): aanrecht < 1m telt als wastafel mee voor {Woningwaarderingstelselgroep.sanitair.naam}."
                        )
                        yield waarderingsgroep_builder.met_onderliggend(
                            id=wastafelsoort.name,
                            naam=f"{wastafelsoort.naam} (spoelbak in aanrecht < 1m)",
                            meeteenheid=Meeteenheid.stuks,
                            punten=_WASTAFEL_PUNTEN[wastafelsoort],
                            aantal=1,
                        )
                        aantal_spoelbakken += 1

        totaal_aantal_wastafels += aantal_wastafels

        punten_per_wastafel = Decimal(str(_WASTAFEL_PUNTEN[wastafelsoort]))

        punten_voor_wastafels = rond_af(
            Decimal(str(aantal_wastafels + aantal_spoelbakken)) * punten_per_wastafel,
            decimalen=2,
        )

        if aantal_wastafels > 0:
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}): {aantal_wastafels}x een {wastafelsoort.naam} voor {Woningwaarderingstelselgroep.sanitair.naam}."
            )
            yield waarderingsgroep_builder.met_onderliggend(
                id=wastafelsoort.name,
                naam=wastafelsoort.naam,
                meeteenheid=Meeteenheid.stuks,
                punten=rond_af(
                    aantal_wastafels * punten_per_wastafel,
                    decimalen=2,
                ),
                aantal=aantal_wastafels,
            )

        # Wastafels worden gewaardeerd tot een maximum van 1 punt,
        # meerpersoonswastafels tot een maximum van 1,5 punt,
        # per vertrek of overige ruimte, m.u.v. de badkamer.
        # Voor vrijstellingskandidaten stellen we maximering uit tot
        # maximeer_wastafels (één uitzonderingsruimte mag dan ongemaximeerd
        # blijven voor wastafels én meerpersoonswastafels).
        if (
            punten_voor_wastafels > punten_per_wastafel
            and not _is_badkamerachtige_ruimte(ruimte)
            and not _vrijstellingskandidaat(ruimte)
        ):
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}): {punten_voor_wastafels} punten voor {wastafelsoort.naam} in {ruimte.detail_soort.naam if ruimte.detail_soort else ruimte.naam}. Correctie wordt toegepast ivm maximaal {punten_per_wastafel} punt."
            )
            yield waarderingsgroep_builder.met_onderliggend(
                id=f"max_punten_{wastafelsoort.name}",
                naam=maximering_naam(
                    gedeeld=_ruimte_gedeeld(ruimte),
                    met_puntental=(
                        f"Max {punten_per_wastafel} punt voor {wastafelsoort.naam}"
                    ),
                    gedeelde_naam=f"Maximering voor {wastafelsoort.naam}",
                ),
                punten=rond_af(
                    punten_per_wastafel - punten_voor_wastafels,
                    decimalen=2,
                ),
            )
    # Waarschuw indien er minder wastafels zijn dan ingebouwde kasten met wastafel
    # want een wastafel moet apart worden meegegeven
    aantal_ingebouwde_kasten = installaties[
        Installatiesoort.ingebouwd_kastje_met_in_of_opgebouwde_wastafel
    ]
    if totaal_aantal_wastafels < aantal_ingebouwde_kasten:
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}): {totaal_aantal_wastafels} wastafel(s) zijn minder dan het aantal ingebouwde kasten met wastafel ({aantal_ingebouwde_kasten})."
            f" Een wastafel in een {Installatiesoort.ingebouwd_kastje_met_in_of_opgebouwde_wastafel.naam} moet apart worden meegegeven."
        )


def _waardeer_baden_en_douches(
    ruimte: EenhedenRuimte,
    stelsel: WoningwaarderingstelselReferentiedata,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
) -> Iterator[WaarderingBuilder]:
    installaties = Counter([installatie for installatie in ruimte.installaties or []])
    punten_bad_en_douche = _bad_en_douche_punten(stelsel)
    aantal_douches = _aantal_douches(installaties)
    aantal_baden = installaties[Installatiesoort.bad]

    # Gekoppelde bad+douche: losse BAD met DOU/DRD op dezelfde ruimte
    aantal_bad_en_douches_gekoppeld = min(aantal_douches, aantal_baden)
    # Expliciete referentie BDO (bad en douche als één installatie)
    aantal_bad_en_douche_expliciet = installaties[Installatiesoort.bad_en_douche]
    aantal_bad_en_douches = (
        aantal_bad_en_douches_gekoppeld + aantal_bad_en_douche_expliciet
    )

    if aantal_bad_en_douches > 0:
        punten = rond_af(
            Decimal(str(aantal_bad_en_douches))
            * Decimal(str(punten_bad_en_douche[Installatiesoort.bad_en_douche])),
            decimalen=2,
        )
        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}): {aantal_bad_en_douches}x een {Installatiesoort.bad_en_douche.naam} voor {Woningwaarderingstelselgroep.sanitair.naam}"
        )
        yield waarderingsgroep_builder.met_onderliggend(
            id=Installatiesoort.bad_en_douche.name,
            naam=Installatiesoort.bad_en_douche.naam,
            meeteenheid=Meeteenheid.stuks,
            punten=punten,
            aantal=aantal_bad_en_douches,
        )

    for installatiesoort in [
        Installatiesoort.bad,
        Installatiesoort.douche,
        Installatiesoort.drempelloze_inrijdouche,
    ]:
        aantal = installaties[installatiesoort] - aantal_bad_en_douches
        if aantal > 0:
            punten = rond_af(
                Decimal(str(aantal))
                * Decimal(str(punten_bad_en_douche[installatiesoort])),
                2,
            )
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}): {aantal}x een {installatiesoort.naam} voor {Woningwaarderingstelselgroep.sanitair.naam}"
            )
            yield waarderingsgroep_builder.met_onderliggend(
                id=installatiesoort.name,
                naam=installatiesoort.naam,
                meeteenheid=Meeteenheid.stuks,
                punten=punten,
                aantal=aantal,
            )


def _waardeer_installaties(
    ruimte: EenhedenRuimte,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
    *,
    totaal_punten_bad_en_douche: Decimal,
) -> Iterator[WaarderingBuilder]:
    installaties = Counter([installatie for installatie in ruimte.installaties or []])

    totaal_punten_voorzieningen = Decimal("0")

    totaal_aantal_wastafels = (
        installaties[Installatiesoort.wastafel]
        + installaties[Installatiesoort.meerpersoonswastafel]
    )

    bad_en_of_douche_aanwezig = _heeft_bad_of_douche(installaties)

    if _is_badkamerachtige_ruimte(ruimte):
        detail_soort = ruimte.detail_soort
        if detail_soort is None:
            return
        heeft_extra_voorzieningen = any(
            installatie in _EXTRA_VOORZIENINGEN_PUNTEN for installatie in installaties
        )

        if heeft_extra_voorzieningen:
            # Geen waardering voor extra voorzieningen indien er geen wastafel in de ruimte is
            if totaal_aantal_wastafels == 0:
                warnings.warn(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}): geen wastafel aanwezig in {detail_soort.naam}, extra voorzieningen worden niet gewaardeerd."
                )
            # Geen waardering voor extra voorzieningen indien er geen douche of bad in de ruimte is
            elif not bad_en_of_douche_aanwezig:
                warnings.warn(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}): geen bad of douche aanwezig in {detail_soort.naam}, extra voorzieningen worden niet gewaardeerd."
                )
            elif totaal_aantal_wastafels > 0 and bad_en_of_douche_aanwezig:
                voorzieningen_criterium: WaarderingBuilder | None = None

                for installatiesoort in _EXTRA_VOORZIENINGEN_PUNTEN:
                    aantal = installaties[installatiesoort]
                    if aantal == 0:
                        continue

                    if voorzieningen_criterium is None:
                        voorzieningen_criterium = (
                            waarderingsgroep_builder.met_onderliggend(
                                id="extra_voorzieningen",
                                naam="Extra voorzieningen",
                            )
                        )
                        yield voorzieningen_criterium

                    punten = rond_af(
                        Decimal(str(aantal))
                        * Decimal(str(_EXTRA_VOORZIENINGEN_PUNTEN[installatiesoort])),
                        decimalen=2,
                    )

                    totaal_punten_voorzieningen += punten

                    logger.info(
                        f"Ruimte '{ruimte.naam}' ({ruimte.id}): {aantal}x een {installatiesoort.naam} voor {Woningwaarderingstelselgroep.sanitair.naam}."
                    )
                    yield voorzieningen_criterium.met_onderliggend(
                        id=installatiesoort.name,
                        naam=installatiesoort.naam,
                        meeteenheid=Meeteenheid.stuks,
                        punten=punten,
                        aantal=aantal,
                    )

                    if installatiesoort == Installatiesoort.kastruimte:
                        maximum = Decimal("0.75")
                        correctie = min(maximum - punten, Decimal("0"))
                        if correctie < 0:
                            totaal_punten_voorzieningen += correctie
                            logger.info(
                                f"Ruimte '{ruimte.naam}' ({ruimte.id}) correctie voor {installatiesoort.naam} van {correctie} punten in {Woningwaarderingstelselgroep.sanitair.naam}."
                            )
                            yield voorzieningen_criterium.met_onderliggend(
                                id=f"max_punten_{installatiesoort.name}",
                                naam=maximering_naam(
                                    gedeeld=_ruimte_gedeeld(ruimte),
                                    met_puntental=(
                                        f"Max {maximum} punten voor"
                                        f" {installatiesoort.naam}"
                                    ),
                                    gedeelde_naam=(
                                        f"Maximering voor {installatiesoort.naam}"
                                    ),
                                ),
                                punten=correctie,
                            )

                    if installatiesoort == Installatiesoort.stopcontact_bij_wastafel:
                        correctie_aantal = (totaal_aantal_wastafels * 2) - aantal
                        correctie = min(
                            Decimal(str(correctie_aantal))
                            * Decimal(_EXTRA_VOORZIENINGEN_PUNTEN[installatiesoort]),
                            Decimal("0"),
                        )
                        if correctie < 0:
                            totaal_punten_voorzieningen += correctie
                            logger.info(
                                f"Ruimte '{ruimte.naam}' ({ruimte.id}) correctie voor {installatiesoort.naam} van {correctie} punten want er zijn meer dan 2x zoveel stopcontacten ({aantal}) als wastafels ({totaal_aantal_wastafels})."
                            )
                            yield voorzieningen_criterium.met_onderliggend(
                                id=f"max_{Installatiesoort.stopcontact_bij_wastafel.name}",
                                naam="Max 2 stopcontacten per wastafel",
                                punten=correctie,
                            )

                # De punten voor extra voorzieningen tellen mee tot maximaal het
                # aantal punten voor bad en douche in dezelfde ruimte.
                if voorzieningen_criterium is not None:
                    maximering = min(
                        rond_af(
                            totaal_punten_bad_en_douche - totaal_punten_voorzieningen,
                            2,
                        ),
                        Decimal("0"),
                    )
                    if maximering < 0:
                        logger.info(
                            f"Ruimte '{ruimte.naam}' ({ruimte.id}): Maximering van {maximering} punten want maximaal evenveel punten voor bad en douche ({totaal_punten_bad_en_douche}) als voor voorzieningen ({totaal_punten_voorzieningen})."
                        )
                        yield voorzieningen_criterium.met_onderliggend(
                            id="maximering_punten_voorzieningen",
                            naam="Max verdubbeling punten bad en douche",
                            punten=maximering,
                        )


def _aantal_wastafels(
    waarderingen: list[WaarderingBuilder],
    ruimte_criterium: WaarderingBuilder,
    soort: Referentiedata,
) -> int:
    return int(
        sum(
            int(woningwaardering.aantal or 0)
            for woningwaardering in waarderingen
            if (
                woningwaardering.bovenliggende is ruimte_criterium
                and woningwaardering.segment == soort.name
                and woningwaardering.aantal is not None
            )
        )
    )


def _puntenwinst_wastafel_maximering(
    aantal_wastafels: int,
    aantal_meerpersoonswastafels: int,
    deler: int,
) -> Decimal:
    # Punten die de maximering per vertrek/overige ruimte zou afsnijden, gedeeld
    # door het aantal onzelfstandige woonruimten waarmee de ruimte wordt gedeeld.
    winst = Decimal("0")
    if aantal_wastafels > 1:
        winst += (Decimal(aantal_wastafels) - Decimal("1")) * _PUNTEN_WASTAFEL
    if aantal_meerpersoonswastafels > 1:
        winst += (
            Decimal(aantal_meerpersoonswastafels) - Decimal("1")
        ) * _PUNTEN_MEERPERSOONSWASTAFEL
    return winst / Decimal(deler)


def _bepaal_uitzonderingsruimte(
    ruimte_waarderingen: list[
        tuple[EenhedenRuimte, WaarderingBuilder, list[WaarderingBuilder]]
    ],
) -> EenhedenRuimte | None:
    # Bijlage I B, sanitair: maximaal één ruimte, naast de badkamer, mag meer
    # dan één (meerpersoons)wastafel hebben. We kiezen de vrijstellingskandidaat
    # met de hoogste puntenwinst; bij gelijke stand de eerste in de input.
    uitzonderingsruimte: EenhedenRuimte | None = None
    hoogste_winst: Decimal | None = None

    for ruimte, ruimte_criterium, waarderingen in ruimte_waarderingen:
        if not _vrijstellingskandidaat(ruimte):
            continue

        winst = _puntenwinst_wastafel_maximering(
            _aantal_wastafels(
                waarderingen, ruimte_criterium, Installatiesoort.wastafel
            ),
            _aantal_wastafels(
                waarderingen,
                ruimte_criterium,
                Installatiesoort.meerpersoonswastafel,
            ),
            ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1,
        )
        if hoogste_winst is None or winst > hoogste_winst:
            hoogste_winst = winst
            uitzonderingsruimte = ruimte

    if uitzonderingsruimte is not None:
        logger.info(
            f"Ruimte '{uitzonderingsruimte.naam}' ({uitzonderingsruimte.id}) "
            f"is de 8+-uitzonderingsruimte (puntenwinst {hoogste_winst})."
        )

    return uitzonderingsruimte


def _maximeer_wastafels_in_ruimte(
    ruimte: EenhedenRuimte,
    ruimte_criterium: WaarderingBuilder,
    waarderingen: list[WaarderingBuilder],
    *,
    soort: Referentiedata,
    uitzonderingsruimte: EenhedenRuimte | None,
    maximum: Decimal,
) -> None:
    # Maximeer alleen vrijstellingskandidaten die niet de uitzonderingsruimte zijn.
    if not _vrijstellingskandidaat(ruimte) or ruimte == uitzonderingsruimte:
        return

    # Tel alle wastafel-criteria in deze ruimte (inclusief spoelbakken in korte
    # aanrechten), zodat maximering hetzelfde totaal gebruikt als in
    # _waardeer_wastafels.
    totaal_aantal = _aantal_wastafels(waarderingen, ruimte_criterium, soort)
    if totaal_aantal <= 1:
        return

    logger.info(
        f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft {totaal_aantal} {soort.naam}. Maximaal {maximum} punt voor {soort.naam}."
    )
    correctie = rond_af(
        maximum - Decimal(str(totaal_aantal)) * maximum,
        decimalen=2,
    )
    waarderingen.append(
        ruimte_criterium.met_onderliggend(
            id=f"max_punten_{soort.name}",
            naam=maximering_naam(
                gedeeld=_ruimte_gedeeld(ruimte),
                met_puntental=f"Max {maximum} punt voor {soort.naam}",
                gedeelde_naam=f"Maximering voor {soort.naam}",
            ),
            punten=float(correctie),
        )
    )


def maximeer_wastafels(
    ruimte_waarderingen: list[
        tuple[EenhedenRuimte, WaarderingBuilder, list[WaarderingBuilder]]
    ],
) -> None:
    uitzonderingsruimte = _bepaal_uitzonderingsruimte(ruimte_waarderingen)

    for ruimte, ruimte_criterium, waarderingen in ruimte_waarderingen:
        _maximeer_wastafels_in_ruimte(
            ruimte,
            ruimte_criterium,
            waarderingen,
            soort=Installatiesoort.wastafel,
            uitzonderingsruimte=uitzonderingsruimte,
            maximum=_PUNTEN_WASTAFEL,
        )
        _maximeer_wastafels_in_ruimte(
            ruimte,
            ruimte_criterium,
            waarderingen,
            soort=Installatiesoort.meerpersoonswastafel,
            uitzonderingsruimte=uitzonderingsruimte,
            maximum=_PUNTEN_MEERPERSOONSWASTAFEL,
        )
