from woningwaardering.vera.bvg.models import Referentiedata


class BOUWKUNDIGELEMENTSOORT:
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
