from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Tijdseenheid(Referentiedatasoort):
    uren = Referentiedata(
        code="UUR",
        naam="Uren",
    )
    """
    Registratie van de duur in uren
    """

    minuten = Referentiedata(
        code="MIN",
        naam="Minuten",
    )
    """
    Registratie van de duur in minuten
    """
