from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class TijdseenheidReferentiedata(Referentiedata):
    pass


class Tijdseenheid(Referentiedatasoort):
    uren = TijdseenheidReferentiedata(
        code="UUR",
        naam="Uren",
    )
    """
    Registratie van de duur in uren
    """

    minuten = TijdseenheidReferentiedata(
        code="MIN",
        naam="Minuten",
    )
    """
    Registratie van de duur in minuten
    """
