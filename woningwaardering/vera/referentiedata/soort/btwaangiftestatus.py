from vera.referentiedata.models import Referentiedata


class Btwaangiftestatus:
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
