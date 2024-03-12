
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class VERANTWOORDINGCONSOLIDATIE:

    geconsolideerd = Referentiedata(
        code="CON",
        naam="Geconsolideerd",
    )
    # geconsolideerd = ("CON", "Geconsolideerd")
    """
    Financiële verantwoording vindt plaats voor meerdere financieel bedrijven
    geconsolideerd
    """

    enkelvoudig = Referentiedata(
        code="ENK",
        naam="Enkelvoudig",
    )
    # enkelvoudig = ("ENK", "Enkelvoudig")
    """
    Financiële verantwoording vindt plaats per financieel bedrijf afzonderlijk
    """
