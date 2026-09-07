from datetime import date
from typing import cast

from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenWozEenheid,
)

DATUM_FORMAT = "%d-%m-%Y"


def woz_waardepeildatums(peildatum: date) -> tuple[date, date]:
    return (
        date(peildatum.year - 1, 1, 1),
        date(peildatum.year - 2, 1, 1),
    )


def ontbrekende_relevante_woz_toelichting(
    eenheid: EenhedenEenheid,
    peildatum: date,
) -> str:
    if eenheid.woz_eenheden:
        datums = " of ".join(
            waardepeildatum.strftime(DATUM_FORMAT)
            for waardepeildatum in woz_waardepeildatums(peildatum)
        )
        return f"geen WOZ-waarde gevonden met waardepeildatum {datums}"
    return "geen WOZ-waarde aangeleverd"


def waardepeildatum_van_woz_eenheid(woz_eenheid: EenhedenWozEenheid) -> date:
    # Na het filter in meest_recente_relevante_woz_eenheid, of bij de
    # geconstrueerde minimum WOZ-waarde, is waardepeildatum altijd gezet.
    return cast(date, woz_eenheid.waardepeildatum)


def meest_recente_relevante_woz_eenheid(
    eenheid: EenhedenEenheid,
    peildatum: date,
) -> EenhedenWozEenheid | None:
    """Selecteer de meest recente bruikbare WOZ-beschikking voor de peildatum."""
    waardepeildatums = woz_waardepeildatums(peildatum)
    woz_eenheden: list[EenhedenWozEenheid] = [
        woz_eenheid
        for woz_eenheid in eenheid.woz_eenheden or []
        if woz_eenheid is not None
        and woz_eenheid.waardepeildatum in waardepeildatums
        and woz_eenheid.vastgestelde_waarde not in (None, 0)
    ]
    if not woz_eenheden:
        return None
    return max(woz_eenheden, key=waardepeildatum_van_woz_eenheid)
