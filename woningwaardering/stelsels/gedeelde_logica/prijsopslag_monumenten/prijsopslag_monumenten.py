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


def opslag_gemeentelijk_of_provinciaal_monument(
    eenheid: EenhedenEenheid,
    stelselgroep: Woningwaarderingstelselgroep = Woningwaarderingstelselgroep.prijsopslag_monumenten_en_nieuwbouw,
) -> WoningwaarderingResultatenWoningwaardering | None:
    if any(
        monument.code
        in [
            Eenheidmonument.gemeentelijk_monument.code,
            Eenheidmonument.provinciaal_monument.code,
        ]
        for monument in eenheid.monumenten or []
    ):
        logger.info(
            f"Eenheid ({eenheid.id}) is gemeentelijk of provinciaal monument en wordt gewaardeerd met een opslagpercentage van 15% op de maximale huurprijs voor de stelselgroep {stelselgroep.naam}."
        )
        return WoningwaarderingResultatenWoningwaardering(
            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                naam="Gemeentelijk of provinciaal monument",
            ),
            opslagpercentage=0.15,
        )
    return None


def opslag_beschermd_stads_of_dorpsgezicht(
    eenheid: EenhedenEenheid,
    stelselgroep: Woningwaarderingstelselgroep = Woningwaarderingstelselgroep.prijsopslag_monumenten_en_nieuwbouw,
) -> WoningwaarderingResultatenWoningwaardering | None:
    if any(
        monument.code
        in [
            Eenheidmonument.beschermd_dorpsgezicht.code,
            Eenheidmonument.beschermd_stadsgezicht.code,
        ]
        for monument in eenheid.monumenten or []
    ) and not any(
        monument.code
        in [
            Eenheidmonument.rijksmonument.code,
            Eenheidmonument.gemeentelijk_monument.code,
            Eenheidmonument.provinciaal_monument.code,
        ]
        for monument in eenheid.monumenten or []
    ):
        if eenheid.bouwjaar is None:
            warnings.warn(
                f"Eenheid ({eenheid.id}): geen bouwjaar gevonden",
                UserWarning,
            )
        elif eenheid.bouwjaar < 1965:
            logger.info(
                f"Eenheid ({eenheid.id}) behoort tot een beschermd stads- of dorpsgezicht en wordt gewaardeerd met een opslagpercentage van 5% op de maximale huurprijs voor de stelselgroep {stelselgroep.naam}."
            )
            return WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam="Beschermd stads- of dorpsgezicht",
                ),
                opslagpercentage=0.05,
            )

        else:
            logger.info(
                f"Eenheid ({eenheid.id}) behoort tot een beschermd stads- of dorpsgezicht, maar is niet gebouwd voor 1965. Er wordt geen opslagpercentage toegepast."
            )
    return None
