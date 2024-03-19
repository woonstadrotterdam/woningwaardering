from vera.bvg.generated import Referentiedata


class Overeenkomstkoppelingstatus:
    aangevraagd = Referentiedata(
        code="AAN",
        naam="Aangevraagd",
    )
    """
    Het koppelen van de overeenkomsten is aangevraagd
    """

    afgewezen = Referentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    """
    Het koppelen van de overeenkomsten is afgewezen
    """

    gekoppeld = Referentiedata(
        code="GEK",
        naam="Gekoppeld",
    )
    """
    Het koppelen van de overeenkomsten is gekoppeld
    """
