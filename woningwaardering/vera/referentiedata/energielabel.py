from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Energielabel(Enum):
    a = Referentiedata(
        code="A",
        naam="A",
    )

    ap = Referentiedata(
        code="AP",
        naam="A+",
    )

    ap3 = Referentiedata(
        code="AP3",
        naam="A+++",
    )

    ap4 = Referentiedata(
        code="AP4",
        naam="A++++",
    )

    app = Referentiedata(
        code="APP",
        naam="A++",
    )

    b = Referentiedata(
        code="B",
        naam="B",
    )

    c = Referentiedata(
        code="C",
        naam="C",
    )

    d = Referentiedata(
        code="D",
        naam="D",
    )

    e = Referentiedata(
        code="E",
        naam="E",
    )

    f = Referentiedata(
        code="F",
        naam="F",
    )

    g = Referentiedata(
        code="G",
        naam="G",
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
