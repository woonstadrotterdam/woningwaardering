from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Boekjaarstatus(Enum):
    gesloten = Referentiedata(
        code="GES",
        naam="Gesloten",
    )

    huidig = Referentiedata(
        code="HUD",
        naam="Huidig",
    )

    open = Referentiedata(
        code="OPN",
        naam="Open",
    )

    vorig = Referentiedata(
        code="VRG",
        naam="Vorig",
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
