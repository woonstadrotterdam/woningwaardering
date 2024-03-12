
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class SANCTIESTATUS:

    aangemaakt = Referentiedata(
        code="AAN",
        naam="Aangemaakt",
    )
    # aangemaakt = ("AAN", "Aangemaakt")
    """
    Aangemaakt
    """

    definitief = Referentiedata(
        code="DEF",
        naam="Definitief",
    )
    # definitief = ("DEF", "Definitief")
    """
    Definitief (na 1e van de volgende kalendermaand)
    """

    ingetrokken = Referentiedata(
        code="ING",
        naam="Ingetrokken",
    )
    # ingetrokken = ("ING", "Ingetrokken")
    """
    Ingetrokken
    """
