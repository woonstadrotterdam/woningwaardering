from datetime import date

from loguru import logger

from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenPrijscomponent,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata import (
    Eenheidmonument,
    Prijscomponentdetailsoort,
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
            monument
            in [
                Eenheidmonument.rijksmonument,
                Eenheidmonument.gemeentelijk_monument,
                Eenheidmonument.provinciaal_monument,
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


def get_energieprestatievergoeding(
    peildatum: date,
    eenheid: EenhedenEenheid,
) -> EenhedenPrijscomponent | None:
    """
    Geeft de eerst gevonden geldige energieprestatievergoeding voor de eenheid.

    Args:
        peildatum (date): Peildatum
        eenheid (EenhedenEenheid): Eenheid

    Returns:
        EenhedenPrijscomponent | None: Energieprestatievergoeding of None indien niet gevonden.
    """
    return next(
        (
            prijscomponent
            for prijscomponent in eenheid.prijscomponenten or []
            if prijscomponent.detail_soort
            == Prijscomponentdetailsoort.energieprestatievergoeding
            and (
                prijscomponent.begindatum is None
                or prijscomponent.begindatum <= peildatum
            )
            and (
                prijscomponent.einddatum is None or prijscomponent.einddatum > peildatum
            )
        ),
        None,
    )
