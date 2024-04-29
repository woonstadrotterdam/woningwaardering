from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Publicatiedetailstatus(Enum):
    woning_krijgt_andere_bestemming = Referentiedata(
        code="BES",
        naam="Woning krijgt andere bestemming",
        parent=Referentiedata(
            code="ING",
            naam="Ingetrokken",
        ),
    )
    """
    Woning krijgt andere bestemming.
    """

    geen_toewijzing = Referentiedata(
        code="GTW",
        naam="Geen toewijzing",
        parent=Referentiedata(
            code="AFG",
            naam="Afgerond",
        ),
    )
    """
    Geen toewijzing
    """

    woning_wordt_handmatig_bemiddeld = Referentiedata(
        code="HAN",
        naam="Woning wordt handmatig bemiddeld",
        parent=Referentiedata(
            code="ING",
            naam="Ingetrokken",
        ),
    )
    """
    Woning wordt handmatig bemiddeld.
    """

    verhuurd_onder_voorbehoud = Referentiedata(
        code="HUU",
        naam="Verhuurd onder voorbehoud",
        parent=Referentiedata(
            code="GEP",
            naam="Gepubliceerd",
        ),
    )
    """
    Verhuurd onder voorbehoud
    """

    huuropzegging_is_ingetrokken = Referentiedata(
        code="ING",
        naam="Huuropzegging is ingetrokken",
        parent=Referentiedata(
            code="ING",
            naam="Ingetrokken",
        ),
    )
    """
    Huuropzegging is ingetrokken.
    """

    verkocht_onder_voorbehoud = Referentiedata(
        code="KOO",
        naam="Verkocht onder voorbehoud",
        parent=Referentiedata(
            code="GEP",
            naam="Gepubliceerd",
        ),
    )
    """
    Verkocht onder voorbehoud
    """

    onder_bod = Referentiedata(
        code="OND",
        naam="Onder bod",
        parent=Referentiedata(
            code="GEP",
            naam="Gepubliceerd",
        ),
    )
    """
    Onder bod
    """

    publicatie_met_onjuiste_gegevens = Referentiedata(
        code="ONJ",
        naam="Publicatie met onjuiste gegevens",
        parent=Referentiedata(
            code="ING",
            naam="Ingetrokken",
        ),
    )
    """
    Publicatie met onjuiste gegevens.
    """

    onder_optie = Referentiedata(
        code="OOP",
        naam="Onder optie",
        parent=Referentiedata(
            code="GEP",
            naam="Gepubliceerd",
        ),
    )
    """
    Onder optie
    """

    woning_wordt_gerenoveerd = Referentiedata(
        code="REN",
        naam="Woning wordt gerenoveerd",
        parent=Referentiedata(
            code="ING",
            naam="Ingetrokken",
        ),
    )
    """
    Woning wordt gerenoveerd.
    """

    toegewezen = Referentiedata(
        code="TOE",
        naam="Toegewezen",
        parent=Referentiedata(
            code="AFG",
            naam="Afgerond",
        ),
    )
    """
    Toegewezen
    """

    woning_gaat_uit_exploitatie = Referentiedata(
        code="UIT",
        naam="Woning gaat uit exploitatie",
        parent=Referentiedata(
            code="ING",
            naam="Ingetrokken",
        ),
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
