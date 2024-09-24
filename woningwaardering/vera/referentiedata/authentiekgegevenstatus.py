from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Authentiekgegevenstatus(Enum):
    gevalideerd = Referentiedata(
        code="GEV",
        naam="Gevalideerd",
    )
    """
    Gegevens zijn gevalideerd door de bron.
    """

    vervallen = Referentiedata(
        code="VER",
        naam="Vervallen",
    )
    """
    Gegevens zijn vervallen doordat deze zijn verlopen.
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
