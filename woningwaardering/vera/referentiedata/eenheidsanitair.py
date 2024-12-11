from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EenheidsanitairReferentiedata(Referentiedata):
    pass


class Eenheidsanitair(Referentiedatasoort):
    ligbad = EenheidsanitairReferentiedata(
        code="BAD",
        naam="Ligbad",
    )

    aparte_douche = EenheidsanitairReferentiedata(
        code="DOU",
        naam="Aparte douche",
    )

    apart_toilet = EenheidsanitairReferentiedata(
        code="TOI",
        naam="Apart toilet",
    )
