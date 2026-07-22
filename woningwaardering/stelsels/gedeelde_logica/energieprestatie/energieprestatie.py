from datetime import date
from decimal import Decimal

from loguru import logger

from woningwaardering.stelsels.builders import (
    WaarderingBuilder,
    WaarderingsgroepBuilder,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenPrijscomponent,
)
from woningwaardering.vera.referentiedata import (
    Eenheidmonument,
    Prijscomponentdetailsoort,
    Woningwaarderingstelselgroep,
)


def monument_correctie(
    eenheid: EenhedenEenheid,
    woningwaardering: WaarderingBuilder,
    *,
    waarderingsgroep_builder: WaarderingsgroepBuilder | WaarderingBuilder,
) -> WaarderingBuilder | None:
    """
    Berekent de correctie voor monumenten.
    Voor rijks-, provinciale en gemeentelijke monumenten geldt dat de waardering voor energieprestatie minimaal 0 punten is.

    Args:
        eenheid (EenhedenEenheid): Eenheid
        woningwaardering (WaarderingBuilder): De waardering voor Energieprestatie tot zover.
        waarderingsgroep_builder (WaarderingsgroepBuilder | WaarderingBuilder): waarderingsgroep of bestaande waardering in de hiërarchie.

    Returns:
        WaarderingBuilder | None: De correctiewaardering indien van toepassing, anders None
    """

    is_rijks_provinciaal_of_gemeentelijk_monument = eenheid.monumenten and any(
        monument
        in [
            Eenheidmonument.rijksmonument,
            Eenheidmonument.gemeentelijk_monument,
            Eenheidmonument.provinciaal_monument,
        ]
        for monument in eenheid.monumenten or []
    )
    if not is_rijks_provinciaal_of_gemeentelijk_monument:
        return None

    punten = woningwaardering.punten
    minimum_punten = Decimal("0.0")

    if punten is None or punten >= minimum_punten:
        return None

    correctie_punten = minimum_punten - Decimal(str(punten))

    logger.info(
        f"Eenheid ({eenheid.id}) is een monument: waardering voor {Woningwaarderingstelselgroep.energieprestatie.naam} is minimaal {minimum_punten} punten."
    )
    return waarderingsgroep_builder.maak_onderliggende(
        id="correctie_monument",
        naam="Correctie monument",
        punten=correctie_punten,
    )


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
