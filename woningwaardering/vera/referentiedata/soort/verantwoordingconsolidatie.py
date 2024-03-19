from vera.referentiedata.models import Referentiedata


class Verantwoordingconsolidatie:
    geconsolideerd = Referentiedata(
        code="CON",
        naam="Geconsolideerd",
    )
    """
    Financiële verantwoording vindt plaats voor meerdere financieel bedrijven
    geconsolideerd
    """

    enkelvoudig = Referentiedata(
        code="ENK",
        naam="Enkelvoudig",
    )
    """
    Financiële verantwoording vindt plaats per financieel bedrijf afzonderlijk
    """
