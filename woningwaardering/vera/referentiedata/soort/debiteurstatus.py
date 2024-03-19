from vera.bvg.generated import Referentiedata


class Debiteurstatus:
    actief = Referentiedata(
        code="ACT",
        naam="Actief",
    )

    alleen_voor_betalen = Referentiedata(
        code="BET",
        naam="Alleen voor betalen",
    )

    geblokkeerd = Referentiedata(
        code="GEB",
        naam="Geblokkeerd",
    )

    voorlopig = Referentiedata(
        code="VRL",
        naam="Voorlopig",
    )
