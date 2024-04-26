from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Eenheidcriteriasoort(Enum):
    selectie = Referentiedata(
        code="SEL",
        naam="Selectie",
    )
    """
    Selectiecriteria die worden gebruikt om de passendheid van een woningzoekende voor
    de eenheid te bepalen.
    """

    sortering = Referentiedata(
        code="SOR",
        naam="Sortering",
    )
    """
    Sorteercriteria die worden gebruikt om de positie van een woningzoekende voor de
    eenheid te bepalen.
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
