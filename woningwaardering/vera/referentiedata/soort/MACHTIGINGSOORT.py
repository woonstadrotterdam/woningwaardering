
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class MACHTIGINGSOORT:

    doorlopend = Referentiedata(
        code="DOO",
        naam="Doorlopend",
    )
    # doorlopend = ("DOO", "Doorlopend")

    eenmalig = Referentiedata(
        code="EEN",
        naam="Eenmalig",
    )
    # eenmalig = ("EEN", "Eenmalig")
