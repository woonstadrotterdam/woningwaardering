from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class MachtigingsoortReferentiedata(Referentiedata):
    pass


class Machtigingsoort(Referentiedatasoort):
    doorlopend = MachtigingsoortReferentiedata(
        code="DOO",
        naam="Doorlopend",
    )

    eenmalig = MachtigingsoortReferentiedata(
        code="EEN",
        naam="Eenmalig",
    )
