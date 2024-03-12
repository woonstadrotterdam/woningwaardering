
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class AUTHENTIEKGEGEVENSTATUS:

    gevalideerd = Referentiedata(
        code="GEV",
        naam="Gevalideerd",
    )
    # gevalideerd = ("GEV", "Gevalideerd")
    """
    Gegevens zijn gevalideerd door de bron.
    """

    vervallen = Referentiedata(
        code="VER",
        naam="Vervallen",
    )
    # vervallen = ("VER", "Vervallen")
    """
    Gegevens zijn vervallen doordat deze zijn verlopen.
    """
