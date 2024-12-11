from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class AfrekenwijzesoortReferentiedata(Referentiedata):
    pass


class Afrekenwijzesoort(Referentiedatasoort):
    afkoop = AfrekenwijzesoortReferentiedata(
        code="AFK",
        naam="Afkoop",
    )
    """
    De onderhoudsorder wordt niet afgerekend omdat dit type onderhoud is afgekocht op
    totaalniveau.
    """

    garantie = AfrekenwijzesoortReferentiedata(
        code="GAR",
        naam="Garantie",
    )
    """
    De onderhoudsorder wordt niet afgerekend omdat de werkzaamheden onder garantie
    vallen
    """

    nacalculatie_eenheidsprijzen = AfrekenwijzesoortReferentiedata(
        code="NCE",
        naam="Nacalculatie eenheidsprijzen",
    )
    """
    De onderhoudsorder wordt afgerekend op basis van aantal eenheden x eenheidsrpijs.
    Bij bestedingsoort kan hier gebruik gemaakt worden van de soort Vaste taakprijs
    """

    nacalculatie_regie = AfrekenwijzesoortReferentiedata(
        code="NCR",
        naam="Nacalculatie regie",
    )
    """
    De onderhoudsorder wordt afgerekend op basis van de werkelijke bestedingen
    (arbeidstijd, reistijd, materiaal)
    """

    vaste_prijs = AfrekenwijzesoortReferentiedata(
        code="VPR",
        naam="Vaste prijs",
    )
    """
    De onderhoudsorder wordt afgerekend op basis van een vaste (totaal-)prijs
    """
