from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Vacaturesoort(Referentiedatasoort):
    tijdelijke_inhuur = Referentiedata(
        code="TIJ",
        naam="Tijdelijke inhuur",
    )
    """
    Tijdelijke inhuur
    """

    vaste_dienst = Referentiedata(
        code="VAS",
        naam="Vaste dienst",
    )
    """
    Vaste dienst
    """
