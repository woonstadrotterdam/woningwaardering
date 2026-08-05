import warnings
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.builders import WaarderingsgroepBuilder
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    Referentiedata,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Meeteenheid,
    Ruimtedetailsoort,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.utils import heeft_bouwkundig_element

parkeertype_punten_mapping: dict[Referentiedata, dict[str, Decimal]] = {
    Ruimtedetailsoort.parkeerplek_in_inpandige_afgesloten_parkeergarage: {
        "Type I": Decimal("9.0")
    },
    Ruimtedetailsoort.parkeerplek_in_uitpandige_afgesloten_parkeergarage: {
        "Type II": Decimal("6.0")
    },
    Ruimtedetailsoort.carport: {"Type II": Decimal("6.0")},
    Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex: {
        "Type III": Decimal("4.0")
    },
}


def is_parkeer_detailsoort_voor_gemeenschappelijke_parkeerruimten(
    detail_soort: Referentiedata | None,
) -> bool:
    """Of het detailsoort een van de specifieke parkeer-detailsoorten van rubriek 10 is."""
    return detail_soort in parkeertype_punten_mapping


def kwalificeert_voor_gemeenschappelijke_parkeerruimte(
    ruimte: EenhedenRuimte,
) -> bool:
    """Of de ruimte in rubriek 10 daadwerkelijk punten krijgt.

    Naast een specifieke parkeer-detailsoort vereist rubriek 10 een oppervlakte
    van minimaal 12 m² en een ingevuld `gedeeld_met_aantal_adressen`.
    """
    return (
        is_parkeer_detailsoort_voor_gemeenschappelijke_parkeerruimten(
            ruimte.detail_soort
        )
        and ruimte.oppervlakte is not None
        and ruimte.oppervlakte >= 12.0
        and ruimte.gedeeld_met_aantal_adressen is not None
    )


def waardeer_gemeenschappelijke_parkeerruimte(
    ruimte: EenhedenRuimte,
    *,
    waarderingsgroep_builder: WaarderingsgroepBuilder,
) -> None:
    """Bepaalt de waardering voor gemeenschappelijke parkeerruimten.

    Args:
        ruimte (EenhedenRuimte): De te waarderen ruimte
        waarderingsgroep_builder (WaarderingsgroepBuilder): waarderingsgroep waarin
            de hiërarchie wordt opgebouwd.

    De waardering wordt bepaald op basis van het type parkeerruimte:
    - Type I (inpandige afgesloten parkeerplek): 9 punten
    - Type II (uitpandige afgesloten parkeerplek of carport): 6 punten
    - Type III (parkeerplek buiten behorend bij een complex): 4 punten

    Extra punten:
    - +2 punten bij aanwezigheid van een laadpaal die exclusief is voor gebruik
      door bewoners (2.10.5).

    Voorwaarden:
    - De oppervlakte moet minimaal 12m² zijn
    - Het aantal punten wordt gedeeld door het aantal adressen en (bij onzelfstandig)
      het aantal onzelfstandige woonruimten op het adres
    - De ruimte moet van één van de volgende detailsoorten zijn:
        - inpandige afgesloten parkeerplek
        - uitpandige afgesloten parkeerplek
        - carport
        - parkeerplek buiten behorend bij een complex
    """
    if ruimte.detail_soort is None:
        warnings.warn(f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen detailsoort")
        return

    if ruimte.detail_soort in [
        # onderstaande parkeergelegenden worden vervangen: https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/110#issuecomment-2190641829
        Ruimtedetailsoort.open_parkeergarage_niet_specifieke_plek,
        Ruimtedetailsoort.open_parkeergarage_specifieke_plek,
        Ruimtedetailsoort.parkeergarage_niet_specifieke_plek,
        Ruimtedetailsoort.specifieke_parkeerplek_in_parkeergarage,
    ]:
        detailsoorten = list(parkeertype_punten_mapping)
        if len(detailsoorten) > 1:
            geaccepteerde_detailsoorten = (
                ", ".join(str(detailsoort) for detailsoort in detailsoorten[:-1])
                + f" of {detailsoorten[-1]}"
            )
        else:
            geaccepteerde_detailsoorten = str(detailsoorten[0])
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft als ruimtedetailsoort {ruimte.detail_soort}. Gebruik {geaccepteerde_detailsoorten} als detailsoort om in aanmerking te komen voor een waardering onder {Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.naam}.",
            UserWarning,
        )
        return

    if not is_parkeer_detailsoort_voor_gemeenschappelijke_parkeerruimten(
        ruimte.detail_soort
    ):
        logger.debug(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft detailsoort {ruimte.detail_soort} en wordt niet gewaardeerd voor {Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.naam}."
        )
        return

    if ruimte.oppervlakte is None:
        warnings.warn(f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen oppervlakte")
        return

    if ruimte.gedeeld_met_aantal_adressen is None:
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen 'gedeeld_met_aantal_adressen'. Zet 'gedeeld_met_aantal_adressen' >= 2 wanneer de ruimte gedeeld is. 'gedeeld_met_aantal_adressen' op 0 of 1 wordt beschouwd als niet gedeeld."
        )
        return

    if not ruimte.oppervlakte >= 12.0:
        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) voldoet niet aan de eis van 12m2 voor een parkeervak."
        )
        return

    # Een parkeerruimte waartoe bewoners van één adres op grond van de huurovereenkomst
    # exclusieve toegang hebben, wordt gewaardeerd volgens rubriek 2 (bijvoorbeeld een
    # garagebox behorende tot de woning) of rubriek 8 (bijvoorbeeld een oprit exclusief
    # behorende tot de woning). Zie ook de implementatietoelichting voor privé-parkeerplekken
    # die met onzelfstandige woonruimten gedeeld worden.
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
    deler = Decimal(aantal_adressen * aantal_onzelfstandige_woonruimten)
    heeft_laadpaal = heeft_bouwkundig_element(
        ruimte, Bouwkundigelementdetailsoort.laadpaal
    )

    for (
        type_parkeeruimte,
        punten,
    ) in parkeertype_punten_mapping[ruimte.detail_soort].items():
        totaal_punten_type_parkeeruimte = punten * Decimal(str(ruimte.aantal)) / deler

        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een gemeenschappelijke parkeerruimte '{type_parkeeruimte}'."
        )

        gedeeld_met_laag.met_onderliggend(
            id=ruimte.id,
            naam=type_parkeeruimte,
            meeteenheid=Meeteenheid.stuks,
            aantal=ruimte.aantal,
            punten=utils.rond_af(totaal_punten_type_parkeeruimte, decimalen=2),
        )

        # 2.10.5 Laadpalen: 2 extra punten.
        if heeft_laadpaal:
            totaal_punten_laadpaal = (
                Decimal("2.0") * Decimal(str(ruimte.aantal)) / deler
            )

            logger.info(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft een laadpaal bij '{type_parkeeruimte}'."
            )

            gedeeld_met_laag.met_onderliggend(
                id=f"{ruimte.id}_laadpaal",
                naam="Laadpaal",
                meeteenheid=Meeteenheid.stuks,
                aantal=ruimte.aantal,
                punten=utils.rond_af(totaal_punten_laadpaal, decimalen=2),
            )
