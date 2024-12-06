from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Aktesoort(Referentiedatasoort):
    notariele_akte = Referentiedata(
        code="NOT",
        naam="Notariële akte",
    )
    """
    Akte vastgelegd bij de notaris.
    """

    onderhandse_akte = Referentiedata(
        code="OND",
        naam="Onderhandse akte",
    )
    """
    Akte die door twee of meer partijen is vastgesteld (onderhands)
    """
