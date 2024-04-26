from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Aktesoort(Enum):
    notariele_akte = Referentiedata(
        code="NOT",
        naam="Notariële akte",
    )
    """
    Akte vastgelegd bij de notaris.
    """

    onderhandse_akte = Referentiedata(
        code="OND",
        naam="Onderhandse akte",
    )
    """
    Akte die door twee of meer partijen is vastgesteld (onderhands)
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
