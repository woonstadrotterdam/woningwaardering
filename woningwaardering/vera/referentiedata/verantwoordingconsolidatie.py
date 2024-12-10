from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class VerantwoordingconsolidatieReferentiedata(Referentiedata):
    pass


class Verantwoordingconsolidatie(Referentiedatasoort):
    geconsolideerd = VerantwoordingconsolidatieReferentiedata(
        code="CON",
        naam="Geconsolideerd",
    )
    """
    Financiële verantwoording vindt plaats voor meerdere financieel bedrijven
    geconsolideerd
    """

    enkelvoudig = VerantwoordingconsolidatieReferentiedata(
        code="ENK",
        naam="Enkelvoudig",
    )
    """
    Financiële verantwoording vindt plaats per financieel bedrijf afzonderlijk
    """
