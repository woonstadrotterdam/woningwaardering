
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class OVEREENKOMSTSTATUS:

    beeindigd = Referentiedata(
        code="BEE",
        naam="Beeindigd",
    )
    # beeindigd = ("BEE", "Beeindigd")
    """
    De einddatum van de overeenkomst is verstreken en deze is daadwerkelijk beeindigd.
    """

    geannuleerd = Referentiedata(
        code="GEA",
        naam="Geannuleerd",
    )
    # geannuleerd = ("GEA", "Geannuleerd")
    """
    De partijen hebben afgesproken dat de huurovereenkomst toch niet definitief gemaakt
    wordt. Deze status kan alleen ontstaan wanneer de overeenkomst de status Voorlopig
    of Goedgekeurd heeft. Wanneer een overeenkomst actief is zal deze opgezegd,
    ontbonden of vernietigd moeten worden.
    """

    goedgekeurd = Referentiedata(
        code="GOE",
        naam="Goedgekeurd",
    )
    # goedgekeurd = ("GOE", "Goedgekeurd")
    """
    De overeenkomst is goedgekeurd door de verhuurder en wacht op een handtekening van
    de huurder.
    """

    lopend = Referentiedata(
        code="LOP",
        naam="Lopend",
    )
    # lopend = ("LOP", "Lopend")
    """
    De overeenkomst is getekend en loopt tot de vastgestelde einddatum of volgens de
    specifieke voorwaarden van de overeenkomst
    """

    ontbonden = Referentiedata(
        code="ONT",
        naam="Ontbonden",
    )
    # ontbonden = ("ONT", "Ontbonden")
    """
    De aanduiding dat de overeenkomst voor de einddatum is ontbonden en niet door een
    natuurlijke weg is beëindigd. Ontbonden vanwege contractbreuk, -fraude.
    """

    opgezegd = Referentiedata(
        code="OPG",
        naam="Opgezegd",
    )
    # opgezegd = ("OPG", "Opgezegd")
    """
    De overeenkomst is daadwerkelijk opgezegd en een einddatum van de overeenkomst is
    vastgelegd.
    """

    vernietigd = Referentiedata(
        code="VER",
        naam="Vernietigd",
    )
    # vernietigd = ("VER", "Vernietigd")
    """
    De aanduiding dat de overeenkomst is vernietigd en niet door een natuurlijke weg is
    beëindigd. Het contract is niet geldig tot stand gekomen vanwege wilsgebrek of
    nietig verklaard vanwege handelsonbevoegdheid of –onbekwaamheid.
    """

    voorlopig = Referentiedata(
        code="VOO",
        naam="Voorlopig",
    )
    # voorlopig = ("VOO", "Voorlopig")
    """
    De overeenkomst is nog voorlopig en moet goedgekeurd worden door de verhuurder en
    huurder voordat deze definitief is. Bij een voorlopige overeenkomst moeten
    bijvoorbeeld nog bewijsstukken aangeleverd worden.
    """

    voorlopig_opgezegd = Referentiedata(
        code="VOP",
        naam="Voorlopig opgezegd",
    )
    # voorlopig_opgezegd = ("VOP", "Voorlopig opgezegd")
    """
    De overeenkomst is opgezegd door de huurder maar is nog wel actief en de opzegging
    is ook nog niet definitief gemaakt.
    """
