import warnings
from datetime import date

from loguru import logger

from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.referentiedata.eenheidmonument import Eenheidmonument


def opslag_rijksmonument(
    peildatum: date,
    eenheid: EenhedenEenheid,
    stelselgroep: Woningwaarderingstelselgroep = Woningwaarderingstelselgroep.prijsopslag_monumenten_en_nieuwbouw,
) -> WoningwaarderingResultatenWoningwaardering | None:
    if any(
        monument.code == Eenheidmonument.rijksmonument.code
        for monument in eenheid.monumenten or []
    ):
        datum_afsluiten_huurovereenkomst = eenheid.datum_afsluiten_huurovereenkomst
        if datum_afsluiten_huurovereenkomst is None:
            warnings.warn(
                f"Eenheid ({eenheid.id}): 'datum_afsluiten_huurovereenkomst' is niet gespecificeerd voor dit rijksmonument.",
                UserWarning,
            )
            logger.warning(
                f"Eenheid ({eenheid.id}): Voor de waardering van dit rijksmonument wordt de peildatum {peildatum} gebruikt in plaats van de datum van de afsluiting van de huurovereenkomst."
            )
            datum_afsluiten_huurovereenkomst = peildatum

        woningwaardering = WoningwaarderingResultatenWoningwaardering(
            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                naam="Rijksmonument",
            ),
        )

        if datum_afsluiten_huurovereenkomst >= date(2024, 7, 1):
            logger.info(
                f"Eenheid ({eenheid.id}) is een rijksmonument en krijgt een opslagpercentage van 35% op de maximale huurprijs voor {stelselgroep.naam}."
            )
            woningwaardering.opslagpercentage = 0.35
        elif (
            stelselgroep
            == Woningwaarderingstelselgroep.prijsopslag_monumenten_en_nieuwbouw
        ):
            # 50 punten voor zelfstandige woonruimten
            logger.info(
                f"Eenheid ({eenheid.id}) is een rijksmonument en krijgt 50 punten voor {stelselgroep.naam}."
            )
            woningwaardering.punten = 50.0
        elif stelselgroep == Woningwaarderingstelselgroep.prijsopslag_monumenten:
            # 10 punten voor onzelfstandige woonruimten
            logger.info(
                f"Eenheid ({eenheid.id}) is een rijksmonument en krijgt 10 punten voor {stelselgroep.naam}."
            )
            woningwaardering.punten = 10.0

        return woningwaardering
    return None
