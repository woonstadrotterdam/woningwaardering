from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Btwaangiftestatus(Referentiedatasoort):
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
