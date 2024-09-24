from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Betaalgegevensoort(Enum):
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

    @property
    def code(self) -> str:
        if self.value.code is None:
            raise TypeError("de code van een Referentiedata object mag niet None zijn")
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
