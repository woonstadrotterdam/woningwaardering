
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class AANBIEDINGSTATUS:

    aangeboden = Referentiedata(
        code="AAN",
        naam="Aangeboden",
    )
    # aangeboden = ("AAN", "Aangeboden")
    """
    Er is aanbieding gedaan aan een of meer kandidaten.
    """

    geweigerd = Referentiedata(
        code="GEW",
        naam="Geweigerd",
    )
    # geweigerd = ("GEW", "Geweigerd")
    """
    Een kandidaat heeft een verstrekte aanbieding afgewezen.
    """

    ingetrokken = Referentiedata(
        code="ING",
        naam="Ingetrokken",
    )
    # ingetrokken = ("ING", "Ingetrokken")
    """
    Een aan een kandidaat verstrekte aanbieding is ingetrokken.
    """

    toegewezen = Referentiedata(
        code="TOE",
        naam="Toegewezen",
    )
    # toegewezen = ("TOE", "Toegewezen")
    """
    Een eenheid is toegewezen aan een kandidaat.
    """
