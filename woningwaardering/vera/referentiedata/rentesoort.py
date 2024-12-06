from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Rentesoort(Referentiedatasoort):
    variabel = Referentiedata(
        code="VAR",
        naam="Variabel",
    )

    vast = Referentiedata(
        code="VST",
        naam="Vast",
    )
