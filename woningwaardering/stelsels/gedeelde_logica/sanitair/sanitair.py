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
from woningwaardering.stelsels.gedeelde_logica.aanrecht import (
    AANRECHT_MINIMALE_LENGTE_MM,
)
from woningwaardering.stelsels.gedeelde_logica.keuken import (
    OPEN_KEUKEN_DETAIL_SOORTEN,
    VERTREK_MET_AANRECHT_DETAIL_SOORTEN,
)
from woningwaardering.stelsels.utils import (
    gedeeld_met_adressen,
    gedeeld_met_onzelfstandige_woonruimten,
    rond_af,
)
from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenEenheid,
    EenhedenRuimte,
    Referentiedata,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Doelgroep,
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

# Bij een adres met 8 of meer onzelfstandige woonruimten geldt voor maximaal één
# niet-badkamer-ruimte een uitzondering op de wastafelmaximering.

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
    wastafel_uitzonderingsruimte: EenhedenRuimte | None = None,
) -> list[WaarderingBuilder]:
    if ruimte.detail_soort is None:
        warnings.warn(f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen detailsoort.")
        return []

    ruimte_criterium = waarderingsgroep_builder.met_subgroep(
        id=ruimte.id,
        naam=ruimte.naam
        or ruimte.id
        or (ruimte.detail_soort.naam if ruimte.detail_soort else ""),
    )

    detail_waarderingen: list[WaarderingBuilder] = [
        *list(_waardeer_toiletten(ruimte, ruimte_criterium)),
        *list(
            _waardeer_wastafels(
                ruimte,
                ruimte_criterium,
                uitzonderingsruimte=wastafel_uitzonderingsruimte,
            )
        ),
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


def converteer_bouwkundige_elementen_naar_installaties(
    eenheid: EenhedenEenheid,
) -> None:
    # Backwards compatibiliteit voor bouwkundige elementen
    for ruimte in eenheid.ruimten or []:
        ruimte.installaties = ruimte.installaties or []
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
            if not bouwkundige_elementen:
                continue
            if installatiesoort in ruimte.installaties:
                continue
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


def _korte_aanrechten(
    ruimte: EenhedenRuimte,
) -> list[BouwkundigElementenBouwkundigElement]:
    if ruimte.detail_soort not in (
        Ruimtedetailsoort.keuken,
        *OPEN_KEUKEN_DETAIL_SOORTEN,
        *VERTREK_MET_AANRECHT_DETAIL_SOORTEN,
    ):
        return []

    return [
        element
        for element in ruimte.bouwkundige_elementen or []
        if element.detail_soort == Bouwkundigelementdetailsoort.aanrecht
        and element.lengte is not None
        and element.lengte < AANRECHT_MINIMALE_LENGTE_MM
    ]


def _aantal_wastafels_in_ruimte(
    ruimte: EenhedenRuimte,
    soort: InstallatiesoortReferentiedata,
) -> int:
    aantal = Counter(ruimte.installaties or [])[soort]
    if soort == Installatiesoort.wastafel:
        aantal += len(_korte_aanrechten(ruimte))
    return aantal


def _is_wastafel_uitzonderingskandidaat(
    ruimte: EenhedenRuimte,
    *,
    zorgwoning: bool,
) -> bool:
    if ruimte.soort is None or ruimte.detail_soort is None:
        return False
    if _is_badkamerachtige_ruimte(ruimte):
        return False
    if zorgwoning and gedeeld_met_adressen(ruimte):
        return False
    return True


def _netto_winst_wastafelmaximering(ruimte: EenhedenRuimte) -> Decimal:
    bruto_winst = sum(
        Decimal(max(_aantal_wastafels_in_ruimte(ruimte, soort) - 1, 0))
        * Decimal(str(_WASTAFEL_PUNTEN[soort]))
        for soort in (
            Installatiesoort.wastafel,
            Installatiesoort.meerpersoonswastafel,
        )
    )
    if bruto_winst <= 0:
        return Decimal("0")

    deler = Decimal(
        (ruimte.gedeeld_met_aantal_adressen or 1)
        * (ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1)
    )
    return bruto_winst / deler


def bepaal_wastafel_uitzonderingsruimte(
    eenheid: EenhedenEenheid,
) -> EenhedenRuimte | None:
    # Bijlage I, onder B, rubriek 6:
    # "Daarnaast geldt er voor adressen met 8 of meer onzelfstandige
    # woonruimten dat er voor maximaal één ruimte, naast de badkamer, een ruimte
    # mag zijn met meer dan één wastafel die voor waardering in aanmerking komt."
    if not any(
        (ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 0) >= 8
        for ruimte in eenheid.ruimten or []
    ):
        return None

    kandidaten = [
        ruimte
        for ruimte in eenheid.ruimten or []
        if _is_wastafel_uitzonderingskandidaat(
            ruimte,
            zorgwoning=eenheid.doelgroep == Doelgroep.zorg,
        )
    ]
    if not kandidaten:
        return None
    return max(kandidaten, key=_netto_winst_wastafelmaximering)


def _waardeer_wastafels(
    ruimte: EenhedenRuimte,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
    *,
    uitzonderingsruimte: EenhedenRuimte | None,
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
        aantal_spoelbakken = (
            len(_korte_aanrechten(ruimte))
            if wastafelsoort == Installatiesoort.wastafel
            else 0
        )

        totaal_aantal_wastafels += aantal_wastafels

        punten_per_wastafel = Decimal(str(_WASTAFEL_PUNTEN[wastafelsoort]))

        punten_voor_wastafels = rond_af(
            Decimal(str(aantal_wastafels + aantal_spoelbakken)) * punten_per_wastafel,
            decimalen=2,
        )

        if aantal_spoelbakken > 0:
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}): {aantal_spoelbakken}x aanrecht < 1m telt als wastafel mee voor {Woningwaarderingstelselgroep.sanitair.naam}."
            )
            yield waarderingsgroep_builder.met_onderliggend(
                id=wastafelsoort.name,
                naam=f"{wastafelsoort.naam} (spoelbak in aanrecht < 1m)",
                meeteenheid=Meeteenheid.stuks,
                punten=rond_af(
                    aantal_spoelbakken * punten_per_wastafel,
                    decimalen=2,
                ),
                aantal=aantal_spoelbakken,
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
        if (
            punten_voor_wastafels > punten_per_wastafel
            and not _is_badkamerachtige_ruimte(ruimte)
            and ruimte is not uitzonderingsruimte
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
