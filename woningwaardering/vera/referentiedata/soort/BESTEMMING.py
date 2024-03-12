
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class BESTEMMING:

    huur = Referentiedata(
        code="HUU",
        naam="Huur",
    )
    # huur = ("HUU", "Huur")
    """
    Eenheid is bestemd voor verhuur bij mutatie.
    """

    koop = Referentiedata(
        code="KOO",
        naam="Koop",
    )
    # koop = ("KOO", "Koop")
    """
    Eenheid is bestemd voor verkoop bij mutatie.
    """

    sloop = Referentiedata(
        code="SLO",
        naam="Sloop",
    )
    # sloop = ("SLO", "Sloop")
    """
    Eenheid is bestemd voor sloop bij mutatie.
    """
