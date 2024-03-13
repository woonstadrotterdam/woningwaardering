from woningwaardering.vera.bvg.models import Referentiedata


class VERBIJZONDERINGSTATUS:
    actief = Referentiedata(
        code="ACT",
        naam="Actief",
    )

    geblokkeerd = Referentiedata(
        code="BLK",
        naam="Geblokkeerd",
    )

    historisch = Referentiedata(
        code="HIS",
        naam="Historisch",
    )
