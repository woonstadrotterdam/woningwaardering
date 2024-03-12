
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class PRIJSCOMPONENTSOORT:

    dienstencomponent = Referentiedata(
        code="DIE",
        naam="Dienstencomponent",
    )
    # dienstencomponent = ("DIE", "Dienstencomponent")
    """
    Let op: niet te verwarren met prijscomponentdetailsoort 'Dienst- en
    recreatieruimten'. Die laatste is een (subsidiabele) Servicekosten component.
    """

    eenmalig = Referentiedata(
        code="EEN",
        naam="Eenmalig",
    )
    # eenmalig = ("EEN", "Eenmalig")
    """
    Eenmalige kosten, bijv. administratiekosten afsluiten huurovereenkomst
    """

    huuraanpassing = Referentiedata(
        code="HUA",
        naam="Huuraanpassing",
    )
    # huuraanpassing = ("HUA", "Huuraanpassing")
    """
    Aanpassingen zoals, korting, compensatie, opslag, etc.
    """

    aankoopprijs = Referentiedata(
        code="KOO",
        naam="Aankoopprijs",
    )
    # aankoopprijs = ("KOO", "Aankoopprijs")
    """
    Prijs van de aankoop
    """

    netto_huur = Referentiedata(
        code="NET",
        naam="Netto Huur",
    )
    # netto_huur = ("NET", "Netto Huur")
    """
    Netto huur, bijvoorbeeld de kale huur, of een andere prijscomponent (zie
    prijscomponentdetailsoorten) die tot de netto huur wordt gerekend.
    """

    parkeren = Referentiedata(
        code="PAR",
        naam="Parkeren",
    )
    # parkeren = ("PAR", "Parkeren")
    """
    Prijscomponent voor een parkeergelegenheid, als deze onlosmakelijk onderdeel
    uitmaakt van de huurovereenkomst voor een woongelegenheid. Let op: als de prijs voor
    parkeergelegenheid onderdeel is van de netto huur, gebruik dan componentsoort Netto
    Huur in combinatie met een prijscomponentdetailsoort.
    """

    service = Referentiedata(
        code="SER",
        naam="Service",
    )
    # service = ("SER", "Service")
    """
    Aanvullende kosten zoals: huismeester, glasfonds, rioolreiniging, etc.
    """

    starterslening = Referentiedata(
        code="STA",
        naam="Starterslening",
    )
    # starterslening = ("STA", "Starterslening")

    verbruik = Referentiedata(
        code="VER",
        naam="Verbruik",
    )
    # verbruik = ("VER", "Verbruik")
    """
    Water, Warmte, Electriciteit, etc.
    """
