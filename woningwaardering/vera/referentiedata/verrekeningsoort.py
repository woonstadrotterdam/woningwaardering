from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Verrekeningsoort(Enum):
    te_activeren = Referentiedata(
        code="ACT",
        naam="Te activeren",
    )
    """
    Bij de verrekening wordt (een deel van) het bedrag geactiveerd
    """

    te_verhalen = Referentiedata(
        code="VER",
        naam="Te verhalen",
    )
    """
    Bij de verrekening wordt (een deel van) het bedrag verhaald op een derde partij
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
