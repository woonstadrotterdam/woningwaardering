
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class KWALITEITSNIVEAU:

    eenvoudig = Referentiedata(
        code="EEN",
        naam="Eenvoudig",
    )
    # eenvoudig = ("EEN", "Eenvoudig")

    hoogwaardig = Referentiedata(
        code="HOO",
        naam="Hoogwaardig",
    )
    # hoogwaardig = ("HOO", "Hoogwaardig")

    luxe = Referentiedata(
        code="LUX",
        naam="Luxe",
    )
    # luxe = ("LUX", "Luxe")

    standaard = Referentiedata(
        code="STA",
        naam="Standaard",
    )
    # standaard = ("STA", "Standaard")
