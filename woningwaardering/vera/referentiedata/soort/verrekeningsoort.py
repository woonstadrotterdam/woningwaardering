from vera.referentiedata.models import Referentiedata


class Verrekeningsoort:
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
