from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class SanctiestatusReferentiedata(Referentiedata):
    pass


class Sanctiestatus(Referentiedatasoort):
    aangemaakt = SanctiestatusReferentiedata(
        code="AAN",
        naam="Aangemaakt",
    )
    """
    Aangemaakt
    """

    definitief = SanctiestatusReferentiedata(
        code="DEF",
        naam="Definitief",
    )
    """
    Definitief (na 1e van de volgende kalendermaand)
    """

    ingetrokken = SanctiestatusReferentiedata(
        code="ING",
        naam="Ingetrokken",
    )
    """
    Ingetrokken
    """
