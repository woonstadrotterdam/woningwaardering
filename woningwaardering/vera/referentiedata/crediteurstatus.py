from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class CrediteurstatusReferentiedata(Referentiedata):
    pass


class Crediteurstatus(Referentiedatasoort):
    actief = CrediteurstatusReferentiedata(
        code="ACT",
        naam="Actief",
    )

    alleen_voor_betalen = CrediteurstatusReferentiedata(
        code="BET",
        naam="Alleen voor betalen",
    )
    """
    Korting
    """

    geblokkeerd = CrediteurstatusReferentiedata(
        code="GEB",
        naam="Geblokkeerd",
    )
    """
    Toeslag
    """

    voorlopig = CrediteurstatusReferentiedata(
        code="VRL",
        naam="Voorlopig",
    )
