from vera.bvg.generated import Referentiedata


class Aanbiedingstatus:
    aangeboden = Referentiedata(
        code="AAN",
        naam="Aangeboden",
    )
    """
    Er is aanbieding gedaan aan een of meer kandidaten.
    """

    geweigerd = Referentiedata(
        code="GEW",
        naam="Geweigerd",
    )
    """
    Een kandidaat heeft een verstrekte aanbieding afgewezen.
    """

    ingetrokken = Referentiedata(
        code="ING",
        naam="Ingetrokken",
    )
    """
    Een aan een kandidaat verstrekte aanbieding is ingetrokken.
    """

    toegewezen = Referentiedata(
        code="TOE",
        naam="Toegewezen",
    )
    """
    Een eenheid is toegewezen aan een kandidaat.
    """
