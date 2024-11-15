from loguru import logger

from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata.eenheidmonument import Eenheidmonument
from woningwaardering.vera.referentiedata.woningwaarderingstelselgroep import (
    Woningwaarderingstelselgroep,
)


def monument_correctie(
    eenheid: EenhedenEenheid,
    woningwaardering: WoningwaarderingResultatenWoningwaardering,
) -> WoningwaarderingResultatenWoningwaardering | None:
    """
    Berekent de correctie voor monumenten.
    Voor rijks-, provinciale en gemeentelijke monumenten geldt dat de waardering voor energieprestatie minimaal 0 punten is.

    Args:
        eenheid (EenhedenEenheid): Eenheid
        woningwaardering (WoningwaarderingResultatenWoningwaardering): De waardering voor Energieprestatie tot zover.

    Returns:
        WoningwaarderingResultatenWoningwaardering | None: De correctiewaardering indien van toepassing, anders None
    """

    if (
        eenheid.monumenten
        and any(
            monument.code
            in [
                Eenheidmonument.rijksmonument.code,
                Eenheidmonument.gemeentelijk_monument.code,
                Eenheidmonument.provinciaal_monument.code,
            ]
            for monument in eenheid.monumenten or []
        )
        and woningwaardering.punten
        and woningwaardering.punten < 0.0
    ):
        logger.info(
            f"Eenheid ({eenheid.id}) is een monument: waardering voor {Woningwaarderingstelselgroep.energieprestatie.naam} is minimaal 0 punten."
        )
        return WoningwaarderingResultatenWoningwaardering(
            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                naam="Correctie monument"
            ),
            punten=woningwaardering.punten * -1.0,
        )
    return None
