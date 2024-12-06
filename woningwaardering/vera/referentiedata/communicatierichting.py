from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Communicatierichting(Referentiedatasoort):
    inkomend = Referentiedata(
        code="INK",
        naam="Inkomend",
    )

    uitgaand = Referentiedata(
        code="UIT",
        naam="Uitgaand",
    )
