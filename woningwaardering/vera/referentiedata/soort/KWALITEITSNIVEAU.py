from woningwaardering.vera.bvg.models import Referentiedata


class KWALITEITSNIVEAU:
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
