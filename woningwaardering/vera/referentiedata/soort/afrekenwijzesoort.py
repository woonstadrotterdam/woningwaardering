from vera.bvg.generated import Referentiedata


class Afrekenwijzesoort:
    afkoop = Referentiedata(
        code="AFK",
        naam="Afkoop",
    )
    """
    De onderhoudsorder wordt niet afgerekend omdat dit type onderhoud is afgekocht op
    totaalniveau
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
