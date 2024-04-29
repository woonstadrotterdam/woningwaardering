from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Dagdeel(Enum):
    avond = Referentiedata(
        code="AVO",
        naam="Avond",
    )
    """
    Tussen 18 en 24 uur.
    """

    middag = Referentiedata(
        code="MID",
        naam="Middag",
    )
    """
    Tussen 12 en 18 uur.
    """

    ochtend = Referentiedata(
        code="OCH",
        naam="Ochtend",
    )
    """
    Tussen 8 en 12 uur.
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
