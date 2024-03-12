
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class ENERGIELABEL:

    a = Referentiedata(
        code="A",
        naam="A",
    )
    # a = ("A", "A")

    ap = Referentiedata(
        code="AP",
        naam="A+",
    )
    # ap = ("AP", "A+")

    ap3 = Referentiedata(
        code="AP3",
        naam="A+++",
    )
    # ap3 = ("AP3", "A+++")

    ap4 = Referentiedata(
        code="AP4",
        naam="A++++",
    )
    # ap4 = ("AP4", "A++++")

    app = Referentiedata(
        code="APP",
        naam="A++",
    )
    # app = ("APP", "A++")

    b = Referentiedata(
        code="B",
        naam="B",
    )
    # b = ("B", "B")

    c = Referentiedata(
        code="C",
        naam="C",
    )
    # c = ("C", "C")

    d = Referentiedata(
        code="D",
        naam="D",
    )
    # d = ("D", "D")

    e = Referentiedata(
        code="E",
        naam="E",
    )
    # e = ("E", "E")

    f = Referentiedata(
        code="F",
        naam="F",
    )
    # f = ("F", "F")

    g = Referentiedata(
        code="G",
        naam="G",
    )
    # g = ("G", "G")
