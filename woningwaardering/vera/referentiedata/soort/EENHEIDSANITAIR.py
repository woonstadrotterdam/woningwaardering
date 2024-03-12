
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class EENHEIDSANITAIR:

    ligbad = Referentiedata(
        code="BAD",
        naam="Ligbad",
    )
    # ligbad = ("BAD", "Ligbad")

    aparte_douche = Referentiedata(
        code="DOU",
        naam="Aparte douche",
    )
    # aparte_douche = ("DOU", "Aparte douche")

    apart_toilet = Referentiedata(
        code="TOI",
        naam="Apart toilet",
    )
    # apart_toilet = ("TOI", "Apart toilet")
