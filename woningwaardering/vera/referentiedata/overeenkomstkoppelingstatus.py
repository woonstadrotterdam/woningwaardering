from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class OvereenkomstkoppelingstatusReferentiedata(Referentiedata):
    pass


class Overeenkomstkoppelingstatus(Referentiedatasoort):
    aangevraagd = OvereenkomstkoppelingstatusReferentiedata(
        code="AAN",
        naam="Aangevraagd",
    )
    """
    Het koppelen van de overeenkomsten is aangevraagd
    """

    afgewezen = OvereenkomstkoppelingstatusReferentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    """
    Het koppelen van de overeenkomsten is afgewezen
    """

    gekoppeld = OvereenkomstkoppelingstatusReferentiedata(
        code="GEK",
        naam="Gekoppeld",
    )
    """
    Het koppelen van de overeenkomsten is gekoppeld
    """
