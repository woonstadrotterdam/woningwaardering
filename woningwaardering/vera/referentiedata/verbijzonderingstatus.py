from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class VerbijzonderingstatusReferentiedata(Referentiedata):
    pass


class Verbijzonderingstatus(Referentiedatasoort):
    actief = VerbijzonderingstatusReferentiedata(
        code="ACT",
        naam="Actief",
    )

    geblokkeerd = VerbijzonderingstatusReferentiedata(
        code="BLK",
        naam="Geblokkeerd",
    )

    historisch = VerbijzonderingstatusReferentiedata(
        code="HIS",
        naam="Historisch",
    )
