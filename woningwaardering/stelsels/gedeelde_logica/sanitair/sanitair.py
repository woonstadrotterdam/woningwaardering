import warnings
from collections import Counter
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels.criterium_id import CriteriumId
from woningwaardering.stelsels.utils import rond_af
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
    Referentiedata,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Installatiesoort,
    Ruimtedetailsoort,
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
                naam=f"{ruimte.naam} - Voorzieningen: Max verdubbeling punten bad en douche",
                id=str(
                    CriteriumId(
                        stelselgroep=Woningwaarderingstelselgroep.sanitair,
                        ruimte_id=ruimte.id,
                        criterium="maximering_punten_voorzieningen",
                    )
                ),
            ),
            punten=float(maximering),
        )


def bouwkundige_elementen_naar_installaties(
    eenheid: EenhedenEenheid, voorkom_duplicaten: bool = False
) -> None:
    """Converteer bouwkundige elementen naar installaties voor alle ruimten in een eenheid."""
    for ruimte in eenheid.ruimten or []:
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
                aantal_bouwkundige_elementen = len(bouwkundige_elementen)
                warnings.warn(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft {aantal_bouwkundige_elementen}x {bouwkundigelementdetailsoort.naam} als bouwkundig element. Dit dient als `Installatiesoort` '{installatiesoort}' op de ruimte onder `installaties` gespecificeerd te worden."
                )

                if voorkom_duplicaten:
                    # Tel hoeveel van deze installatiesoort al aanwezig zijn
                    bestaande_installaties = (
                        ruimte.installaties.count(installatiesoort)
                        if ruimte.installaties
                        else 0
                    )

                    # Voeg alleen toe wat nog niet als installatie gespecificeerd is
                    aantal_toe_te_voegen = max(
                        0, aantal_bouwkundige_elementen - bestaande_installaties
                    )

                    if aantal_toe_te_voegen > 0:
                        logger.info(
                            f"Ruimte '{ruimte.naam}' ({ruimte.id}): {aantal_toe_te_voegen}x {bouwkundigelementdetailsoort.naam} wordt als {installatiesoort.naam} toegevoegd aan installaties"
                        )
                        ruimte.installaties.extend(
                            [installatiesoort for _ in range(aantal_toe_te_voegen)]
                        )
                    elif bestaande_installaties >= aantal_bouwkundige_elementen:
                        logger.info(
                            f"Ruimte '{ruimte.naam}' ({ruimte.id}): {aantal_bouwkundige_elementen}x {bouwkundigelementdetailsoort.naam} als bouwkundig element is al gespecificeerd onder installaties als {installatiesoort.naam}"
                        )
                else:
                    # Voeg alle bouwkundige elementen toe als installaties zonder rekening te houden met bestaande installaties
                    logger.info(
                        f"Ruimte '{ruimte.naam}' ({ruimte.id}): {aantal_bouwkundige_elementen}x {bouwkundigelementdetailsoort.naam} wordt als {installatiesoort.naam} toegevoegd aan installaties"
                    )
                    ruimte.installaties.extend(
                        [installatiesoort for _ in range(aantal_bouwkundige_elementen)]
                    )

                # Verwijder de oorspronkelijke bouwkundige elementen
                if ruimte.bouwkundige_elementen:
                    ruimte.bouwkundige_elementen = [
                        element
                        for element in ruimte.bouwkundige_elementen
                        if element.detail_soort != bouwkundigelementdetailsoort
                    ]


def _waardeer_toiletten(
    ruimte: EenhedenRuimte,
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    installaties = Counter([installatie for installatie in ruimte.installaties or []])
    mapping_toilet: dict[Referentiedata, dict[Referentiedata, float]] = {
        Ruimtedetailsoort.toiletruimte: {
            Installatiesoort.hangend_toilet: 3.75,
            Installatiesoort.staand_toilet: 3.0,
        },
        Ruimtedetailsoort.badkamer: {
            Installatiesoort.hangend_toilet: 2.75,
            Installatiesoort.staand_toilet: 2.0,
        },
        Ruimtedetailsoort.badkamer_met_toilet: {
            Installatiesoort.hangend_toilet: 2.75,
            Installatiesoort.staand_toilet: 2.0,
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
            Installatiesoort.hangend_toilet,
            Installatiesoort.staand_toilet,
        ]:
            aantal_toiletten = installaties[toiletsoort]

            if aantal_toiletten > 0:
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}): {aantal_toiletten}x een {toiletsoort.naam} voor {Woningwaarderingstelselgroep.sanitair.naam}."
                )
                yield WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=f"{ruimte.naam} - {toiletsoort.naam}",
                        id=str(
                            CriteriumId(
                                stelselgroep=Woningwaarderingstelselgroep.sanitair,
                                ruimte_id=ruimte.id,
                                criterium=toiletsoort.name,
                            )
                        ),
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
        Installatiesoort.wastafel: 1.0,
        Installatiesoort.meerpersoonswastafel: 1.5,
        Installatiesoort.douche: 4.0 if zelfstandige_woonruimte else 3.0,
        Installatiesoort.bad: 6.0 if zelfstandige_woonruimte else 5.0,
        Installatiesoort.bad_en_douche: 7.0 if zelfstandige_woonruimte else 6.0,
    }

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
                        yield WoningwaarderingResultatenWoningwaardering(
                            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                naam=f"{ruimte.naam} - {wastafelsoort.naam} (spoelbak in aanrecht < 1m)",
                                id=str(
                                    CriteriumId(
                                        stelselgroep=Woningwaarderingstelselgroep.sanitair,
                                        ruimte_id=ruimte.id,
                                        criterium=wastafelsoort.name,
                                    )
                                ),
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
                        naam=f"{ruimte.naam} - {wastafelsoort.naam}",
                        id=str(
                            CriteriumId(
                                stelselgroep=Woningwaarderingstelselgroep.sanitair,
                                ruimte_id=ruimte.id,
                                criterium=wastafelsoort.name,
                            )
                        ),
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
                        id=str(
                            CriteriumId(
                                stelselgroep=Woningwaarderingstelselgroep.sanitair,
                                ruimte_id=ruimte.id,
                                criterium=f"max_punten_{wastafelsoort.name}",
                            )
                        ),
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
    ruimte: EenhedenRuimte, stelsel: WoningwaarderingstelselReferentiedata
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    installaties = Counter([installatie for installatie in ruimte.installaties or []])
    zelfstandige_woonruimte = (
        stelsel == Woningwaarderingstelsel.zelfstandige_woonruimten
    )
    punten_sanitair = {
        Installatiesoort.wastafel: 1.0,
        Installatiesoort.meerpersoonswastafel: 1.5,
        Installatiesoort.douche: 4.0 if zelfstandige_woonruimte else 3.0,
        Installatiesoort.drempelloze_inrijdouche: 4.0
        if zelfstandige_woonruimte
        else 3.0,
        Installatiesoort.bad: 6.0 if zelfstandige_woonruimte else 5.0,
        Installatiesoort.bad_en_douche: 7.0 if zelfstandige_woonruimte else 6.0,
    }
    aantal_douches = (
        installaties[Installatiesoort.douche]
        + installaties[Installatiesoort.drempelloze_inrijdouche]
    )
    aantal_baden = installaties[Installatiesoort.bad]

    aantal_bad_en_douches = min(aantal_douches, aantal_baden)

    if aantal_bad_en_douches > 0:
        punten = rond_af(
            Decimal(str(aantal_bad_en_douches))
            * Decimal(str(punten_sanitair[Installatiesoort.bad_en_douche])),
            decimalen=2,
        )
        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}): {aantal_bad_en_douches}x een {Installatiesoort.bad_en_douche.naam} voor {Woningwaarderingstelselgroep.sanitair.naam}"
        )
        yield (
            WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"{ruimte.naam} - {Installatiesoort.bad_en_douche.naam}",
                    id=str(
                        CriteriumId(
                            stelselgroep=Woningwaarderingstelselgroep.sanitair,
                            ruimte_id=ruimte.id,
                            criterium=Installatiesoort.bad_en_douche.name,
                        )
                    ),
                ),
                punten=float(punten),
                aantal=aantal_bad_en_douches,
            )
        )

    for installatiesoort in [
        Installatiesoort.bad,
        Installatiesoort.douche,
        Installatiesoort.drempelloze_inrijdouche,
    ]:
        aantal = installaties[installatiesoort] - aantal_bad_en_douches
        if aantal > 0:
            punten = rond_af(
                Decimal(str(aantal)) * Decimal(str(punten_sanitair[installatiesoort])),
                2,
            )
            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}): {aantal}x een {installatiesoort.naam} voor {Woningwaarderingstelselgroep.sanitair.naam}"
            )
            yield (
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=f"{ruimte.naam} - {installatiesoort.naam}",
                        id=str(
                            CriteriumId(
                                stelselgroep=Woningwaarderingstelselgroep.sanitair,
                                ruimte_id=ruimte.id,
                                criterium=installatiesoort.name,
                            )
                        ),
                    ),
                    punten=float(punten),
                    aantal=aantal,
                )
            )


def _waardeer_installaties(
    ruimte: EenhedenRuimte, stelsel: WoningwaarderingstelselReferentiedata
) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
    installaties = Counter([installatie for installatie in ruimte.installaties or []])
    punten_installaties: dict[Referentiedata, float] = {
        Installatiesoort.bubbelfunctie_van_het_bad: 1.5,
        Installatiesoort.douchewand: 1.25,
        Installatiesoort.handdoekenradiator: 0.75,
        Installatiesoort.ingebouwd_kastje_met_in_of_opgebouwde_wastafel: 1,
        Installatiesoort.kastruimte: 0.75,
        Installatiesoort.stopcontact_bij_wastafel: 0.25,
        Installatiesoort.eenhandsmengkraan: 0.25,
        Installatiesoort.thermostatische_mengkraan: 0.5,
    }

    totaal_punten_voorzieningen = Decimal("0")

    totaal_aantal_wastafels = (
        installaties[Installatiesoort.wastafel]
        + installaties[Installatiesoort.meerpersoonswastafel]
    )

    bad_en_of_douche_aanwezig = (
        installaties[Installatiesoort.bad]
        + installaties[Installatiesoort.douche]
        + installaties[Installatiesoort.bad_en_douche]
    ) > 0

    if ruimte.detail_soort in [
        Ruimtedetailsoort.badkamer,
        Ruimtedetailsoort.badkamer_met_toilet,
        Ruimtedetailsoort.doucheruimte,
    ]:
        heeft_extra_voorzieningen = any(
            installatie in punten_installaties for installatie in installaties
        )

        if heeft_extra_voorzieningen:
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
                        set(punten_installaties)
                        | {
                            Installatiesoort.wastafel,
                            Installatiesoort.meerpersoonswastafel,
                            Installatiesoort.bad_en_douche,
                            Installatiesoort.douche,
                            Installatiesoort.bad,
                        }
                        | {
                            Installatiesoort.hangend_toilet,
                            Installatiesoort.staand_toilet,
                        }
                    ):
                        logger.debug(
                            f"Installatie {installatie.naam} komt niet in aanmerking voor waardering"
                        )
                        continue

                    if installatie in punten_installaties:
                        punten = rond_af(
                            Decimal(str(aantal))
                            * Decimal(str(punten_installaties[installatie])),
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
                                    id=str(
                                        CriteriumId(
                                            stelselgroep=Woningwaarderingstelselgroep.sanitair,
                                            ruimte_id=ruimte.id,
                                            criterium=installatie.name,
                                        )
                                    ),
                                ),
                                punten=float(punten),
                                aantal=aantal,
                            )
                        )

                        if installatie == Installatiesoort.kastruimte:
                            maximum = Decimal("0.75")
                            correctie = min(maximum - punten, Decimal("0"))
                            if correctie < 0:
                                totaal_punten_voorzieningen += correctie
                                logger.info(
                                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) correctie voor {installatie.naam} van {correctie} punten in {Woningwaarderingstelselgroep.sanitair.naam}."
                                )
                                yield WoningwaarderingResultatenWoningwaardering(
                                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                        naam=f"{ruimte.naam} - Voorzieningen: Max {maximum} punten voor {installatie.naam}",
                                        id=str(
                                            CriteriumId(
                                                stelselgroep=Woningwaarderingstelselgroep.sanitair,
                                                ruimte_id=ruimte.id,
                                                criterium=f"max_punten_{installatie.name}",
                                            )
                                        ),
                                    ),
                                    punten=float(correctie),
                                )

                        if installatie == Installatiesoort.stopcontact_bij_wastafel:
                            correctie_aantal = (totaal_aantal_wastafels * 2) - aantal
                            correctie = min(
                                Decimal(str(correctie_aantal))
                                * Decimal(punten_installaties[installatie]),
                                Decimal("0"),
                            )
                            if correctie < 0:
                                totaal_punten_voorzieningen += correctie
                                logger.info(
                                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) correctie voor {installatie.naam} van {correctie} punten want er zijn meer dan 2x zoveel stopcontacten ({aantal}) als wastafels ({totaal_aantal_wastafels})."
                                )
                                yield WoningwaarderingResultatenWoningwaardering(
                                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                        naam=f"{ruimte.naam} - Voorzieningen: Max 2 stopcontacten per wastafel",
                                        id=str(
                                            CriteriumId(
                                                stelselgroep=Woningwaarderingstelselgroep.sanitair,
                                                ruimte_id=ruimte.id,
                                                criterium=f"max_{Installatiesoort.stopcontact_bij_wastafel.name}",
                                            )
                                        ),
                                    ),
                                    punten=float(correctie),
                                )
