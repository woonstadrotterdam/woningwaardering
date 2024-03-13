from woningwaardering.vera.bvg.models import Referentiedata


class CREDITEURSTATUS:
    actief = Referentiedata(
        code="ACT",
        naam="Actief",
    )

    alleen_voor_betalen = Referentiedata(
        code="BET",
        naam="Alleen voor betalen",
    )
    """
    Korting
    """

    geblokkeerd = Referentiedata(
        code="GEB",
        naam="Geblokkeerd",
    )
    """
    Toeslag
    """

    voorlopig = Referentiedata(
        code="VRL",
        naam="Voorlopig",
    )
