
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class BETAALGEGEVENSOORT:

    bankrekening = Referentiedata(
        code="BAN",
        naam="Bankrekening",
    )
    # bankrekening = ("BAN", "Bankrekening")
    """
    Het betaalgegeven van een relatie, behorende bij een overeenkomst, is een
    bankrekening.
    """

    creditcard = Referentiedata(
        code="CRE",
        naam="Creditcard",
    )
    # creditcard = ("CRE", "Creditcard")
    """
    Het betaalgegeven van een relatie, behorende bij een overeenkomst, is een credit
    card.
    """

    paypal_account = Referentiedata(
        code="PAY",
        naam="Paypal account",
    )
    # paypal_account = ("PAY", "Paypal account")
    """
    Het betaalgegeven van een relatie, behorende bij een overeenkomst, is een paypal
    account.
    """

    transfermate = Referentiedata(
        code="TRA",
        naam="TransferMate",
    )
    # transfermate = ("TRA", "TransferMate")
    """
    Het betaalgegeven van een relatie, behorende bij een overeenkomst, is een
    TransferMate account.
    """
