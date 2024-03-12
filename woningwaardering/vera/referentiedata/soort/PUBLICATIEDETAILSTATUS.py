
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class PUBLICATIEDETAILSTATUS:

    woning_krijgt_andere_bestemming = Referentiedata(
        code="BES",
        naam="Woning krijgt andere bestemming",
    )
    # woning_krijgt_andere_bestemming = ("BES", "Woning krijgt andere bestemming")
    """
    Woning krijgt andere bestemming.
    """

    geen_toewijzing = Referentiedata(
        code="GTW",
        naam="Geen toewijzing",
    )
    # geen_toewijzing = ("GTW", "Geen toewijzing")
    """
    Geen toewijzing
    """

    woning_wordt_handmatig_bemiddeld = Referentiedata(
        code="HAN",
        naam="Woning wordt handmatig bemiddeld",
    )
    # woning_wordt_handmatig_bemiddeld = ("HAN", "Woning wordt handmatig bemiddeld")
    """
    Woning wordt handmatig bemiddeld.
    """

    verhuurd_onder_voorbehoud = Referentiedata(
        code="HUU",
        naam="Verhuurd onder voorbehoud",
    )
    # verhuurd_onder_voorbehoud = ("HUU", "Verhuurd onder voorbehoud")
    """
    Verhuurd onder voorbehoud
    """

    huuropzegging_is_ingetrokken = Referentiedata(
        code="ING",
        naam="Huuropzegging is ingetrokken",
    )
    # huuropzegging_is_ingetrokken = ("ING", "Huuropzegging is ingetrokken")
    """
    Huuropzegging is ingetrokken.
    """

    verkocht_onder_voorbehoud = Referentiedata(
        code="KOO",
        naam="Verkocht onder voorbehoud",
    )
    # verkocht_onder_voorbehoud = ("KOO", "Verkocht onder voorbehoud")
    """
    Verkocht onder voorbehoud
    """

    onder_bod = Referentiedata(
        code="OND",
        naam="Onder bod",
    )
    # onder_bod = ("OND", "Onder bod")
    """
    Onder bod
    """

    publicatie_met_onjuiste_gegevens = Referentiedata(
        code="ONJ",
        naam="Publicatie met onjuiste gegevens",
    )
    # publicatie_met_onjuiste_gegevens = ("ONJ", "Publicatie met onjuiste gegevens")
    """
    Publicatie met onjuiste gegevens.
    """

    onder_optie = Referentiedata(
        code="OOP",
        naam="Onder optie",
    )
    # onder_optie = ("OOP", "Onder optie")
    """
    Onder optie
    """

    woning_wordt_gerenoveerd = Referentiedata(
        code="REN",
        naam="Woning wordt gerenoveerd",
    )
    # woning_wordt_gerenoveerd = ("REN", "Woning wordt gerenoveerd")
    """
    Woning wordt gerenoveerd.
    """

    toegewezen = Referentiedata(
        code="TOE",
        naam="Toegewezen",
    )
    # toegewezen = ("TOE", "Toegewezen")
    """
    Toegewezen
    """

    woning_gaat_uit_exploitatie = Referentiedata(
        code="UIT",
        naam="Woning gaat uit exploitatie",
    )
    # woning_gaat_uit_exploitatie = ("UIT", "Woning gaat uit exploitatie")
    """
    Woning gaat uit exploitatie.
    """
