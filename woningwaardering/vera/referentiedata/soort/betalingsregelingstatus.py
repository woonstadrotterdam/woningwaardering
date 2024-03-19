from vera.bvg.generated import Referentiedata


class Betalingsregelingstatus:
    aangevraagd = Referentiedata(
        code="AAN",
        naam="Aangevraagd",
    )
    """
    Ook wel aangemaakt.
    """

    actief = Referentiedata(
        code="ACT",
        naam="Actief",
    )
    """
    Toegekende betalingsregeling die loopt.
    """

    geannuleerd = Referentiedata(
        code="ANN",
        naam="Geannuleerd",
    )
    """
    Tussentijds gestopte regeling.
    """

    beeindigd = Referentiedata(
        code="BEE",
        naam="Beëindigd",
    )
    """
    Ook wel afgerond. Alle betalingsverplichtingen zijn voldaan.
    """

    bevroren = Referentiedata(
        code="BEV",
        naam="Bevroren",
    )
    """
    Tussentijds bevroren betalingsregeling omdat het niet mogelijk is om te voldoen aan
    de regeling.
    """
