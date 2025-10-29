from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class KwaliteitsniveauReferentiedata(Referentiedata):
    pass


class Kwaliteitsniveau(Referentiedatasoort):
    eenvoudig = KwaliteitsniveauReferentiedata(
        code="EEN",
        naam="Eenvoudig",
    )

    hoogwaardig = KwaliteitsniveauReferentiedata(
        code="HOO",
        naam="Hoogwaardig",
    )

    luxe = KwaliteitsniveauReferentiedata(
        code="LUX",
        naam="Luxe",
    )

    standaard = KwaliteitsniveauReferentiedata(
        code="STA",
        naam="Standaard",
    )
