from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Overeenkomstsoort(Enum):
    arbeid = Referentiedata(
        code="ARB",
        naam="Arbeid",
    )
    """
    Arbeidsovereenkomst
    """

    betalerovereenkomst = Referentiedata(
        code="BET",
        naam="Betalerovereenkomst",
    )
    """
    Overeenkomst waarin afspraken zijn vastgelegd met een afwijkende betaler voor een
    andere (huur-)overeenkomst
    """

    huurovereenkomst = Referentiedata(
        code="HUU",
        naam="Huurovereenkomst",
    )
    """
    Overeenkomst met betrekking tot het huren van roerend of onroerend goed.
    """

    inhuur = Referentiedata(
        code="INH",
        naam="Inhuur",
    )
    """
    Inhuurovereenkomst
    """

    inschrijving = Referentiedata(
        code="INS",
        naam="Inschrijving",
    )
    """
    Overeenkomst met betrekking tot de registratie van een woningzoekende in een
    woonruimteverdeel gebied.
    """

    koopovereenkomst = Referentiedata(
        code="KOO",
        naam="Koopovereenkomst",
    )
    """
    Overeenkomst met betrekking tot het kopen van roerend of onroerend goed.
    """

    lease = Referentiedata(
        code="LEA",
        naam="Lease",
    )
    """
    Leaseovereenkomst
    """

    onderhoudsovereenkomst = Referentiedata(
        code="OND",
        naam="Onderhoudsovereenkomst",
    )
    """
    Overeenkomst met betrekking tot het onderhouden of beheren van roerend of onroerend
    goed.
    """

    serviceovereenkomst = Referentiedata(
        code="SER",
        naam="Serviceovereenkomst",
    )
    """
    Overeenkomst met betrekking tot (aanvullende) dienstverlening zoals glazenwassen,
    reparaties, groenverzorging. Ook de verschillende vormen van inschrijvingen of
    abonnementen vallen onder de soort Service overeenkomst.
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
