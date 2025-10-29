from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BtwaangiftestatusReferentiedata(Referentiedata):
    pass


class Btwaangiftestatus(Referentiedatasoort):
    definitief = BtwaangiftestatusReferentiedata(
        code="DEF",
        naam="Definitief",
    )

    in_behandeling = BtwaangiftestatusReferentiedata(
        code="IBH",
        naam="In behandeling",
    )

    voorlopig = BtwaangiftestatusReferentiedata(
        code="VRL",
        naam="Voorlopig",
    )
