import warnings
from collections import Counter
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels.utils import rond_af
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    Referentiedata,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
    Voorzieningsoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
    WoningwaarderingstelselgroepReferentiedata,
    WoningwaarderingstelselReferentiedata,
)
from woningwaardering.vera.utils import get_bouwkundige_elementen


def waardeer_sanitair(
    ruimte: EenhedenRuimte,
    stelselgroep: WoningwaarderingstelselgroepReferentiedata,
    stelsel: WoningwaarderingstelselReferentiedata,
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    if ruimte.detail_soort is None:
        warnings.warn(f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen detailsoort.")
        return

    _bouwkundige_elementen_naar_installaties(ruimte)

    yield from _waardeer_toiletten(ruimte)

    yield from _waardeer_wastafels(ruimte, stelsel)

    baden_en_douches_waarderingen = list(_waardeer_baden_en_douches(ruimte, stelsel))
    totaal_punten_bad_en_douche = Decimal(
        sum(
            Decimal(str(woningwaardering.punten))
            for woningwaardering in baden_en_douches_waarderingen
            if woningwaardering.punten is not None
        )
    )
    yield from baden_en_douches_waarderingen

    voorziening_waarderingen = list(_waardeer_installaties(ruimte, stelsel))
    totaal_punten_voorzieningen = Decimal(
        sum(
            Decimal(str(woningwaardering.punten))
            for woningwaardering in voorziening_waarderingen
            if woningwaardering.punten is not None
        )
    )
    yield from voorziening_waarderingen

    maximering = min(
        rond_af(totaal_punten_bad_en_douche - totaal_punten_voorzieningen, 2),
        Decimal("0"),
    )

    if maximering < 0:
        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}): Maximering van {maximering} punten want maximaal evenveel punten voor bad en douche ({totaal_punten_bad_en_douche}) als voor voorzieningen ({totaal_punten_voorzieningen})."
        )

        yield WoningwaarderingResultatenWoningwaardering(
            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=f"{ruimte.naam} - Voorzieningen: Max verdubbeling punten bad en douche"
            ),
            punten=float(maximering),
        )


def _bouwkundige_elementen_naar_installaties(ruimte: EenhedenRuimte) -> None:
    ruimte.installaties = ruimte.installaties or []
    # Backwards compatibiliteit voor bouwkundige elementen
    for bouwkundigelementdetailsoort, voorzieningsoort in {
        Bouwkundigelementdetailsoort.wastafel: Voorzieningsoort.wastafel,
        Bouwkundigelementdetailsoort.douche: Voorzieningsoort.douche,
        Bouwkundigelementdetailsoort.bad: Voorzieningsoort.bad,
        Bouwkundigelementdetailsoort.kast: Voorzieningsoort.kastruimte,
        Bouwkundigelementdetailsoort.closetcombinatie: Voorzieningsoort.staand_toilet,
        Bouwkundigelementdetailsoort.fontein: Voorzieningsoort.wastafel,
    }.items():
        bouwkundige_elementen = list(
            get_bouwkundige_elementen(ruimte, bouwkundigelementdetailsoort)
        )
        if bouwkundige_elementen:
            warnings.warn(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft een {bouwkundigelementdetailsoort.naam} als bouwkundig element. Dit dient als `Voorzieningsoort` '{voorzieningsoort}' op de ruimte onder `installaties` gespecificeerd te worden."
            )
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}): {bouwkundigelementdetailsoort.naam} wordt als {voorzieningsoort.naam} toegevoegd aan installaties"
            )
            ruimte.installaties.extend(
                [voorzieningsoort for _ in bouwkundige_elementen]
            )


def _waardeer_toiletten(
    ruimte: EenhedenRuimte,
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    installaties = Counter([installatie for installatie in ruimte.installaties or []])
    mapping_toilet: dict[Referentiedata, dict[Referentiedata, float]] = {
        Ruimtedetailsoort.toiletruimte: {
            Voorzieningsoort.hangend_toilet: 3.75,
            Voorzieningsoort.staand_toilet: 3.0,
        },
        Ruimtedetailsoort.badkamer: {
            Voorzieningsoort.hangend_toilet: 2.75,
            Voorzieningsoort.staand_toilet: 2.0,
        },
        Ruimtedetailsoort.badkamer_met_toilet: {
            Voorzieningsoort.hangend_toilet: 2.75,
            Voorzieningsoort.staand_toilet: 2.0,
        },
    }

    # Toiletten buiten toiletruimten en badkamers komen niet in aanmerking voor waardering.
    if ruimte.detail_soort in [
        Ruimtedetailsoort.toiletruimte,
        Ruimtedetailsoort.badkamer,
        Ruimtedetailsoort.badkamer_met_toilet,
        Ruimtedetailsoort.doucheruimte,
    ]:
        for toiletsoort in [
            Voorzieningsoort.hangend_toilet,
            Voorzieningsoort.staand_toilet,
        ]:
            aantal_toiletten = installaties[toiletsoort]

            if aantal_toiletten > 0:
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}): {aantal_toiletten}x een {toiletsoort.naam} voor {Woningwaarderingstelselgroep.sanitair.naam}."
                )
                yield WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=f"{ruimte.naam} - {toiletsoort.naam}",
                    ),
                    punten=float(
                        rond_af(
                            Decimal(
                                str(mapping_toilet[ruimte.detail_soort][toiletsoort])
                            )
                            * Decimal(str(aantal_toiletten)),
                            decimalen=2,
                        )
                    ),
                    aantal=aantal_toiletten,
                )


def _waardeer_wastafels(
    ruimte: EenhedenRuimte, stelsel: WoningwaarderingstelselReferentiedata
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    zelfstandige_woonruimte = (
        stelsel == Woningwaarderingstelsel.zelfstandige_woonruimten
    )
    installaties = Counter([installatie for installatie in ruimte.installaties or []])
    punten_sanitair = {
        Voorzieningsoort.wastafel: 1.0,
        Voorzieningsoort.meerpersoonswastafel: 1.5,
        Voorzieningsoort.douche: 4.0 if zelfstandige_woonruimte else 3.0,
        Voorzieningsoort.bad: 6.0 if zelfstandige_woonruimte else 5.0,
        Voorzieningsoort.bad_en_douche: 7.0 if zelfstandige_woonruimte else 6.0,
    }

    totaal_aantal_wastafels = 0

    for wastafelsoort in [
        Voorzieningsoort.wastafel,
        Voorzieningsoort.meerpersoonswastafel,
    ]:
        aantal_wastafels = installaties[wastafelsoort]

        # Een aanrecht met spoelbak, waarvan de lengte minder bedraagt dan 1 m,
        # voldoet dus niet aan de eis van 1 m en wordt daarom niet als aanrecht gewaardeerd,
        # maar als wastafel.
        aantal_spoelbakken = 0
        if wastafelsoort == Voorzieningsoort.wastafel and ruimte.detail_soort in (
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
                        yield WoningwaarderingResultatenWoningwaardering(
                            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                naam=f"{ruimte.naam} - {wastafelsoort.naam} (spoelbak in aanrecht < 1m)"
                            ),
                            punten=float(punten_sanitair[wastafelsoort]),
                            aantal=1,
                        )
                        aantal_spoelbakken += 1

        totaal_aantal_wastafels += aantal_wastafels

        punten_per_wastafel = Decimal(str(punten_sanitair[wastafelsoort]))

        punten_voor_wastafels = rond_af(
            Decimal(str(aantal_wastafels + aantal_spoelbakken)) * punten_per_wastafel,
            decimalen=2,
        )

        if aantal_wastafels > 0:
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}): {aantal_wastafels}x een {wastafelsoort.naam} voor {Woningwaarderingstelselgroep.sanitair.naam}."
            )
            yield (
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=f"{ruimte.naam} - {wastafelsoort.naam}"
                    ),
                    punten=float(
                        rond_af(
                            aantal_wastafels * punten_per_wastafel,
                            decimalen=2,
                        )
                    ),
                    aantal=aantal_wastafels,
                )
            )

            # Wastafels worden gewaardeerd tot een maximum van 1 punt,
            # meerpersoonswastafels tot een maximum van 1,5 punt,
            # per vertrek of overige ruimte, m.u.v. de badkamer.
            if (
                punten_voor_wastafels > punten_per_wastafel
                and ruimte.detail_soort
                not in [
                    Ruimtedetailsoort.badkamer,
                    Ruimtedetailsoort.badkamer_met_toilet,
                    Ruimtedetailsoort.doucheruimte,
                ]
                # Op een adres met minimaal acht of meer onzelfstandige woonruimten geldt dit maximum niet voor maximaal één ruimte.
                # Dat betekent dat er voor adressen met acht of meer onzelfstandige woonruimten maximaal één ruimte mag zijn,
                # naast de badkamer, met meer dan één wastafel die voor waardering in aanmerking komt.
                # Voor woonruimten met >= 8 onzelfstandige woonruimten passen we hier geen maximering toe,
                # dit doen we in de Sanitair class voor onzelfstandige woonruimten
                and (
                    ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten is None
                    or (
                        ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten is not None
                        and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten < 8
                    )
                )
            ):
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}): {punten_voor_wastafels} punten voor {wastafelsoort.naam} in {ruimte.detail_soort.naam if ruimte.detail_soort else ruimte.naam}. Correctie wordt toegepast ivm maximaal {punten_per_wastafel} punt."
                )
                yield WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=f"{ruimte.naam} - Max {punten_per_wastafel} punt voor {wastafelsoort.naam}",
                    ),
                    punten=rond_af(
                        punten_per_wastafel - punten_voor_wastafels,
                        decimalen=2,
                    ),
                )
    # Waarschuw indien er minder wastafels zijn dan ingebouwde kasten met wastafel
    # want een wastafel moet apart worden meegegeven
    aantal_ingebouwde_kasten = installaties[
        Voorzieningsoort.ingebouwd_kastje_met_in_of_opgebouwde_wastafel
    ]
    if totaal_aantal_wastafels < aantal_ingebouwde_kasten:
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}): {totaal_aantal_wastafels} wastafel(s) zijn minder dan het aantal ingebouwde kasten met wastafel ({aantal_ingebouwde_kasten})."
            f" Een wastafel in een {Voorzieningsoort.ingebouwd_kastje_met_in_of_opgebouwde_wastafel.naam} moet apart worden meegegeven."
        )


def _waardeer_baden_en_douches(
    ruimte: EenhedenRuimte, stelsel: WoningwaarderingstelselReferentiedata
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    installaties = Counter([installatie for installatie in ruimte.installaties or []])
    zelfstandige_woonruimte = (
        stelsel == Woningwaarderingstelsel.zelfstandige_woonruimten
    )
    punten_sanitair = {
        Voorzieningsoort.wastafel: 1.0,
        Voorzieningsoort.meerpersoonswastafel: 1.5,
        Voorzieningsoort.douche: 4.0 if zelfstandige_woonruimte else 3.0,
        Voorzieningsoort.bad: 6.0 if zelfstandige_woonruimte else 5.0,
        Voorzieningsoort.bad_en_douche: 7.0 if zelfstandige_woonruimte else 6.0,
    }
    aantal_douches = installaties[Voorzieningsoort.douche]
    aantal_baden = installaties[Voorzieningsoort.bad]

    aantal_bad_en_douches = min(aantal_douches, aantal_baden)

    if aantal_bad_en_douches > 0:
        punten = rond_af(
            Decimal(str(aantal_bad_en_douches))
            * Decimal(str(punten_sanitair[Voorzieningsoort.bad_en_douche])),
            decimalen=2,
        )
        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}): {aantal_bad_en_douches}x een {Voorzieningsoort.bad_en_douche.naam} voor {Woningwaarderingstelselgroep.sanitair.naam}"
        )
        yield (
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"{ruimte.naam} - {Voorzieningsoort.bad_en_douche.naam}"
                ),
                punten=float(punten),
                aantal=aantal_bad_en_douches,
            )
        )

    for voorzieningsoort in [
        Voorzieningsoort.bad,
        Voorzieningsoort.douche,
    ]:
        aantal = installaties[voorzieningsoort] - aantal_bad_en_douches
        if aantal > 0:
            punten = rond_af(
                Decimal(str(aantal)) * Decimal(str(punten_sanitair[voorzieningsoort])),
                2,
            )
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}): {aantal}x een {voorzieningsoort.naam} voor {Woningwaarderingstelselgroep.sanitair.naam}"
            )
            yield (
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=f"{ruimte.naam} - {voorzieningsoort.naam}"
                    ),
                    punten=float(punten),
                    aantal=aantal,
                )
            )


def _waardeer_installaties(
    ruimte: EenhedenRuimte, stelsel: WoningwaarderingstelselReferentiedata
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    installaties = Counter([installatie for installatie in ruimte.installaties or []])
    punten_voorzieningen: dict[Referentiedata, float] = {
        Voorzieningsoort.bubbelfunctie_van_het_bad: 1.5,
        Voorzieningsoort.douchewand: 1.25,
        Voorzieningsoort.handdoekenradiator: 0.75,
        Voorzieningsoort.ingebouwd_kastje_met_in_of_opgebouwde_wastafel: 1,
        Voorzieningsoort.kastruimte: 0.75,
        Voorzieningsoort.stopcontact_bij_wastafel: 0.25,
        Voorzieningsoort.eenhandsmengkraan: 0.25,
        Voorzieningsoort.thermostatische_mengkraan: 0.5,
    }

    totaal_punten_voorzieningen = Decimal("0")

    totaal_aantal_wastafels = (
        installaties[Voorzieningsoort.wastafel]
        + installaties[Voorzieningsoort.meerpersoonswastafel]
    )

    bad_en_of_douche_aanwezig = (
        installaties[Voorzieningsoort.bad]
        + installaties[Voorzieningsoort.douche]
        + installaties[Voorzieningsoort.bad_en_douche]
    ) > 0

    if ruimte.detail_soort in [
        Ruimtedetailsoort.badkamer,
        Ruimtedetailsoort.badkamer_met_toilet,
        Ruimtedetailsoort.doucheruimte,
    ]:
        # Geen waardering voor extra voorzieningen indien er geen wastafel in de ruimte is
        if totaal_aantal_wastafels == 0:
            warnings.warn(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}): geen wastafel aanwezig in {ruimte.detail_soort.naam}, extra voorzieningen worden niet gewaardeerd."
            )
        # Geen waardering voor extra voorzieningen indien er geen douche of bad in de ruimte is
        elif not bad_en_of_douche_aanwezig:
            warnings.warn(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}): geen bad of douche aanwezig in {ruimte.detail_soort.naam}, extra voorzieningen worden niet gewaardeerd."
            )
        elif totaal_aantal_wastafels > 0 and bad_en_of_douche_aanwezig:
            for installatie, aantal in installaties.items():
                if installatie not in (
                    set(punten_voorzieningen)
                    | {
                        Voorzieningsoort.wastafel,
                        Voorzieningsoort.meerpersoonswastafel,
                        Voorzieningsoort.bad_en_douche,
                        Voorzieningsoort.douche,
                        Voorzieningsoort.bad,
                    }
                    | {
                        Voorzieningsoort.hangend_toilet,
                        Voorzieningsoort.staand_toilet,
                    }
                ):
                    logger.debug(
                        f"Installatie {installatie.naam} komt niet in aanmerking voor waardering"
                    )
                    continue

                if installatie in punten_voorzieningen:
                    punten = rond_af(
                        Decimal(str(aantal))
                        * Decimal(str(punten_voorzieningen[installatie])),
                        decimalen=2,
                    )

                    totaal_punten_voorzieningen += punten

                    logger.info(
                        f"Ruimte '{ruimte.naam}' ({ruimte.id}): {aantal}x een {installatie.naam} voor {Woningwaarderingstelselgroep.sanitair.naam}."
                    )
                    yield (
                        WoningwaarderingResultatenWoningwaardering(
                            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                naam=f"{ruimte.naam} - Voorzieningen: {installatie.naam}",
                            ),
                            punten=float(punten),
                            aantal=aantal,
                        )
                    )

                    if installatie == Voorzieningsoort.kastruimte:
                        maximum = Decimal("0.75")
                        correctie = min(maximum - punten, Decimal("0"))
                        if correctie < 0:
                            totaal_punten_voorzieningen += correctie
                            logger.info(
                                f"Ruimte '{ruimte.naam}' ({ruimte.id}) correctie voor {installatie.naam} van {correctie} punten in {Woningwaarderingstelselgroep.sanitair.naam}."
                            )
                            yield WoningwaarderingResultatenWoningwaardering(
                                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                    naam=f"{ruimte.naam} - Voorzieningen: Max {maximum} punten voor {installatie.naam}"
                                ),
                                punten=float(correctie),
                            )

                    if installatie == Voorzieningsoort.stopcontact_bij_wastafel:
                        correctie_aantal = (totaal_aantal_wastafels * 2) - aantal
                        correctie = min(
                            Decimal(str(correctie_aantal))
                            * Decimal(punten_voorzieningen[installatie]),
                            Decimal("0"),
                        )
                        if correctie < 0:
                            totaal_punten_voorzieningen += correctie
                            logger.info(
                                f"Ruimte '{ruimte.naam}' ({ruimte.id}) correctie voor {installatie.naam} van {correctie} punten want er zijn meer dan 2x zoveel stopcontacten ({aantal}) als wastafels ({totaal_aantal_wastafels})."
                            )
                            yield WoningwaarderingResultatenWoningwaardering(
                                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                    naam=f"{ruimte.naam} - Voorzieningen: Max 2 stopcontacten per wastafel"
                                ),
                                punten=float(correctie),
                            )
