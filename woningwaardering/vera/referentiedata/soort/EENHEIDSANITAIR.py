from woningwaardering.vera.bvg.models import Referentiedata


class EENHEIDSANITAIR:
    ligbad = Referentiedata(
        code="BAD",
        naam="Ligbad",
    )

    aparte_douche = Referentiedata(
        code="DOU",
        naam="Aparte douche",
    )

    apart_toilet = Referentiedata(
        code="TOI",
        naam="Apart toilet",
    )
