from vera.bvg.generated import Referentiedata


class Betaalwijzesoort:
    handmatige_overboeking = Referentiedata(
        code="HND",
        naam="Handmatige overboeking",
    )
    """
    Een door de betaler geïnitieerde betaling, via een bankoverboeking , een voldaan
    betaalverzoek of via een PIN-betaling.
    """

    incasso = Referentiedata(
        code="INC",
        naam="Incasso",
    )
    """
    Een door de ontvanger geïnitieerde incasso, er moet een Incassomachtiging aan ten
    grondslag liggen.
    """
