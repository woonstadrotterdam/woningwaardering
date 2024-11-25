import warnings
from decimal import Decimal
from typing import Generator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.vera.bvg.generated import (
    EenhedenRuimte,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.referentiedata.bouwkundigelementdetailsoort import (
    Bouwkundigelementdetailsoort,
)
from woningwaardering.vera.referentiedata.ruimtedetailsoort import Ruimtedetailsoort
from woningwaardering.vera.utils import heeft_bouwkundig_element

parkeertype_punten_mapping = {
    Ruimtedetailsoort.parkeervak_auto_binnen.code: {"Type I": Decimal("9.0")},
    Ruimtedetailsoort.carport.code: {"Type II": Decimal("6.0")},
    Ruimtedetailsoort.parkeervak_auto_buiten_niet_overdekt.code: {
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
    if ruimte.detail_soort.code is None:
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen 'code' in detailsoort"
        )
        return

    if ruimte.detail_soort.code in [
        Ruimtedetailsoort.parkeervak_motorfiets_binnen.code,
        Ruimtedetailsoort.parkeervak_scootmobiel_binnen.code,
        Ruimtedetailsoort.stalling_extern.code,
        Ruimtedetailsoort.stalling_intern.code,
        Ruimtedetailsoort.parkeervak_motorfiets_buiten_niet_overdekt.code,
        Ruimtedetailsoort.parkeervak_scootmobiel_buiten.code,
    ]:
        logger.debug(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) met ruimtedetailsoort {ruimte.detail_soort.code} is een parkeerplek die niet gewaardeerd wordt voor {Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.naam}."
        )
        return

    if ruimte.detail_soort.code in [
        Ruimtedetailsoort.parkeerterrein.code,
        Ruimtedetailsoort.parkeergarage.code,
    ]:
        logger.warning(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een {Ruimtedetailsoort.parkeerterrein.naam if ruimte.detail_soort.code==Ruimtedetailsoort.parkeerterrein.code else Ruimtedetailsoort.parkeergarage.naam} en kan momenteel niet gewaardeerd worden in de woningwaardering package. Voeg een parkeerplek los toe aan de eenheden om deze in aanmerking te laten komen voor een waardering onder {Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.naam}. Raadpleeg docs/implementatietoelichting-beleidsboeken/zelfstandige_woonruimten.md voor meer informatie."
        )
        return

    if ruimte.detail_soort.code not in [
        Ruimtedetailsoort.parkeervak_auto_binnen.code,
        Ruimtedetailsoort.carport.code,
        Ruimtedetailsoort.parkeervak_auto_buiten_niet_overdekt.code,
    ]:
        logger.debug(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) telt niet mee voor {Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.naam}."
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
    ) in parkeertype_punten_mapping[ruimte.detail_soort.code].items():
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
