from woningwaardering.vera.bvg.models import Referentiedata


class BETAALGEGEVENSOORT:
    bankrekening = Referentiedata(
        code="BAN",
        naam="Bankrekening",
    )
    """
    Het betaalgegeven van een relatie, behorende bij een overeenkomst,  is een
    bankrekening.
    """

    creditcard = Referentiedata(
        code="CRE",
        naam="Creditcard",
    )
    """
    Het betaalgegeven van een relatie, behorende bij een overeenkomst,  is een credit
    card.
    """

    paypal_account = Referentiedata(
        code="PAY",
        naam="Paypal account",
    )
    """
    Het betaalgegeven van een relatie, behorende bij een overeenkomst,  is een paypal
    account.
    """

    transfermate = Referentiedata(
        code="TRA",
        naam="TransferMate",
    )
    """
    Het betaalgegeven van een relatie, behorende bij een overeenkomst,  is een
    TransferMate account.
    """
