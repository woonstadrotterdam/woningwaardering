from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Btwaangiftestatus(Enum):
    definitief = Referentiedata(
        code="DEF",
        naam="Definitief",
    )

    in_behandeling = Referentiedata(
        code="IBH",
        naam="In behandeling",
    )

    voorlopig = Referentiedata(
        code="VRL",
        naam="Voorlopig",
    )

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
