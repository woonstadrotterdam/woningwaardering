from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class AfspraakstatusReferentiedata(Referentiedata):
    pass


class Afspraakstatus(Referentiedatasoort):
    aangevraagd = AfspraakstatusReferentiedata(
        code="AAN",
        naam="Aangevraagd",
    )
    """
    De afspraak is nog niet gepland, maar wel aangevraagd. Daarbij kan eventueel een
    voorkeur bloktijd zijn opgegeven.
    """

    afgerond = AfspraakstatusReferentiedata(
        code="AFG",
        naam="Afgerond",
    )
    """
    De afspraak heeft plaatsgevonden.
    """

    geannuleerd = AfspraakstatusReferentiedata(
        code="ANN",
        naam="Geannuleerd",
    )
    """
    De afspraak is geannuleerd.
    """

    gepland = AfspraakstatusReferentiedata(
        code="GEP",
        naam="Gepland",
    )
    """
    De afspraak is gepland. Hierbij zal doorgaans ook een medewerker zijn toegewezen.
    """
