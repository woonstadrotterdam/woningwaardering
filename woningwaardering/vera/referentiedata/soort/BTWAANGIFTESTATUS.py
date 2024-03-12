
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class BTWAANGIFTESTATUS:

    definitief = Referentiedata(
        code="DEF",
        naam="Definitief",
    )
    # definitief = ("DEF", "Definitief")

    in_behandeling = Referentiedata(
        code="IBH",
        naam="In behandeling",
    )
    # in_behandeling = ("IBH", "In behandeling")

    voorlopig = Referentiedata(
        code="VRL",
        naam="Voorlopig",
    )
    # voorlopig = ("VRL", "Voorlopig")
