
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class PUBLICATIESTATUS:

    in_aanbieding = Referentiedata(
        code="AAN",
        naam="In aanbieding",
    )
    # in_aanbieding = ("AAN", "In aanbieding")
    """
    Het gepubliceerde vastgoed is in aanbieding.
    """

    afgerond = Referentiedata(
        code="AFG",
        naam="Afgerond",
    )
    # afgerond = ("AFG", "Afgerond")
    """
    De publicatie van het vastgoed is afgerond.
    """

    gepubliceerd = Referentiedata(
        code="GEP",
        naam="Gepubliceerd",
    )
    # gepubliceerd = ("GEP", "Gepubliceerd")
    """
    Het beschikbaar vastgoed is gepubliceerd.
    """

    gereed_voor_publicatie = Referentiedata(
        code="GER",
        naam="Gereed voor publicatie",
    )
    # gereed_voor_publicatie = ("GER", "Gereed voor publicatie")
    """
    De publicatie van beschikbaar vastgoed is gereed voor publicatie.
    """

    ingetrokken = Referentiedata(
        code="ING",
        naam="Ingetrokken",
    )
    # ingetrokken = ("ING", "Ingetrokken")
    """
    De publicatie van het vastgoed is ingetrokken.
    """

    in_voorbereiding = Referentiedata(
        code="VOO",
        naam="In voorbereiding",
    )
    # in_voorbereiding = ("VOO", "In voorbereiding")
    """
    De publicatie van beschikbaar vastgoed is in voorbereiding.
    """
