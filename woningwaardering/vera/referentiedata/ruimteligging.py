from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Ruimteligging(Enum):
    noord = Referentiedata(
        code="NOO",
        naam="Noord",
    )

    noordoost = Referentiedata(
        code="NOS",
        naam="Noordoost",
    )

    noordwest = Referentiedata(
        code="NWE",
        naam="Noordwest",
    )

    oost = Referentiedata(
        code="OOS",
        naam="Oost",
    )

    west = Referentiedata(
        code="WES",
        naam="West",
    )

    zuidoost = Referentiedata(
        code="ZOO",
        naam="Zuidoost",
    )

    zuid = Referentiedata(
        code="ZUI",
        naam="Zuid",
    )

    zuidwest = Referentiedata(
        code="ZWE",
        naam="Zuidwest",
    )

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
