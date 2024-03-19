from vera.referentiedata.models import Referentiedata


class Sanctiestatus:
    aangemaakt = Referentiedata(
        code="AAN",
        naam="Aangemaakt",
    )
    """
    Aangemaakt
    """

    definitief = Referentiedata(
        code="DEF",
        naam="Definitief",
    )
    """
    Definitief (na 1e van de volgende kalendermaand)
    """

    ingetrokken = Referentiedata(
        code="ING",
        naam="Ingetrokken",
    )
    """
    Ingetrokken
    """
