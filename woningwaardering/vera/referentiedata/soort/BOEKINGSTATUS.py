
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class BOEKINGSTATUS:

    gefiatteerd = Referentiedata(
        code="FIA",
        naam="Gefiatteerd",
    )
    # gefiatteerd = ("FIA", "Gefiatteerd")
    """
    Boeking is definitief en niet meer wijzigbaar.
    """

    historisch = Referentiedata(
        code="HIS",
        naam="Historisch",
    )
    # historisch = ("HIS", "Historisch")
    """
    Boeking is onderdeel van een afgesloten administratieve periode of boekjaar.
    """

    voorlopig = Referentiedata(
        code="VRL",
        naam="Voorlopig",
    )
    # voorlopig = ("VRL", "Voorlopig")
    """
    Boeking is niet definitief en kan worden gewijzigd of verwijderd.
    """
