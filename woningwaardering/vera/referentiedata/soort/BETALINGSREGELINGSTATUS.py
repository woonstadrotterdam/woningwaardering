
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class BETALINGSREGELINGSTATUS:

    aangevraagd = Referentiedata(
        code="AAN",
        naam="Aangevraagd",
    )
    # aangevraagd = ("AAN", "Aangevraagd")
    """
    Ook wel aangemaakt.
    """

    actief = Referentiedata(
        code="ACT",
        naam="Actief",
    )
    # actief = ("ACT", "Actief")
    """
    Toegekende betalingsregeling die loopt.
    """

    geannuleerd = Referentiedata(
        code="ANN",
        naam="Geannuleerd",
    )
    # geannuleerd = ("ANN", "Geannuleerd")
    """
    Tussentijds gestopte regeling.
    """

    beeindigd = Referentiedata(
        code="BEE",
        naam="Beëindigd",
    )
    # beeindigd = ("BEE", "Beëindigd")
    """
    Ook wel afgerond. Alle betalingsverplichtingen zijn voldaan.
    """

    bevroren = Referentiedata(
        code="BEV",
        naam="Bevroren",
    )
    # bevroren = ("BEV", "Bevroren")
    """
    Tussentijds bevroren betalingsregeling omdat het niet mogelijk is om te voldoen aan
    de regeling.
    """
