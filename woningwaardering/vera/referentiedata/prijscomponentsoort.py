from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Prijscomponentsoort(Enum):
    dienstencomponent = Referentiedata(
        code="DIE",
        naam="Dienstencomponent",
    )
    """
    Let op: niet te verwarren met prijscomponentdetailsoort 'Dienst- en
    recreatieruimten'. Die laatste is een (subsidiabele) Servicekosten component.
    """

    eenmalig = Referentiedata(
        code="EEN",
        naam="Eenmalig",
    )
    """
    Eenmalige kosten, bijv. administratiekosten afsluiten huurovereenkomst
    """

    huuraanpassing = Referentiedata(
        code="HUA",
        naam="Huuraanpassing",
    )
    """
    Aanpassingen zoals, korting, compensatie, opslag, etc.
    """

    aankoopprijs = Referentiedata(
        code="KOO",
        naam="Aankoopprijs",
    )
    """
    Prijs van de aankoop
    """

    netto_huur = Referentiedata(
        code="NET",
        naam="Netto Huur",
    )
    """
    Netto huur, bijvoorbeeld de kale huur, of een andere prijscomponent (zie
    prijscomponentdetailsoorten) die tot de netto huur wordt gerekend.
    """

    parkeren = Referentiedata(
        code="PAR",
        naam="Parkeren",
    )
    """
    Prijscomponent voor een parkeergelegenheid als deze onlosmakelijk onderdeel uitmaakt
    van de huurovereenkomst voor een woongelegenheid. Let op: als de prijs voor
    parkeergelegenheid onderdeel is van de netto huur gebruik dan componentsoort
    Netto Huur in combinatie met een prijscomponentdetailsoort.
    """

    service = Referentiedata(
        code="SER",
        naam="Service",
    )
    """
    Aanvullende kosten zoals: huismeester, glasfonds, rioolreiniging, etc.
    """

    starterslening = Referentiedata(
        code="STA",
        naam="Starterslening",
    )

    verbruik = Referentiedata(
        code="VER",
        naam="Verbruik",
    )
    """
    Water, Warmte, Electriciteit, etc.
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
