
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class EINDEREDEN:

    ontbinding = Referentiedata(
        code="ONT",
        naam="Ontbinding",
    )
    # ontbinding = ("ONT", "Ontbinding")
    """
    Een overeenkomst wordt of is beëindigd omdat de andere partij haar afspraken onder
    de overeenkomst niet nakomt.
    """

    opzegging = Referentiedata(
        code="OPZ",
        naam="Opzegging",
    )
    # opzegging = ("OPZ", "Opzegging")
    """
    Een overeenkomst wordt of is beëindigd omdat een van de partijen deze opzegt. Dit is
    alleen mogelijk bij bepaalde benoemde overeenkomsten, zoals een huurovereenkomst of
    een arbeidsovereenkomst.
    """

    vernietiging = Referentiedata(
        code="VER",
        naam="Vernietiging",
    )
    # vernietiging = ("VER", "Vernietiging")
    """
    Een overeenkomst wordt of is beëindigd (eventueel met terugwerkende kracht) omdat
    sprake is van een zogenaamd wilsgebrek (bedreiging, bedrog, dwaling, misbruik van
    omstandigheden)
    """
