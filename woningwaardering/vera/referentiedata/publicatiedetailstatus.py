from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.publicatiestatus import Publicatiestatus


class Publicatiedetailstatus(Enum):
    woning_krijgt_andere_bestemming = Referentiedata(
        code="BES",
        naam="Woning krijgt andere bestemming",
        parent=Publicatiestatus.ingetrokken.value,
    )
    """
    Woning krijgt andere bestemming.
    """

    geen_toewijzing = Referentiedata(
        code="GTW",
        naam="Geen toewijzing",
        parent=Publicatiestatus.afgerond.value,
    )
    """
    Geen toewijzing
    """

    woning_wordt_handmatig_bemiddeld = Referentiedata(
        code="HAN",
        naam="Woning wordt handmatig bemiddeld",
        parent=Publicatiestatus.ingetrokken.value,
    )
    """
    Woning wordt handmatig bemiddeld.
    """

    verhuurd_onder_voorbehoud = Referentiedata(
        code="HUU",
        naam="Verhuurd onder voorbehoud",
        parent=Publicatiestatus.gepubliceerd.value,
    )
    """
    Verhuurd onder voorbehoud
    """

    huuropzegging_is_ingetrokken = Referentiedata(
        code="ING",
        naam="Huuropzegging is ingetrokken",
        parent=Publicatiestatus.ingetrokken.value,
    )
    """
    Huuropzegging is ingetrokken.
    """

    verkocht_onder_voorbehoud = Referentiedata(
        code="KOO",
        naam="Verkocht onder voorbehoud",
        parent=Publicatiestatus.gepubliceerd.value,
    )
    """
    Verkocht onder voorbehoud
    """

    onder_bod = Referentiedata(
        code="OND",
        naam="Onder bod",
        parent=Publicatiestatus.gepubliceerd.value,
    )
    """
    Onder bod
    """

    publicatie_met_onjuiste_gegevens = Referentiedata(
        code="ONJ",
        naam="Publicatie met onjuiste gegevens",
        parent=Publicatiestatus.ingetrokken.value,
    )
    """
    Publicatie met onjuiste gegevens.
    """

    onder_optie = Referentiedata(
        code="OOP",
        naam="Onder optie",
        parent=Publicatiestatus.gepubliceerd.value,
    )
    """
    Onder optie
    """

    woning_wordt_gerenoveerd = Referentiedata(
        code="REN",
        naam="Woning wordt gerenoveerd",
        parent=Publicatiestatus.ingetrokken.value,
    )
    """
    Woning wordt gerenoveerd.
    """

    toegewezen = Referentiedata(
        code="TOE",
        naam="Toegewezen",
        parent=Publicatiestatus.afgerond.value,
    )
    """
    Toegewezen
    """

    woning_gaat_uit_exploitatie = Referentiedata(
        code="UIT",
        naam="Woning gaat uit exploitatie",
        parent=Publicatiestatus.ingetrokken.value,
    )
    """
    Woning gaat uit exploitatie.
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
