
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class EXTERNEINCASSOSTATUS:

    actief = Referentiedata(
        code="ACT",
        naam="Actief",
    )
    # actief = ("ACT", "Actief")

    beeindigd = Referentiedata(
        code="EIN",
        naam="Beëindigd",
    )
    # beeindigd = ("EIN", "Beëindigd")

    nieuw = Referentiedata(
        code="NIE",
        naam="Nieuw",
    )
    # nieuw = ("NIE", "Nieuw")
