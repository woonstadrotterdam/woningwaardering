from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Eenheidklimaatbeheersingsoort(Enum):
    individueel = Referentiedata(
        code="IND",
        naam="Individueel",
    )

    collectief = Referentiedata(
        code="COL",
        naam="Collectief",
    )

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
