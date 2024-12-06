from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Bouwkundigelementsoort(Referentiedatasoort):
    overig = Referentiedata(
        code="OVE",
        naam="Overig",
    )

    verwarming = Referentiedata(
        code="VER",
        naam="Verwarming",
    )

    voorziening = Referentiedata(
        code="VOO",
        naam="Voorziening",
    )

    warmwater = Referentiedata(
        code="WAT",
        naam="Warmwater",
    )
