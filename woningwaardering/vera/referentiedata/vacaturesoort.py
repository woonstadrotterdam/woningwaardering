from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class VacaturesoortReferentiedata(Referentiedata):
    pass


class Vacaturesoort(Referentiedatasoort):
    tijdelijke_inhuur = VacaturesoortReferentiedata(
        code="TIJ",
        naam="Tijdelijke inhuur",
    )
    """
    Tijdelijke inhuur
    """

    vaste_dienst = VacaturesoortReferentiedata(
        code="VAS",
        naam="Vaste dienst",
    )
    """
    Vaste dienst
    """
