from woningwaardering.vera.bvg.generated import Referentiedata


class Grootboekrekeningstatus:
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
