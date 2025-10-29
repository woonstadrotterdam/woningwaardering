from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EnergielabelReferentiedata(Referentiedata):
    pass


class Energielabel(Referentiedatasoort):
    a = EnergielabelReferentiedata(
        code="A",
        naam="A",
    )

    ap = EnergielabelReferentiedata(
        code="AP",
        naam="A+",
    )

    ap3 = EnergielabelReferentiedata(
        code="AP3",
        naam="A+++",
    )

    ap4 = EnergielabelReferentiedata(
        code="AP4",
        naam="A++++",
    )

    app = EnergielabelReferentiedata(
        code="APP",
        naam="A++",
    )

    b = EnergielabelReferentiedata(
        code="B",
        naam="B",
    )

    c = EnergielabelReferentiedata(
        code="C",
        naam="C",
    )

    d = EnergielabelReferentiedata(
        code="D",
        naam="D",
    )

    e = EnergielabelReferentiedata(
        code="E",
        naam="E",
    )

    f = EnergielabelReferentiedata(
        code="F",
        naam="F",
    )

    g = EnergielabelReferentiedata(
        code="G",
        naam="G",
    )
