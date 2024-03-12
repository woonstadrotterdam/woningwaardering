
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class EENHEIDKLIMAATBEHEERSINGSOORT:

    individueel = Referentiedata(
        code="IND",
        naam="Individueel",
    )
    # individueel = ("IND", "Individueel")

    collectief = Referentiedata(
        code="COL",
        naam="Collectief",
    )
    # collectief = ("COL", "Collectief")
