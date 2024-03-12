
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class CONTACTGEGEVENSTATUS:

    aangemaakt = Referentiedata(
        code="AAN",
        naam="Aangemaakt",
    )
    # aangemaakt = ("AAN", "Aangemaakt")
    """
    Het contactgegeven is aangemaakt.
    """

    gevalideerd = Referentiedata(
        code="GEV",
        naam="Gevalideerd",
    )
    # gevalideerd = ("GEV", "Gevalideerd")
    """
    Het contactgeggeven is gevalideerd via een mail, sms etc.
    """

    ongeldig = Referentiedata(
        code="ONG",
        naam="Ongeldig",
    )
    # ongeldig = ("ONG", "Ongeldig")
    """
    Het contactgegeven is niet (meer) geldig.
    """
