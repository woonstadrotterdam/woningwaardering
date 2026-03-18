from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BetaalwijzesoortReferentiedata(Referentiedata):
    pass


class Betaalwijzesoort(Referentiedatasoort):
    contant = BetaalwijzesoortReferentiedata(
        code="CON",
        naam="Contant",
    )
    """
    Een door de betaler geïniteerde betaling, via contante betaling.
    """

    incasso = BetaalwijzesoortReferentiedata(
        code="INC",
        naam="Incasso",
    )
    """
    Een door de ontvanger geïnitieerde incasso, er moet een Incassomachtiging aan ten
    grondslag liggen.
    """

    e_mail = BetaalwijzesoortReferentiedata(
        code="MAI",
        naam="E-mail",
    )
    """
    Een door de betaler geïniteerde betaling, door middel van een betaallink via e-mail.
    """

    online = BetaalwijzesoortReferentiedata(
        code="ONL",
        naam="Online",
    )
    """
    Een door de betaler geïniteerde betaling, door online betaling. Bijvoorbeeld door
    middel van iDEAL.
    """

    overboeking = BetaalwijzesoortReferentiedata(
        code="OVB",
        naam="Overboeking",
    )
    """
    Een door de betaler geïniteerde betaling, door (periodieke) overboeking.
    """

    pin_betaling = BetaalwijzesoortReferentiedata(
        code="PIN",
        naam="Pin-betaling",
    )
    """
    Een door de betaler geïniteerde betaling, via PIN-betaling
    """
