from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Relatiedetailsoort(Enum):
    huishouden = Referentiedata(
        code="HUI",
        naam="Huishouden",
        parent=Referentiedata(
            code="GRO",
            naam="Relatiegroep",
        ),
    )
    """
    Een huishouden bestaat uit één of meer personen die op hetzelfde adres wonen en een
    economisch-consumptieve eenheid vormen. (CORA)
    """

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
