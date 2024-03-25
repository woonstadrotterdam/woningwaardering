from woningwaardering.vera.bvg.generated import Referentiedata


class Eindereden:
    ontbinding = Referentiedata(
        code="ONT",
        naam="Ontbinding",
    )
    """
    Een overeenkomst wordt of is beëindigd omdat de andere partij haar afspraken onder
    de overeenkomst niet nakomt.
    """

    opzegging = Referentiedata(
        code="OPZ",
        naam="Opzegging",
    )
    """
    Een overeenkomst wordt of is beëindigd omdat een van de partijen deze opzegt. Dit is
    alleen mogelijk bij bepaalde benoemde overeenkomsten, zoals een huurovereenkomst
    of een arbeidsovereenkomst.
    """

    vernietiging = Referentiedata(
        code="VER",
        naam="Vernietiging",
    )
    """
    Een overeenkomst wordt of is beëindigd (eventueel met terugwerkende kracht) omdat
    sprake is van een zogenaamd wilsgebrek (bedreiging, bedrog, dwaling, misbruik
    van omstandigheden)
    """
