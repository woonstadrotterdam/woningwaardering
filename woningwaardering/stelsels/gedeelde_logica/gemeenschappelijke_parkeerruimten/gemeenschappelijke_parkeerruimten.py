import warnings
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.builders import (
    WaarderingBuilder,
    WaarderingsgroepBuilder,
)
from woningwaardering.stelsels.gedeelde_logica.parkeerruimten import (
    MINIMALE_OPPERVLAKTE_PARKEERVAK,
    PARKEERTYPE_PUNTEN,
    PUNTEN_PER_LAADPAAL,
    VERVALLEN_PARKEERGARAGE_DETAILSOORTEN,
    aantal_laadpalen,
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
    - Type I (in een afgesloten parkeergarage, in- of uitpandig: `PIP`, `PUP`):
      9 punten
    - Type II (`PBD`, of een gemeenschappelijke `carport`): 6 punten
    - Type III (`PBC`, of een gemeenschappelijke `parkeerplaats`): 4 punten

    Extra punten:
    - +2 punten bij aanwezigheid van een laadpaal die exclusief is voor gebruik
      door bewoners (2.10.5), maar alleen wanneer de parkeerruimte hier punten
      krijgt. Krijgt zij die niet, dan wordt de laadpaal in rubriek 12
      gewaardeerd.

    Voorwaarden:
    - Type-detailsoorten (`PIP`, `PUP`, `PBD`, `PBC`) worden hier altijd
      gewaardeerd, privé of gemeenschappelijk.
    - Een `carport` of `parkeerplaats` (VERA-buitenruimte) wordt hier alleen
      gewaardeerd wanneer zij gemeenschappelijk is; privé hoort zij in
      rubriek 8 Buitenruimten.
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

    # Bij een parkeerplaats in een gemeenschappelijke parkeerruimte
    # hoort een Type-detailsoort. De warning vuurt ook onder de 12 m²-eis.
    if ruimte.detail_soort == Ruimtedetailsoort.parkeerplaats and not utils.is_prive(
        ruimte
    ):
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een gemeenschappelijke {Ruimtedetailsoort.parkeerplaats}. Gebruik Type I, II of III ({Ruimtedetailsoort.parkeerplek_in_inpandige_afgesloten_parkeergarage}, {Ruimtedetailsoort.parkeerplek_in_uitpandige_afgesloten_parkeergarage}, {Ruimtedetailsoort.parkeerplek_buiten_met_dak_behorend_bij_complex} of {Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex}) voor een gemeenschappelijke parkeerplek: deze wordt nu gewaardeerd als Type III.",
            UserWarning,
        )

    if ruimte.oppervlakte is None:
        warnings.warn(f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen oppervlakte")
        return

    if ruimte.gedeeld_met_aantal_adressen is None:
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen 'gedeeld_met_aantal_adressen'. De waardering gaat uit van 1 (niet gedeeld). Zet 'gedeeld_met_aantal_adressen' >= 2 wanneer de ruimte gedeeld is."
        )

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
    weergavenaam = _weergavenaam(ruimte)
    criterium_id = _parkeer_criterium_id(weergavenaam, type_parkeerruimte)

    logger.info(
        f"Ruimte '{ruimte.naam}' ({ruimte.id}) wordt gewaardeerd als parkeerplek '{type_parkeerruimte}'."
    )

    plek = gedeeld_met_laag.met_onderliggend(
        id=criterium_id,
        naam=f"{weergavenaam} ({type_parkeerruimte})",
        meeteenheid=Meeteenheid.stuks,
        hergebruik=True,
    )
    _tel_op(
        plek,
        aantal=aantal_plekken,
        punten=totaal_punten_type_parkeeruimte,
    )

    # 2.10.5 Laadpalen: 2 extra punten per laadpaal, gedeeld door dezelfde deler.
    laadpalen = aantal_laadpalen(ruimte)
    if laadpalen:
        totaal_punten_laadpaal = PUNTEN_PER_LAADPAAL * Decimal(laadpalen) / deler

        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft {laadpalen} laadpaal/laadpalen bij '{type_parkeerruimte}'."
        )

        laadpaal = gedeeld_met_laag.met_onderliggend(
            id=f"{criterium_id}_laadpaal",
            naam="Laadpaal",
            meeteenheid=Meeteenheid.stuks,
            hergebruik=True,
        )
        _tel_op(laadpaal, aantal=laadpalen, punten=totaal_punten_laadpaal)


def _weergavenaam(ruimte: EenhedenRuimte) -> str:
    """Naam van de parkeerplek in de output: `ruimte.naam`, anders de detailsoort.

    Args:
        ruimte (EenhedenRuimte): De parkeerruimte.

    Returns:
        str: De weergavenaam.
    """
    if ruimte.naam:
        return ruimte.naam
    if ruimte.detail_soort is not None and ruimte.detail_soort.naam:
        return ruimte.detail_soort.naam
    return ruimte.id or "onbekend"


def _parkeer_criterium_id(weergavenaam: str, type_parkeerruimte: str) -> str:
    """Stabiel id-segment voor een gegroepeerde parkeerplek (weergavenaam + Type).

    Args:
        weergavenaam (str): De naam in de output.
        type_parkeerruimte (str): Type I, II of III.

    Returns:
        str: Het id-segment.
    """
    return f"{weergavenaam}_{type_parkeerruimte}".lower().replace(" ", "_")


def _tel_op(waardering: WaarderingBuilder, *, aantal: int, punten: Decimal) -> None:
    """Tel aantal en punten op bij een bestaande (hergebruikte) waardering.

    Args:
        waardering (WaarderingBuilder): De waardering die wordt bijgewerkt.
        aantal (int): Het aantal plekken of laadpalen om op te tellen.
        punten (Decimal): De punten om op te tellen.
    """
    waardering.aantal = int(waardering.aantal or 0) + aantal
    waardering.punten = utils.rond_af(
        Decimal(str(waardering.punten or 0)) + punten,
        decimalen=2,
    )
