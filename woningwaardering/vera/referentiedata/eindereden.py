from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Eindereden(Enum):
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

    @property
    def code(self) -> str:
        if self.value.code is None:
            raise TypeError("de code van een Referentiedata object mag niet None zijn")
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
