from vera.bvg.generated import Referentiedata


class Bouwkundigelementsoort:
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
