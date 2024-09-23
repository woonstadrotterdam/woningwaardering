from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Inkomensbron(Enum):
    anders = Referentiedata(
        code="AND",
        naam="Anders",
    )

    arbeid = Referentiedata(
        code="ARB",
        naam="Arbeid",
    )

    sociale_uitkering = Referentiedata(
        code="SOC",
        naam="Sociale uitkering",
    )

    studiefinanciering = Referentiedata(
        code="STU",
        naam="Studiefinanciering",
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
