from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Aanbiedingstatus(Enum):
    aangeboden = Referentiedata(
        code="AAN",
        naam="Aangeboden",
    )
    """
    Er is aanbieding gedaan aan een of meer kandidaten.
    """

    geweigerd = Referentiedata(
        code="GEW",
        naam="Geweigerd",
    )
    """
    Een kandidaat heeft een verstrekte aanbieding afgewezen.
    """

    ingetrokken = Referentiedata(
        code="ING",
        naam="Ingetrokken",
    )
    """
    Een aan een kandidaat verstrekte aanbieding is ingetrokken.
    """

    toegewezen = Referentiedata(
        code="TOE",
        naam="Toegewezen",
    )
    """
    Een eenheid is toegewezen aan een kandidaat.
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
