
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class OVEREENKOMSTKOPPELINGSTATUS:

    aangevraagd = Referentiedata(
        code="AAN",
        naam="Aangevraagd",
    )
    # aangevraagd = ("AAN", "Aangevraagd")
    """
    Het koppelen van de overeenkomsten is aangevraagd
    """

    afgewezen = Referentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    # afgewezen = ("AFG", "Afgewezen")
    """
    Het koppelen van de overeenkomsten is afgewezen
    """

    gekoppeld = Referentiedata(
        code="GEK",
        naam="Gekoppeld",
    )
    # gekoppeld = ("GEK", "Gekoppeld")
    """
    Het koppelen van de overeenkomsten is gekoppeld
    """
