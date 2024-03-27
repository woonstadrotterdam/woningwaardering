from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Relatiedetailsoort(Enum):
    huishouden = Referentiedata(
        code="HUI",
        naam="Huishouden",
    )
    """
    Een huishouden bestaat uit één of meer personen die op hetzelfde adres wonen en een
    economisch-consumptieve eenheid vormen. (CORA)
    """

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
