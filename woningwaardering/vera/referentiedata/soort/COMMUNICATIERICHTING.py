
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class COMMUNICATIERICHTING:

    inkomend = Referentiedata(
        code="INK",
        naam="Inkomend",
    )
    # inkomend = ("INK", "Inkomend")

    uitgaand = Referentiedata(
        code="UIT",
        naam="Uitgaand",
    )
    # uitgaand = ("UIT", "Uitgaand")
