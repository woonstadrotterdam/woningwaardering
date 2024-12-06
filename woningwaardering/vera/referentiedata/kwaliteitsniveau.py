from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Kwaliteitsniveau(Referentiedatasoort):
    eenvoudig = Referentiedata(
        code="EEN",
        naam="Eenvoudig",
    )

    hoogwaardig = Referentiedata(
        code="HOO",
        naam="Hoogwaardig",
    )

    luxe = Referentiedata(
        code="LUX",
        naam="Luxe",
    )

    standaard = Referentiedata(
        code="STA",
        naam="Standaard",
    )
