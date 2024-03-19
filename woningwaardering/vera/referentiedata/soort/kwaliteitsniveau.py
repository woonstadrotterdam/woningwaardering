from vera.bvg.generated import Referentiedata


class Kwaliteitsniveau:
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
