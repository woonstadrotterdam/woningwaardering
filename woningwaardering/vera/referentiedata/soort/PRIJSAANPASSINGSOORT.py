
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class PRIJSAANPASSINGSOORT:

    korting = Referentiedata(
        code="KOR",
        naam="Korting",
    )
    # korting = ("KOR", "Korting")

    toeslag = Referentiedata(
        code="TOE",
        naam="Toeslag",
    )
    # toeslag = ("TOE", "Toeslag")
