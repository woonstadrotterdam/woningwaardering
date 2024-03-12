
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class INSPECTIERAPPORTSTATUS:

    concept = Referentiedata(
        code="CON",
        naam="Concept",
    )
    # concept = ("CON", "Concept")

    definitief = Referentiedata(
        code="DEF",
        naam="Definitief",
    )
    # definitief = ("DEF", "Definitief")

    getekend = Referentiedata(
        code="GET",
        naam="Getekend",
    )
    # getekend = ("GET", "Getekend")

    ter_review = Referentiedata(
        code="REV",
        naam="Ter review",
    )
    # ter_review = ("REV", "Ter review")

    vervallen = Referentiedata(
        code="VAL",
        naam="Vervallen",
    )
    # vervallen = ("VAL", "Vervallen")
