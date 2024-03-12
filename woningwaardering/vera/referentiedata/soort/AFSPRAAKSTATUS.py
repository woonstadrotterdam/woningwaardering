
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class AFSPRAAKSTATUS:

    aangevraagd = Referentiedata(
        code="AAN",
        naam="Aangevraagd",
    )
    # aangevraagd = ("AAN", "Aangevraagd")
    """
    De afspraak is nog niet gepland, maar wel aangevraagd. Daarbij kan eventueel een
    voorkeur bloktijd zijn opgegeven.
    """

    afgerond = Referentiedata(
        code="AFG",
        naam="Afgerond",
    )
    # afgerond = ("AFG", "Afgerond")
    """
    De afspraak heeft plaatsgevonden.
    """

    geannuleerd = Referentiedata(
        code="ANN",
        naam="Geannuleerd",
    )
    # geannuleerd = ("ANN", "Geannuleerd")
    """
    De afspraak is geannuleerd.
    """

    gepland = Referentiedata(
        code="GEP",
        naam="Gepland",
    )
    # gepland = ("GEP", "Gepland")
    """
    De afspraak is gepland. Hierbij zal doorgaans ook een medewerker zijn toegewezen.
    """
