import warnings
from decimal import Decimal
from typing import Generator

from loguru import logger

from woningwaardering.stelsels import utils
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
    Ruimtedetailsoort.parkeervak_auto_binnen: {"Type I": Decimal("9.0")},
    Ruimtedetailsoort.carport: {"Type II": Decimal("6.0")},
    Ruimtedetailsoort.parkeervak_auto_buiten_niet_overdekt: {
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
    - Type I (parkeervak auto binnen): 9 punten
    - Type II (carport): 6 punten
    - Type III (parkeervak auto buiten niet overdekt): 4 punten

    Extra punten:
    - +2 punten bij aanwezigheid van een laadpaal

    Voorwaarden:
    - De oppervlakte moet minimaal 12m² zijn
    - Het aantal punten wordt gedeeld door het aantal eenheden waarmee de ruimte gedeeld is
    - De ruimte moet van één van de volgende detailsoorten zijn:
        - parkeervak auto binnen
        - carport
        - parkeervak auto buiten niet overdekt

    Yields:
        WoningwaarderingResultatenWoningwaardering: Waardering voor een specifiek parkeertype
    """
    if ruimte.detail_soort is None:
        warnings.warn(f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen detailsoort")
        return

    if ruimte.detail_soort in [
        Ruimtedetailsoort.parkeervak_motorfiets_binnen,
        Ruimtedetailsoort.parkeervak_scootmobiel_binnen,
        Ruimtedetailsoort.stalling_extern,
        Ruimtedetailsoort.stalling_intern,
        Ruimtedetailsoort.parkeervak_motorfiets_buiten_niet_overdekt,
        Ruimtedetailsoort.parkeervak_scootmobiel_buiten,
    ]:
        logger.debug(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) met ruimtedetailsoort {ruimte.detail_soort} is een parkeerplek die niet gewaardeerd wordt voor {Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.naam}."
        )
        return

    if ruimte.detail_soort in [
        Ruimtedetailsoort.parkeerterrein,
        Ruimtedetailsoort.parkeergarage,
    ]:
        logger.warning(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een {Ruimtedetailsoort.parkeerterrein.naam if ruimte.detail_soort==Ruimtedetailsoort.parkeerterrein else Ruimtedetailsoort.parkeergarage.naam} en kan momenteel niet gewaardeerd worden in de woningwaardering package. Voeg een parkeerplek los toe aan de eenheden om deze in aanmerking te laten komen voor een waardering onder {Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.naam}. Raadpleeg docs/implementatietoelichting-beleidsboeken/zelfstandige_woonruimten.md voor meer informatie."
        )
        return

    if ruimte.detail_soort not in [
        Ruimtedetailsoort.parkeervak_auto_binnen,  # Type I
        Ruimtedetailsoort.carport,  # Type II
        Ruimtedetailsoort.parkeervak_auto_buiten_niet_overdekt,  # Type III
    ]:
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
            ),
            aantal=ruimte.aantal,
            punten=utils.rond_af(totaal_punten_type_parkeeruimte, decimalen=2),
        )
    return
