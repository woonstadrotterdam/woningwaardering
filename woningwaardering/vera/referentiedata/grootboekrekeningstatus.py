from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class GrootboekrekeningstatusReferentiedata(Referentiedata):
    pass


class Grootboekrekeningstatus(Referentiedatasoort):
    actief = GrootboekrekeningstatusReferentiedata(
        code="ACT",
        naam="Actief",
    )

    geblokkeerd = GrootboekrekeningstatusReferentiedata(
        code="BLK",
        naam="Geblokkeerd",
    )

    historisch = GrootboekrekeningstatusReferentiedata(
        code="HIS",
        naam="Historisch",
    )
