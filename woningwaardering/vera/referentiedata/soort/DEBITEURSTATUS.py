
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class DEBITEURSTATUS:

    actief = Referentiedata(
        code="ACT",
        naam="Actief",
    )
    # actief = ("ACT", "Actief")

    alleen_voor_betalen = Referentiedata(
        code="BET",
        naam="Alleen voor betalen",
    )
    # alleen_voor_betalen = ("BET", "Alleen voor betalen")

    geblokkeerd = Referentiedata(
        code="GEB",
        naam="Geblokkeerd",
    )
    # geblokkeerd = ("GEB", "Geblokkeerd")

    voorlopig = Referentiedata(
        code="VRL",
        naam="Voorlopig",
    )
    # voorlopig = ("VRL", "Voorlopig")
