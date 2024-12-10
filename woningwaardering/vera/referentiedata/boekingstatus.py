from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BoekingstatusReferentiedata(Referentiedata):
    pass


class Boekingstatus(Referentiedatasoort):
    gefiatteerd = BoekingstatusReferentiedata(
        code="FIA",
        naam="Gefiatteerd",
    )
    """
    Boeking is definitief en niet meer wijzigbaar.
    """

    historisch = BoekingstatusReferentiedata(
        code="HIS",
        naam="Historisch",
    )
    """
    Boeking is onderdeel van een afgesloten administratieve periode of boekjaar.
    """

    voorlopig = BoekingstatusReferentiedata(
        code="VRL",
        naam="Voorlopig",
    )
    """
    Boeking is niet definitief en kan worden gewijzigd of verwijderd.
    """
