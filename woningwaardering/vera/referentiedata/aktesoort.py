from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class AktesoortReferentiedata(Referentiedata):
    pass


class Aktesoort(Referentiedatasoort):
    notariele_akte = AktesoortReferentiedata(
        code="NOT",
        naam="Notariële akte",
    )
    """
    Akte vastgelegd bij de notaris.
    """

    onderhandse_akte = AktesoortReferentiedata(
        code="OND",
        naam="Onderhandse akte",
    )
    """
    Akte die door twee of meer partijen is vastgesteld (onderhands)
    """
