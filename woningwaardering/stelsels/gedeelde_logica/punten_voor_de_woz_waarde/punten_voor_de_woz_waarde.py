from datetime import date

from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenWozEenheid,
)


def woz_waardepeildatums(peildatum: date) -> tuple[date, date]:
    return (
        date(peildatum.year - 1, 1, 1),
        date(peildatum.year - 2, 1, 1),
    )


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
    return max(
        woz_eenheden,
        key=lambda woz_eenheid: woz_eenheid.waardepeildatum or date.min,
    )
