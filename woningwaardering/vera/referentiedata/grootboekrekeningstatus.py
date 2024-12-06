from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Grootboekrekeningstatus(Referentiedatasoort):
    actief = Referentiedata(
        code="ACT",
        naam="Actief",
    )

    geblokkeerd = Referentiedata(
        code="BLK",
        naam="Geblokkeerd",
    )

    historisch = Referentiedata(
        code="HIS",
        naam="Historisch",
    )
