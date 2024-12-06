from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Defectstatus(Referentiedatasoort):
    geinspecteerd = Referentiedata(
        code="INS",
        naam="Geinspecteerd",
    )

    gemeld = Referentiedata(
        code="MEL",
        naam="Gemeld",
    )
