import warnings
from decimal import Decimal
from typing import Iterator

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


def waardeer(
    ruimte: EenhedenRuimte,
) -> Iterator[WoningwaarderingResultatenWoningwaardering] | None:
    if ruimte.detail_soort is None:
        warnings.warn(f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen detailsoort")
        return None
    if ruimte.detail_soort.code is None:
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen 'code' in detailsoort"
        )
        return None

    if ruimte.detail_soort.code in [
        Ruimtedetailsoort.parkeervak_motorfiets_binnen.code,
        Ruimtedetailsoort.parkeervak_scootmobiel_binnen.code,
        Ruimtedetailsoort.stalling_extern.code,
        Ruimtedetailsoort.stalling_intern.code,
        Ruimtedetailsoort.parkeervak_motorfiets_buiten_niet_overdekt.code,
        Ruimtedetailsoort.parkeervak_scootmobiel_buiten.code,
    ]:
        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) met ruimtedetailsoort {ruimte.detail_soort.code} is een parkeerplek die niet gewaardeerd wordt in het woningwaardering stelsel volgens het beleidsboek."
        )
        return None

    if ruimte.detail_soort.code in [
        Ruimtedetailsoort.parkeerterrein.code,
        Ruimtedetailsoort.parkeergarage.code,
    ]:
        logger.warning(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) is een {Ruimtedetailsoort.parkeerterrein.naam if ruimte.detail_soort.code==Ruimtedetailsoort.parkeerterrein.code else Ruimtedetailsoort.parkeergarage.naam} en kan momenteel niet gewaardeerd worden in de woningwaardering package. Voeg een parkeerplek los toe aan de eenheden om deze in aanmerking te laten komen voor een waardering onder {Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.naam}. Raadpleeg docs/implementatietoelichting-beleidsboeken/zelfstandige_woonruimten.md voor meer informatie."
        )
        return None

    if ruimte.detail_soort.code not in [
        Ruimtedetailsoort.parkeervak_auto_binnen.code,
        Ruimtedetailsoort.carport.code,
        Ruimtedetailsoort.parkeervak_auto_buiten_niet_overdekt.code,
    ]:
        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) is geen gemeenschappelijke parkeerruimte en wordt niet gewaardeerd onder rubriek {Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten.naam}."
        )
        return None

    if ruimte.oppervlakte is None:
        warnings.warn(f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen oppervlakte")
        return None

    if ruimte.gedeeld_met_aantal_eenheden is None:
        warnings.warn(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen 'gedeeld_met_aantal_eenheden'. Zet 'gedeeld_met_aantal_eenheden' >= 2 wanneer de ruimte gedeeld is. 'gedeeld_met_aantal_eenheden' op 0 of 1 wordt beschouwd als niet gedeeld."
        )
        return None

    if not ruimte.oppervlakte >= 12.0:
        logger.info(
            f"Ruimte '{ruimte.naam}' ({ruimte.id}) voldoet niet aan de eis van 12m2 voor een parkeervak."
        )
        return None

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
