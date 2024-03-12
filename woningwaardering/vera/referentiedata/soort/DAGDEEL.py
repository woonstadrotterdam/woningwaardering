
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class DAGDEEL:

    avond = Referentiedata(
        code="AVO",
        naam="Avond",
    )
    # avond = ("AVO", "Avond")
    """
    Tussen 18 en 24 uur.
    """

    middag = Referentiedata(
        code="MID",
        naam="Middag",
    )
    # middag = ("MID", "Middag")
    """
    Tussen 12 en 18 uur.
    """

    ochtend = Referentiedata(
        code="OCH",
        naam="Ochtend",
    )
    # ochtend = ("OCH", "Ochtend")
    """
    Tussen 8 en 12 uur.
    """
