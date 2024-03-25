from woningwaardering.vera.bvg.generated import Referentiedata


class Eenheidsanitair:
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
