from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Contactgegevenvoorkeur(Enum):
    eerste = Referentiedata(
        code="EER",
        naam="Eerste",
    )

    tweede = Referentiedata(
        code="TWE",
        naam="Tweede",
    )

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
