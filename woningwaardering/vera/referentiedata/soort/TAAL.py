
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class TAAL:

    duits = Referentiedata(
        code="DUI",
        naam="Duits",
    )
    # duits = ("DUI", "Duits")

    engels = Referentiedata(
        code="ENG",
        naam="Engels",
    )
    # engels = ("ENG", "Engels")

    frans = Referentiedata(
        code="FRA",
        naam="Frans",
    )
    # frans = ("FRA", "Frans")

    nederlands = Referentiedata(
        code="NLD",
        naam="Nederlands",
    )
    # nederlands = ("NLD", "Nederlands")

    spaans = Referentiedata(
        code="SPA",
        naam="Spaans",
    )
    # spaans = ("SPA", "Spaans")

    turks = Referentiedata(
        code="TUR",
        naam="Turks",
    )
    # turks = ("TUR", "Turks")
