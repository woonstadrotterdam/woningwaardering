from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Afrekenwijzesoort(Enum):
    afkoop = Referentiedata(
        code="AFK",
        naam="Afkoop",
    )
    """
    De onderhoudsorder wordt niet afgerekend omdat dit type onderhoud is afgekocht op
    totaalniveau.
    """

    garantie = Referentiedata(
        code="GAR",
        naam="Garantie",
    )
    """
    De onderhoudsorder wordt niet afgerekend omdat de werkzaamheden onder garantie
    vallen
    """

    nacalculatie_eenheidsprijzen = Referentiedata(
        code="NCE",
        naam="Nacalculatie eenheidsprijzen",
    )
    """
    De onderhoudsorder wordt afgerekend op basis van aantal eenheden x eenheidsrpijs.
    Bij bestedingsoort kan hier gebruik gemaakt worden van de soort Vaste taakprijs
    """

    nacalculatie_regie = Referentiedata(
        code="NCR",
        naam="Nacalculatie regie",
    )
    """
    De onderhoudsorder wordt afgerekend op basis van de werkelijke bestedingen
    (arbeidstijd, reistijd, materiaal)
    """

    vaste_prijs = Referentiedata(
        code="VPR",
        naam="Vaste prijs",
    )
    """
    De onderhoudsorder wordt afgerekend op basis van een vaste (totaal-)prijs
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
