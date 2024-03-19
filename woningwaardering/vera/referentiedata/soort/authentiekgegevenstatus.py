from vera.bvg.generated import Referentiedata


class Authentiekgegevenstatus:
    gevalideerd = Referentiedata(
        code="GEV",
        naam="Gevalideerd",
    )
    """
    Gegevens zijn gevalideerd door de bron.
    """

    vervallen = Referentiedata(
        code="VER",
        naam="Vervallen",
    )
    """
    Gegevens zijn vervallen doordat deze zijn verlopen.
    """
