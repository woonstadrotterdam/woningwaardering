from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Machtigingsoort(Referentiedatasoort):
    doorlopend = Referentiedata(
        code="DOO",
        naam="Doorlopend",
    )

    eenmalig = Referentiedata(
        code="EEN",
        naam="Eenmalig",
    )
