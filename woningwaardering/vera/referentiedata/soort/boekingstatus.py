from vera.referentiedata.models import Referentiedata


class Boekingstatus:
    gefiatteerd = Referentiedata(
        code="FIA",
        naam="Gefiatteerd",
    )
    """
    Boeking is definitief en niet meer wijzigbaar.
    """

    historisch = Referentiedata(
        code="HIS",
        naam="Historisch",
    )
    """
    Boeking is onderdeel van een afgesloten administratieve periode of boekjaar.
    """

    voorlopig = Referentiedata(
        code="VRL",
        naam="Voorlopig",
    )
    """
    Boeking is niet definitief en kan worden gewijzigd of verwijderd.
    """
