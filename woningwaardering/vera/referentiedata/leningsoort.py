from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Leningsoort(Enum):
    kredietfaciliteit = Referentiedata(
        code="KRE",
        naam="Kredietfaciliteit",
    )

    lening = Referentiedata(
        code="LEN",
        naam="Lening",
    )

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
