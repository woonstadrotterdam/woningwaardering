from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BetalingsregelingstatusReferentiedata(Referentiedata):
    pass


class Betalingsregelingstatus(Referentiedatasoort):
    aangevraagd = BetalingsregelingstatusReferentiedata(
        code="AAN",
        naam="Aangevraagd",
    )
    """
    Ook wel aangemaakt.
    """

    actief = BetalingsregelingstatusReferentiedata(
        code="ACT",
        naam="Actief",
    )
    """
    Toegekende betalingsregeling die loopt.
    """

    geannuleerd = BetalingsregelingstatusReferentiedata(
        code="ANN",
        naam="Geannuleerd",
    )
    """
    Tussentijds gestopte regeling.
    """

    beeindigd = BetalingsregelingstatusReferentiedata(
        code="BEE",
        naam="Beëindigd",
    )
    """
    Ook wel afgerond. Alle betalingsverplichtingen zijn voldaan.
    """

    bevroren = BetalingsregelingstatusReferentiedata(
        code="BEV",
        naam="Bevroren",
    )
    """
    Tussentijds bevroren betalingsregeling omdat het niet mogelijk is om te voldoen aan
    de regeling.
    """
