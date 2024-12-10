from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BouwkundigelementsoortReferentiedata(Referentiedata):
    pass


class Bouwkundigelementsoort(Referentiedatasoort):
    overig = BouwkundigelementsoortReferentiedata(
        code="OVE",
        naam="Overig",
    )

    verwarming = BouwkundigelementsoortReferentiedata(
        code="VER",
        naam="Verwarming",
    )

    voorziening = BouwkundigelementsoortReferentiedata(
        code="VOO",
        naam="Voorziening",
    )

    warmwater = BouwkundigelementsoortReferentiedata(
        code="WAT",
        naam="Warmwater",
    )
