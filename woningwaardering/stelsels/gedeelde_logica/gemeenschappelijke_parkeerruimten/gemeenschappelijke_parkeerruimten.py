import warnings
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.builders import WaarderingsgroepBuilder
from woningwaardering.stelsels.gedeelde_logica.parkeerruimten import (
    MINIMALE_OPPERVLAKTE_PARKEERVAK,
    PARKEERTYPE_PUNTEN,
    PUNTEN_PER_LAADPAAL,
    VERVALLEN_PARKEERGARAGE_DETAILSOORTEN,
    aantal_laadpalen,
    is_gemeenschappelijke_parkeerruimte,
    is_parkeerruimte,
    parkeertype,
    voldoet_aan_oppervlakte_eis,
    wordt_gewaardeerd_in_gemeenschappelijke_parkeerruimten,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Meeteenheid,
    Ruimtedetailsoort,
    Woningwaarderingstelselgroep,
)


def waardeer_gemeenschappelijke_parkeerruimte(
    ruimte: EenhedenRuimte,
    *,
    waarderingsgroep_builder: WaarderingsgroepBuilder,
) -> None:
    """Bepaalt de waardering voor gemeenschappelijke parkeerruimten (rubriek 10).

    Args:
        ruimte (EenhedenRuimte): De te waarderen ruimte
        waarderingsgroep_builder (WaarderingsgroepBuilder): waarderingsgroep waarin
            de hiërarchie wordt opgebouwd.

    De waardering wordt bepaald op basis van het type parkeerplek (2.10.3):
    - Type I (in een afgesloten parkeergarage bij het complex, in- of uitpandig:
      `PIP`, `PUP`): 9 punten
    - Type II (buiten bij het complex met dak: `PBD`, of een gemeenschappelijke
      `carport`): 6 punten
    - Type III (buiten bij het complex zonder dak: `PBC`, of een
      gemeenschappelijke `parkeerplaats`): 4 punten

    Extra punten:
    - +2 punten bij aanwezigheid van een laadpaal die exclusief is voor gebruik
      door bewoners (2.10.5), maar alleen wanneer de parkeerruimte hier punten
      krijgt. Krijgt zij die niet, dan wordt de laadpaal in rubriek 12
      gewaardeerd.

    Voorwaarden:
    - Parkeerplekken bij het complex (`PIP`, `PUP`, `PBD`, `PBC`) worden hier
      altijd gewaardeerd, privé of gemeenschappelijk: zij liggen altijd in een
      gemeenschappelijke parkeergelegenheid.
    - Een `carport` of `parkeerplaats` wordt hier alleen gewaardeerd wanneer zij
      gemeenschappelijk is; privé hoort zij in rubriek 8 Buitenruimten.
    - De oppervlakte moet minimaal 12 m² zijn.
    - Het aantal punten wordt gedeeld door het aantal adressen en het aantal
      onzelfstandige woonruimten op het adres.
    """
    if ruimte.detail_soort is None:
        warnings.warn(f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen detailsoort")
        return

    if ruimte.detail_soort in VERVALLEN_PARKEERGARAGE_DETAILSOORTEN:
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft als ruimtedetailsoort {ruimte.detail_soort}. Gebruik {Ruimtedetailsoort.parkeerplek_in_inpandige_afgesloten_parkeergarage}, {Ruimtedetailsoort.parkeerplek_in_uitpandige_afgesloten_parkeergarage}, {Ruimtedetailsoort.parkeerplek_buiten_met_dak_behorend_bij_complex}, {Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex} of {Ruimtedetailsoort.carport} als detailsoort om in aanmerking te komen voor een waardering onder {Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.naam}.",
            UserWarning,
        )
        return

    if not is_parkeerruimte(ruimte.detail_soort):
        logger.debug(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft detailsoort {ruimte.detail_soort} en valt buiten de parkeerregels."
        )
        return

    if not wordt_gewaardeerd_in_gemeenschappelijke_parkeerruimten(ruimte):
        # Een privé-carport of privé-parkeerplaats wordt in rubriek 8
        # Buitenruimten gewaardeerd; hier zou dat dubbeltelling opleveren.
        logger.debug(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een privé {ruimte.detail_soort.naam} en wordt gewaardeerd onder {Woningwaarderingstelselgroep.buitenruimten.naam}."
        )
        return

    # De waarschuwing hangt aan 'gemeenschappelijk', niet aan 'gewaardeerd': een
    # `parkeerplaats` is per definitie een privé-plek, dus een gemeenschappelijke
    # plek hoort een van de Type-detailsoorten te krijgen. De waarschuwing vuurt
    # daarom ook wanneer de plek onder de 12 m² blijft en nul punten krijgt.
    if (
        ruimte.detail_soort == Ruimtedetailsoort.parkeerplaats
        and is_gemeenschappelijke_parkeerruimte(ruimte)
    ):
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een gemeenschappelijke {Ruimtedetailsoort.parkeerplaats}. Gebruik Type I, II of III ({Ruimtedetailsoort.parkeerplek_in_inpandige_afgesloten_parkeergarage}, {Ruimtedetailsoort.parkeerplek_in_uitpandige_afgesloten_parkeergarage}, {Ruimtedetailsoort.parkeerplek_buiten_met_dak_behorend_bij_complex} of {Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex}) voor een gemeenschappelijke parkeerplek: deze wordt nu gewaardeerd als Type III.",
            UserWarning,
        )

    if ruimte.oppervlakte is None:
        warnings.warn(f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen oppervlakte")
        return

    if ruimte.gedeeld_met_aantal_adressen is None:
        # Zonder het aantal adressen is de deler onbekend. We kennen hier dan
        # geen punten toe in plaats van de plek als niet-gedeeld te waarderen:
        # dat zou bij een in werkelijkheid gedeelde plek het volle puntenaantal
        # aan elk adres toekennen. De laadpaal valt terug op rubriek 12, omdat
        # `krijgt_punten_in_gemeenschappelijke_parkeerruimten` deze ruimte niet
        # als gewaardeerd beschouwt.
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen 'gedeeld_met_aantal_adressen'. Zet 'gedeeld_met_aantal_adressen' >= 2 wanneer de ruimte gedeeld is. 'gedeeld_met_aantal_adressen' op 0 of 1 wordt beschouwd als niet gedeeld."
        )
        return

    if not voldoet_aan_oppervlakte_eis(ruimte):
        # 2.10.3 Een parkeerplek heeft een oppervlakte van minimaal 12 m².
        # De laadpaal volgt de ruimte en wordt dan in rubriek 12 gewaardeerd.
        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) voldoet niet aan de eis van {MINIMALE_OPPERVLAKTE_PARKEERVAK}m2 voor een parkeervak."
        )
        return

    type_parkeerruimte = parkeertype(ruimte)
    if type_parkeerruimte is None:  # pragma: no cover - afgevangen door de guards
        return

    aantal_adressen = ruimte.gedeeld_met_aantal_adressen or 1
    aantal_onzelfstandige_woonruimten = (
        ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten or 1
    )
    gedeeld_met_laag = waarderingsgroep_builder.gedeeld_met(
        aantal_adressen=aantal_adressen,
        aantal_onzelfstandige_woonruimten=aantal_onzelfstandige_woonruimten,
    )

    # 2.10.4 Rekenmethode: delen door aantal adressen; bij privé parkeerplek voor
    # één adres delen door 1. Onzelfstandig: daarna delen door aantal
    # onzelfstandige woonruimten op het adres.
    deler = utils.deler(ruimte)
    aantal_plekken = int(ruimte.aantal or 1)
    punten = PARKEERTYPE_PUNTEN[type_parkeerruimte]
    totaal_punten_type_parkeeruimte = punten * Decimal(aantal_plekken) / deler

    logger.info(
        f"Ruimte '{ruimte.naam}' ({ruimte.id}) wordt gewaardeerd als parkeerplek '{type_parkeerruimte}'."
    )

    gedeeld_met_laag.met_onderliggend(
        id=ruimte.id,
        naam=type_parkeerruimte,
        meeteenheid=Meeteenheid.stuks,
        aantal=aantal_plekken,
        punten=utils.rond_af(totaal_punten_type_parkeeruimte, decimalen=2),
    )

    # 2.10.5 Laadpalen: 2 extra punten per laadpaal, gedeeld door dezelfde deler.
    laadpalen = aantal_laadpalen(ruimte)
    if laadpalen:
        totaal_punten_laadpaal = PUNTEN_PER_LAADPAAL * Decimal(laadpalen) / deler

        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft {laadpalen} laadpaal/laadpalen bij '{type_parkeerruimte}'."
        )

        gedeeld_met_laag.met_onderliggend(
            id=f"{ruimte.id}_laadpaal",
            naam="Laadpaal",
            meeteenheid=Meeteenheid.stuks,
            aantal=laadpalen,
            punten=utils.rond_af(totaal_punten_laadpaal, decimalen=2),
        )
