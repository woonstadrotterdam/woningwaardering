
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class GROOTBOEKREKENINGSTATUS:

    actief = Referentiedata(
        code="ACT",
        naam="Actief",
    )
    # actief = ("ACT", "Actief")

    geblokkeerd = Referentiedata(
        code="BLK",
        naam="Geblokkeerd",
    )
    # geblokkeerd = ("BLK", "Geblokkeerd")

    historisch = Referentiedata(
        code="HIS",
        naam="Historisch",
    )
    # historisch = ("HIS", "Historisch")
