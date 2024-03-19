from vera.bvg.generated import Referentiedata


class Afspraakstatus:
    aangevraagd = Referentiedata(
        code="AAN",
        naam="Aangevraagd",
    )
    """
    De afspraak is nog niet gepland, maar wel aangevraagd. Daarbij kan eventueel een
    voorkeur bloktijd zijn opgegeven.
    """

    afgerond = Referentiedata(
        code="AFG",
        naam="Afgerond",
    )
    """
    De afspraak heeft plaatsgevonden.
    """

    geannuleerd = Referentiedata(
        code="ANN",
        naam="Geannuleerd",
    )
    """
    De afspraak is geannuleerd.
    """

    gepland = Referentiedata(
        code="GEP",
        naam="Gepland",
    )
    """
    De afspraak is gepland. Hierbij zal doorgaans ook een medewerker zijn toegewezen.
    """
