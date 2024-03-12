
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class BETAALWIJZESOORT:

    handmatige_overboeking = Referentiedata(
        code="HND",
        naam="Handmatige overboeking",
    )
    # handmatige_overboeking = ("HND", "Handmatige overboeking")
    """
    Een door de betaler geïnitieerde betaling, via een bankoverboeking , een voldaan
    betaalverzoek of via een PIN-betaling.
    """

    incasso = Referentiedata(
        code="INC",
        naam="Incasso",
    )
    # incasso = ("INC", "Incasso")
    """
    Een door de ontvanger geïnitieerde incasso, er moet een Incassomachtiging aan ten
    grondslag liggen.
    """
