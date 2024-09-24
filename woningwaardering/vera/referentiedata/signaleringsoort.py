from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Signaleringsoort(Enum):
    agressie = Referentiedata(
        code="AGR",
        naam="Agressie",
    )

    oneigenlijk_gebruik_woning = Referentiedata(
        code="ONE",
        naam="Oneigenlijk gebruik woning",
    )

    overlast = Referentiedata(
        code="OVE",
        naam="Overlast",
    )

    huurschuld = Referentiedata(
        code="SCH",
        naam="Huurschuld",
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
