from vera.referentiedata.models import Referentiedata


class Dagdeel:
    avond = Referentiedata(
        code="AVO",
        naam="Avond",
    )
    """
    Tussen 18 en 24 uur.
    """

    middag = Referentiedata(
        code="MID",
        naam="Middag",
    )
    """
    Tussen 12 en 18 uur.
    """

    ochtend = Referentiedata(
        code="OCH",
        naam="Ochtend",
    )
    """
    Tussen 8 en 12 uur.
    """
