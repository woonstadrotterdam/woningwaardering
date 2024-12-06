from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Verrekeningsoort(Referentiedatasoort):
    te_activeren = Referentiedata(
        code="ACT",
        naam="Te activeren",
    )
    """
    Bij de verrekening wordt (een deel van) het bedrag geactiveerd
    """

    te_verhalen = Referentiedata(
        code="VER",
        naam="Te verhalen",
    )
    """
    Bij de verrekening wordt (een deel van) het bedrag verhaald op een derde partij
    """
