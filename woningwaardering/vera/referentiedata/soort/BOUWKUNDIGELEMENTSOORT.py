
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class BOUWKUNDIGELEMENTSOORT:

    overig = Referentiedata(
        code="OVE",
        naam="Overig",
    )
    # overig = ("OVE", "Overig")

    verwarming = Referentiedata(
        code="VER",
        naam="Verwarming",
    )
    # verwarming = ("VER", "Verwarming")

    voorziening = Referentiedata(
        code="VOO",
        naam="Voorziening",
    )
    # voorziening = ("VOO", "Voorziening")

    warmwater = Referentiedata(
        code="WAT",
        naam="Warmwater",
    )
    # warmwater = ("WAT", "Warmwater")
