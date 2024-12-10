from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class CommunicatierichtingReferentiedata(Referentiedata):
    pass


class Communicatierichting(Referentiedatasoort):
    inkomend = CommunicatierichtingReferentiedata(
        code="INK",
        naam="Inkomend",
    )

    uitgaand = CommunicatierichtingReferentiedata(
        code="UIT",
        naam="Uitgaand",
    )
