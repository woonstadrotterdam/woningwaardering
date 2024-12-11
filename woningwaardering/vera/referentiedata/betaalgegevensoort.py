from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BetaalgegevensoortReferentiedata(Referentiedata):
    pass


class Betaalgegevensoort(Referentiedatasoort):
    bankrekening = BetaalgegevensoortReferentiedata(
        code="BAN",
        naam="Bankrekening",
    )
    """
    Het betaalgegeven van een relatie, behorende bij een overeenkomst,  is een
    bankrekening.
    """

    creditcard = BetaalgegevensoortReferentiedata(
        code="CRE",
        naam="Creditcard",
    )
    """
    Het betaalgegeven van een relatie, behorende bij een overeenkomst,  is een credit
    card.
    """

    paypal_account = BetaalgegevensoortReferentiedata(
        code="PAY",
        naam="Paypal account",
    )
    """
    Het betaalgegeven van een relatie, behorende bij een overeenkomst,  is een paypal
    account.
    """

    transfermate = BetaalgegevensoortReferentiedata(
        code="TRA",
        naam="TransferMate",
    )
    """
    Het betaalgegeven van een relatie, behorende bij een overeenkomst,  is een
    TransferMate account.
    """
