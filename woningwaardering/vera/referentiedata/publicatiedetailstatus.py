from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.publicatiestatus import Publicatiestatus
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Publicatiedetailstatus(Referentiedatasoort):
    woning_krijgt_andere_bestemming = Referentiedata(
        code="BES",
        naam="Woning krijgt andere bestemming",
        parent=Publicatiestatus.ingetrokken,
    )
    """
    Woning krijgt andere bestemming.
    """

    geen_toewijzing = Referentiedata(
        code="GTW",
        naam="Geen toewijzing",
        parent=Publicatiestatus.afgerond,
    )
    """
    Geen toewijzing
    """

    woning_wordt_handmatig_bemiddeld = Referentiedata(
        code="HAN",
        naam="Woning wordt handmatig bemiddeld",
        parent=Publicatiestatus.ingetrokken,
    )
    """
    Woning wordt handmatig bemiddeld.
    """

    verhuurd_onder_voorbehoud = Referentiedata(
        code="HUU",
        naam="Verhuurd onder voorbehoud",
        parent=Publicatiestatus.gepubliceerd,
    )
    """
    Verhuurd onder voorbehoud
    """

    huuropzegging_is_ingetrokken = Referentiedata(
        code="ING",
        naam="Huuropzegging is ingetrokken",
        parent=Publicatiestatus.ingetrokken,
    )
    """
    Huuropzegging is ingetrokken.
    """

    verkocht_onder_voorbehoud = Referentiedata(
        code="KOO",
        naam="Verkocht onder voorbehoud",
        parent=Publicatiestatus.gepubliceerd,
    )
    """
    Verkocht onder voorbehoud
    """

    onder_bod = Referentiedata(
        code="OND",
        naam="Onder bod",
        parent=Publicatiestatus.gepubliceerd,
    )
    """
    Onder bod
    """

    publicatie_met_onjuiste_gegevens = Referentiedata(
        code="ONJ",
        naam="Publicatie met onjuiste gegevens",
        parent=Publicatiestatus.ingetrokken,
    )
    """
    Publicatie met onjuiste gegevens.
    """

    onder_optie = Referentiedata(
        code="OOP",
        naam="Onder optie",
        parent=Publicatiestatus.gepubliceerd,
    )
    """
    Onder optie
    """

    woning_wordt_gerenoveerd = Referentiedata(
        code="REN",
        naam="Woning wordt gerenoveerd",
        parent=Publicatiestatus.ingetrokken,
    )
    """
    Woning wordt gerenoveerd.
    """

    toegewezen = Referentiedata(
        code="TOE",
        naam="Toegewezen",
        parent=Publicatiestatus.afgerond,
    )
    """
    Toegewezen
    """

    woning_gaat_uit_exploitatie = Referentiedata(
        code="UIT",
        naam="Woning gaat uit exploitatie",
        parent=Publicatiestatus.ingetrokken,
    )
    """
    Woning gaat uit exploitatie.
    """
