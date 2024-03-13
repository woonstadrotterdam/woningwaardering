from woningwaardering.vera.bvg.models import Referentiedata


class BTWAANGIFTESTATUS:
    definitief = Referentiedata(
        code="DEF",
        naam="Definitief",
    )

    in_behandeling = Referentiedata(
        code="IBH",
        naam="In behandeling",
    )

    voorlopig = Referentiedata(
        code="VRL",
        naam="Voorlopig",
    )
