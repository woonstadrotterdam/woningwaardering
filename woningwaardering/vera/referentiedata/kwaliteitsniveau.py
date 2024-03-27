from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Kwaliteitsniveau(Enum):
    eenvoudig = Referentiedata(
        code="EEN",
        naam="Eenvoudig",
    )

    hoogwaardig = Referentiedata(
        code="HOO",
        naam="Hoogwaardig",
    )

    luxe = Referentiedata(
        code="LUX",
        naam="Luxe",
    )

    standaard = Referentiedata(
        code="STA",
        naam="Standaard",
    )

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
