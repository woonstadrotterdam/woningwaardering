from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BetaalwijzesoortReferentiedata(Referentiedata):
    pass


class Betaalwijzesoort(Referentiedatasoort):
    handmatige_overboeking = BetaalwijzesoortReferentiedata(
        code="HND",
        naam="Handmatige overboeking",
    )
    """
    Een door de betaler geïnitieerde betaling, via een bankoverboeking , een voldaan
    betaalverzoek of via een PIN-betaling.
    """

    incasso = BetaalwijzesoortReferentiedata(
        code="INC",
        naam="Incasso",
    )
    """
    Een door de ontvanger geïnitieerde incasso, er moet een Incassomachtiging aan ten
    grondslag liggen.
    """
