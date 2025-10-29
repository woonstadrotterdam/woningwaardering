from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class PrijscomponentsoortReferentiedata(Referentiedata):
    pass


class Prijscomponentsoort(Referentiedatasoort):
    dienstencomponent = PrijscomponentsoortReferentiedata(
        code="DIE",
        naam="Dienstencomponent",
    )
    """
    Let op: niet te verwarren met prijscomponentdetailsoort 'Dienst- en
    recreatieruimten'. Die laatste is een (subsidiabele) Servicekosten component.
    """

    eenmalig = PrijscomponentsoortReferentiedata(
        code="EEN",
        naam="Eenmalig",
    )
    """
    Eenmalige kosten, bijv. administratiekosten afsluiten huurovereenkomst
    """

    huuraanpassing = PrijscomponentsoortReferentiedata(
        code="HUA",
        naam="Huuraanpassing",
    )
    """
    Aanpassingen zoals, korting, compensatie, opslag, etc.
    """

    aankoopprijs = PrijscomponentsoortReferentiedata(
        code="KOO",
        naam="Aankoopprijs",
    )
    """
    Prijs van de aankoop
    """

    netto_huur = PrijscomponentsoortReferentiedata(
        code="NET",
        naam="Netto Huur",
    )
    """
    Netto huur, bijvoorbeeld de kale huur, of een andere prijscomponent (zie
    prijscomponentdetailsoorten) die tot de netto huur wordt gerekend.
    """

    parkeren = PrijscomponentsoortReferentiedata(
        code="PAR",
        naam="Parkeren",
    )
    """
    Prijscomponent voor een parkeergelegenheid als deze onlosmakelijk onderdeel uitmaakt
    van de huurovereenkomst voor een woongelegenheid. Let op: als de prijs voor
    parkeergelegenheid onderdeel is van de netto huur gebruik dan componentsoort
    Netto Huur in combinatie met een prijscomponentdetailsoort.
    """

    service = PrijscomponentsoortReferentiedata(
        code="SER",
        naam="Service",
    )
    """
    Aanvullende kosten zoals: huismeester, glasfonds, rioolreiniging, etc.
    """

    starterslening = PrijscomponentsoortReferentiedata(
        code="STA",
        naam="Starterslening",
    )

    verbruik = PrijscomponentsoortReferentiedata(
        code="VER",
        naam="Verbruik",
    )
    """
    Water, Warmte, Electriciteit, etc.
    """
