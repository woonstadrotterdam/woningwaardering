
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class INKOMENSBRON:

    anders = Referentiedata(
        code="AND",
        naam="Anders",
    )
    # anders = ("AND", "Anders")

    arbeid = Referentiedata(
        code="ARB",
        naam="Arbeid",
    )
    # arbeid = ("ARB", "Arbeid")

    sociale_uitkering = Referentiedata(
        code="SOC",
        naam="Sociale uitkering",
    )
    # sociale_uitkering = ("SOC", "Sociale uitkering")

    studiefinanciering = Referentiedata(
        code="STU",
        naam="Studiefinanciering",
    )
    # studiefinanciering = ("STU", "Studiefinanciering")
