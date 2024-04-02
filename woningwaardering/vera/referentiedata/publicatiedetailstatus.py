from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Publicatiedetailstatus(Enum):
    woning_krijgt_andere_bestemming = Referentiedata(
        code="BES",
        naam="Woning krijgt andere bestemming",
    )
    """
    Woning krijgt andere bestemming.
    """

    geen_toewijzing = Referentiedata(
        code="GTW",
        naam="Geen toewijzing",
    )
    """
    Geen toewijzing
    """

    woning_wordt_handmatig_bemiddeld = Referentiedata(
        code="HAN",
        naam="Woning wordt handmatig bemiddeld",
    )
    """
    Woning wordt handmatig bemiddeld.
    """

    verhuurd_onder_voorbehoud = Referentiedata(
        code="HUU",
        naam="Verhuurd onder voorbehoud",
    )
    """
    Verhuurd onder voorbehoud
    """

    huuropzegging_is_ingetrokken = Referentiedata(
        code="ING",
        naam="Huuropzegging is ingetrokken",
    )
    """
    Huuropzegging is ingetrokken.
    """

    verkocht_onder_voorbehoud = Referentiedata(
        code="KOO",
        naam="Verkocht onder voorbehoud",
    )
    """
    Verkocht onder voorbehoud
    """

    onder_bod = Referentiedata(
        code="OND",
        naam="Onder bod",
    )
    """
    Onder bod
    """

    publicatie_met_onjuiste_gegevens = Referentiedata(
        code="ONJ",
        naam="Publicatie met onjuiste gegevens",
    )
    """
    Publicatie met onjuiste gegevens.
    """

    onder_optie = Referentiedata(
        code="OOP",
        naam="Onder optie",
    )
    """
    Onder optie
    """

    woning_wordt_gerenoveerd = Referentiedata(
        code="REN",
        naam="Woning wordt gerenoveerd",
    )
    """
    Woning wordt gerenoveerd.
    """

    toegewezen = Referentiedata(
        code="TOE",
        naam="Toegewezen",
    )
    """
    Toegewezen
    """

    woning_gaat_uit_exploitatie = Referentiedata(
        code="UIT",
        naam="Woning gaat uit exploitatie",
    )
    """
    Woning gaat uit exploitatie.
    """

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
