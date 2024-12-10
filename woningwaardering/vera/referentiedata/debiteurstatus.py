from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class DebiteurstatusReferentiedata(Referentiedata):
    pass


class Debiteurstatus(Referentiedatasoort):
    actief = DebiteurstatusReferentiedata(
        code="ACT",
        naam="Actief",
    )

    alleen_voor_betalen = DebiteurstatusReferentiedata(
        code="BET",
        naam="Alleen voor betalen",
    )

    geblokkeerd = DebiteurstatusReferentiedata(
        code="GEB",
        naam="Geblokkeerd",
    )

    voorlopig = DebiteurstatusReferentiedata(
        code="VRL",
        naam="Voorlopig",
    )
