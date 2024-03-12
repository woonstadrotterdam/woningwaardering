
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class DOELGROEP:

    persoon = Referentiedata(
        code="EEN",
        naam="Persoon",
    )
    # persoon = ("EEN", "Persoon")
    """
    Woonruimte is bestemd voor en/of huurder vormt een eenpersoonshuishouden
    """

    gezin = Referentiedata(
        code="GEZ",
        naam="Gezin",
    )
    # gezin = ("GEZ", "Gezin")
    """
    Leefverband van één of meer volwassenen die verantwoordelijkheid dragen voor de
    verzorging en opvoeding van één of meer kinderen.
    """

    huishouden_zonder_kinderen = Referentiedata(
        code="HZO",
        naam="Huishouden zonder kinderen",
    )
    # huishouden_zonder_kinderen = ("HZO", "Huishouden zonder kinderen")
    """
    Huishouden zonder kinderen - Eén of meerdere volwassen personen (tot een bepaald
    maximum leeftijd) die samen een huishouden vormen en (nog) geen kinderen verzorgen.
    """

    jongeren = Referentiedata(
        code="JON",
        naam="Jongeren",
    )
    # jongeren = ("JON", "Jongeren")
    """
    Woonruimte is bestemd voor en/of huurder heeft op het moment van toewijzing een
    specifieke maximum leeftijd
    """

    senioren = Referentiedata(
        code="SEN",
        naam="Senioren",
    )
    # senioren = ("SEN", "Senioren")
    """
    Woonruimte is bestemd voor en/of huurder heeft op het moment van toewijzing een
    specifieke minimum leeftijd
    """

    starter = Referentiedata(
        code="STA",
        naam="Starter",
    )
    # starter = ("STA", "Starter")
    """
    Woonruimte is bestemd voor en/of huurder betreft een starter op de woningmarkt
    """

    studenten = Referentiedata(
        code="STU",
        naam="Studenten",
    )
    # studenten = ("STU", "Studenten")
    """
    Woonruimte is bestemd voor en/of huurder is een student (ontvangt
    studiefinanciering, studeert voltijds of gaat promoveren).
    """

    zorg = Referentiedata(
        code="ZOR",
        naam="Zorg",
    )
    # zorg = ("ZOR", "Zorg")
    """
    Woonruimte is bestemd voor en/of huurder is een zorgbehoevende ((iemand die
    afhankelijk is van) woonruimte die naar aard en gebruik geen logische andere
    aanwendbaarheid kent dan een zorgwoning). Betreft o.a. aanleunwoningen en
    serviceflats.
    """
