from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class RentesoortReferentiedata(Referentiedata):
    pass


class Rentesoort(Referentiedatasoort):
    variabel = RentesoortReferentiedata(
        code="VAR",
        naam="Variabel",
    )

    vast = RentesoortReferentiedata(
        code="VST",
        naam="Vast",
    )
