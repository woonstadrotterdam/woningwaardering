from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Externeincassosoort(Enum):
    deurwaarder = Referentiedata(
        code="DEU",
        naam="Deurwaarder",
    )

    incassobureau = Referentiedata(
        code="INC",
        naam="Incassobureau",
    )

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
