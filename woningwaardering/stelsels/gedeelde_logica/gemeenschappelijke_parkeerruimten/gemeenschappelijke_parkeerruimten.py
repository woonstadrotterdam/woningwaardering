import warnings
from decimal import Decimal
from typing import Generator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.criterium_id import CriteriumId
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    Referentiedata,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.utils import heeft_bouwkundig_element

parkeertype_punten_mapping: dict[Referentiedata, dict[str, Decimal]] = {
    Ruimtedetailsoort.inpandige_afgesloten_parkeerplek: {"Type I": Decimal("9.0")},
    Ruimtedetailsoort.uitpandige_afgesloten_parkeerplek: {"Type II": Decimal("6.0")},
    Ruimtedetailsoort.carport: {"Type II": Decimal("6.0")},
    Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex: {
        "Type III": Decimal("4.0")
    },
}


def waardeer_gemeenschappelijke_parkeerruimte(
    ruimte: EenhedenRuimte,
) -> Generator[WoningwaarderingResultatenWoningwaardering, None, None]:
    """Bepaalt de waardering voor gemeenschappelijke parkeerruimten.

    Args:
        ruimte (EenhedenRuimte): De te waarderen ruimte

    De waardering wordt bepaald op basis van het type parkeerruimte:
    - Type I (inpandige afgesloten parkeerplek): 9 punten
    - Type II (uitpandige afgesloten parkeerplek of carport): 6 punten
    - Type III (parkeerplek buiten behorend bij een complex): 4 punten

    Extra punten:
    - +2 punten bij aanwezigheid van een laadpaal

    Voorwaarden:
    - De oppervlakte moet minimaal 12m² zijn
    - Het aantal punten wordt gedeeld door het aantal eenheden waarmee de ruimte gedeeld is
    - De ruimte moet van één van de volgende detailsoorten zijn:
        - inpandige afgesloten parkeerplek
        - uitpandige afgesloten parkeerplek
        - carport
        - parkeerplek buiten behorend bij een complex

    Yields:
        WoningwaarderingResultatenWoningwaardering: Waardering voor een specifiek parkeertype
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
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft als ruimtedetailsoort {ruimte.detail_soort}. Gebruik {Ruimtedetailsoort.inpandige_afgesloten_parkeerplek}, {Ruimtedetailsoort.carport}, {Ruimtedetailsoort.uitpandige_afgesloten_parkeerplek} of {Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex} als detailsoort om in aanmerking te komen voor een waardering onder {Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.naam}.",
            UserWarning,
        )
        return None

    if ruimte.detail_soort not in [
        Ruimtedetailsoort.inpandige_afgesloten_parkeerplek,  # Type I
        Ruimtedetailsoort.uitpandige_afgesloten_parkeerplek,  # Type II
        Ruimtedetailsoort.carport,  # Type II
        Ruimtedetailsoort.parkeerplek_buiten_behorend_bij_complex,  # Type III
    ]:
        logger.debug(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft detailsoort {ruimte.detail_soort} en wordt niet gewaardeerd voor {Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.naam}."
        )
        return

    if ruimte.oppervlakte is None:
        warnings.warn(f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen oppervlakte")
        return

    if ruimte.gedeeld_met_aantal_eenheden is None:
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen 'gedeeld_met_aantal_eenheden'. Zet 'gedeeld_met_aantal_eenheden' >= 2 wanneer de ruimte gedeeld is. 'gedeeld_met_aantal_eenheden' op 0 of 1 wordt beschouwd als niet gedeeld."
        )
        return

    if not ruimte.oppervlakte >= 12.0:
        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) voldoet niet aan de eis van 12m2 voor een parkeervak."
        )
        return

    for (
        type_parkeeruimte,
        punten,
    ) in parkeertype_punten_mapping[ruimte.detail_soort].items():
        criterium = f"{type_parkeeruimte}"

        if heeft_bouwkundig_element(ruimte, Bouwkundigelementdetailsoort.laadpaal):
            punten += Decimal("2.0")
            criterium += " + laadpaal"

        if ruimte.gedeeld_met_aantal_eenheden >= 2:
            criterium += f" (gedeeld met {ruimte.gedeeld_met_aantal_eenheden} adressen)"
            totaal_punten_type_parkeeruimte = (
                punten * Decimal(str(ruimte.aantal))
            ) / Decimal(str(ruimte.gedeeld_met_aantal_eenheden))
        else:
            criterium += " (privé)"
            totaal_punten_type_parkeeruimte = (
                punten * Decimal(str(ruimte.aantal)) / Decimal("1")
            )

        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een gemeenschappelijke parkeerruimte '{criterium}'."
        )

        yield WoningwaarderingResultatenWoningwaardering(
            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                naam=criterium,
                id=str(
                    CriteriumId(
                        stelselgroep=Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten,
                        ruimte_id=ruimte.id,
                    )
                ),
            ),
            aantal=ruimte.aantal,
            punten=utils.rond_af(totaal_punten_type_parkeeruimte, decimalen=2),
        )
    return
