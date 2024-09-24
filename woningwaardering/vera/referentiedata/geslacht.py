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

    onbekend = Referentiedata(
        code="O",
        naam="Onbekend",
    )
    """
    Manier om genderneutraal aan te duiden of wanneer geslacht niet ter zake doet.
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
