from woningwaardering.vera.bvg.models import Referentiedata


class DEBITEURSTATUS:
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
