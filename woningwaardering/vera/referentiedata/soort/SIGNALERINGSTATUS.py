
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class SIGNALERINGSTATUS:

    actief = Referentiedata(
        code="ACT",
        naam="Actief",
    )
    # actief = ("ACT", "Actief")

    passief = Referentiedata(
        code="PAS",
        naam="Passief",
    )
    # passief = ("PAS", "Passief")

    vervallen = Referentiedata(
        code="VER",
        naam="Vervallen",
    )
    # vervallen = ("VER", "Vervallen")
