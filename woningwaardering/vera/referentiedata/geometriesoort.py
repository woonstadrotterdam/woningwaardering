from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Geometriesoort(Enum):
    omtrek = Referentiedata(
        code="OMT",
        naam="Omtrek",
    )
    """
    De geocoördinaten van de omtrek van een object
    """

    punt = Referentiedata(
        code="PUN",
        naam="Punt",
    )
    """
    De geocoördinaten van het middenpunt van een object
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
