
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class VERREKENINGSOORT:

    te_activeren = Referentiedata(
        code="ACT",
        naam="Te activeren",
    )
    # te_activeren = ("ACT", "Te activeren")
    """
    Bij de verrekening wordt (een deel van) het bedrag geactiveerd
    """

    te_verhalen = Referentiedata(
        code="VER",
        naam="Te verhalen",
    )
    # te_verhalen = ("VER", "Te verhalen")
    """
    Bij de verrekening wordt (een deel van) het bedrag verhaald op een derde partij
    """
