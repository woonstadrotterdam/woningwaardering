from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Rentesoort(Enum):
    variabel = Referentiedata(
        code="VAR",
        naam="Variabel",
    )

    vast = Referentiedata(
        code="VST",
        naam="Vast",
    )

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
