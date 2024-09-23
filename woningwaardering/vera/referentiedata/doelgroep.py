from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Doelgroep(Enum):
    persoon = Referentiedata(
        code="EEN",
        naam="Persoon",
    )
    """
    Woonruimte is bestemd voor en/of huurder vormt een eenpersoonshuishouden
    """

    gezin = Referentiedata(
        code="GEZ",
        naam="Gezin",
    )
    """
    Leefverband van één of meer volwassenen die verantwoordelijkheid dragen voor de
    verzorging en opvoeding van één of meer kinderen.
    """

    huishouden_zonder_kinderen = Referentiedata(
        code="HZO",
        naam="Huishouden zonder kinderen",
    )
    """
    Huishouden zonder kinderen - Eén of meerdere volwassen personen (tot een bepaald
    maximum leeftijd) die samen een huishouden vormen en (nog) geen kinderen
    verzorgen.
    """

    jongeren = Referentiedata(
        code="JON",
        naam="Jongeren",
    )
    """
    Woonruimte is bestemd voor en/of huurder heeft op het moment van toewijzing een
    specifieke maximum leeftijd
    """

    senioren = Referentiedata(
        code="SEN",
        naam="Senioren",
    )
    """
    Woonruimte is bestemd voor en/of huurder heeft op het moment van toewijzing een
    specifieke minimum leeftijd
    """

    starter = Referentiedata(
        code="STA",
        naam="Starter",
    )
    """
    Woonruimte is bestemd voor en/of huurder betreft een starter op de woningmarkt
    """

    studenten = Referentiedata(
        code="STU",
        naam="Studenten",
    )
    """
    Woonruimte is bestemd voor en/of huurder is een student (ontvangt
    studiefinanciering, studeert voltijds of gaat promoveren).
    """

    zorg = Referentiedata(
        code="ZOR",
        naam="Zorg",
    )
    """
    Woonruimte is bestemd voor en/of huurder is een zorgbehoevende ((iemand die
    afhankelijk is van) woonruimte die naar aard en gebruik geen logische andere
    aanwendbaarheid kent dan een zorgwoning). Betreft o.a. aanleunwoningen en
    serviceflats.
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
