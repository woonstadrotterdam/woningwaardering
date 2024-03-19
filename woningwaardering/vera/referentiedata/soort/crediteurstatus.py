from vera.bvg.generated import Referentiedata


class Crediteurstatus:
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
