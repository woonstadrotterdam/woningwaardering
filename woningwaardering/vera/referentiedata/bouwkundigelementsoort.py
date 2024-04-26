from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Bouwkundigelementsoort(Enum):
    overig = Referentiedata(
        code="OVE",
        naam="Overig",
    )

    verwarming = Referentiedata(
        code="VER",
        naam="Verwarming",
    )

    voorziening = Referentiedata(
        code="VOO",
        naam="Voorziening",
    )

    warmwater = Referentiedata(
        code="WAT",
        naam="Warmwater",
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
