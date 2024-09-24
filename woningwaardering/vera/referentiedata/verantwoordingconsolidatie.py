from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Verantwoordingconsolidatie(Enum):
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

    @property
    def code(self) -> str:
        if self.value.code is None:
            raise TypeError("de code van een Referentiedata object mag niet None zijn")
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
