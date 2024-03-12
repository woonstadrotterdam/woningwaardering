
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class RUIMTELIGGING:

    noord = Referentiedata(
        code="NOO",
        naam="Noord",
    )
    # noord = ("NOO", "Noord")

    noordoost = Referentiedata(
        code="NOS",
        naam="Noordoost",
    )
    # noordoost = ("NOS", "Noordoost")

    noordwest = Referentiedata(
        code="NWE",
        naam="Noordwest",
    )
    # noordwest = ("NWE", "Noordwest")

    oost = Referentiedata(
        code="OOS",
        naam="Oost",
    )
    # oost = ("OOS", "Oost")

    west = Referentiedata(
        code="WES",
        naam="West",
    )
    # west = ("WES", "West")

    zuidoost = Referentiedata(
        code="ZOO",
        naam="Zuidoost",
    )
    # zuidoost = ("ZOO", "Zuidoost")

    zuid = Referentiedata(
        code="ZUI",
        naam="Zuid",
    )
    # zuid = ("ZUI", "Zuid")

    zuidwest = Referentiedata(
        code="ZWE",
        naam="Zuidwest",
    )
    # zuidwest = ("ZWE", "Zuidwest")
