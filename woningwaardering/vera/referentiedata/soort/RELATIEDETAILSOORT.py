
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class RELATIEDETAILSOORT:

    huishouden = Referentiedata(
        code="HUI",
        naam="Huishouden",
    )
    # huishouden = ("HUI", "Huishouden")
    """
    Een huishouden bestaat uit één of meer personen die op hetzelfde adres wonen en een
    economisch-consumptieve eenheid vormen. (CORA)
    """
