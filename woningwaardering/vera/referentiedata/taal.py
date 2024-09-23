from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Taal(Enum):
    duits = Referentiedata(
        code="DUI",
        naam="Duits",
    )

    engels = Referentiedata(
        code="ENG",
        naam="Engels",
    )

    frans = Referentiedata(
        code="FRA",
        naam="Frans",
    )

    nederlands = Referentiedata(
        code="NLD",
        naam="Nederlands",
    )

    spaans = Referentiedata(
        code="SPA",
        naam="Spaans",
    )

    turks = Referentiedata(
        code="TUR",
        naam="Turks",
    )

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
