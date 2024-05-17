from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Geslacht(Enum):
    mannelijk = Referentiedata(
        code="M",
        naam="Mannelijk",
    )
    """
    Mannelijk geslacht
    """

    genderneutraal = Referentiedata(
        code="X",
        naam="Genderneutraal",
    )
    """
    X is de term die zowel door de Nederlandse overheid als officieel door veel andere
    landen wordt gebruikt om gender-neutraal te duiden.
    """

    vrouwelijk = Referentiedata(
        code="V",
        naam="Vrouwelijk",
    )
    """
    Vrouwelijk geslacht
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
