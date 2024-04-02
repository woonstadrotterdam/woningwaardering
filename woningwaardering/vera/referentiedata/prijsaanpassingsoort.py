from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Prijsaanpassingsoort(Enum):
    korting = Referentiedata(
        code="KOR",
        naam="Korting",
    )

    toeslag = Referentiedata(
        code="TOE",
        naam="Toeslag",
    )

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
