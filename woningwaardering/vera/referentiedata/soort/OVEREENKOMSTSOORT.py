
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class OVEREENKOMSTSOORT:

    arbeid = Referentiedata(
        code="ARB",
        naam="Arbeid",
    )
    # arbeid = ("ARB", "Arbeid")
    """
    Arbeidsovereenkomst
    """

    betalerovereenkomst = Referentiedata(
        code="BET",
        naam="Betalerovereenkomst",
    )
    # betalerovereenkomst = ("BET", "Betalerovereenkomst")
    """
    Overeenkomst waarin afspraken zijn vastgelegd met een afwijkende betaler voor een
    andere (huur-)overeenkomst
    """

    huurovereenkomst = Referentiedata(
        code="HUU",
        naam="Huurovereenkomst",
    )
    # huurovereenkomst = ("HUU", "Huurovereenkomst")
    """
    Overeenkomst met betrekking tot het huren van roerend of onroerend goed.
    """

    inhuur = Referentiedata(
        code="INH",
        naam="Inhuur",
    )
    # inhuur = ("INH", "Inhuur")
    """
    Inhuurovereenkomst
    """

    inschrijving = Referentiedata(
        code="INS",
        naam="Inschrijving",
    )
    # inschrijving = ("INS", "Inschrijving")
    """
    Overeenkomst met betrekking tot de registratie van een woningzoekende in een
    woonruimteverdeel gebied.
    """

    koopovereenkomst = Referentiedata(
        code="KOO",
        naam="Koopovereenkomst",
    )
    # koopovereenkomst = ("KOO", "Koopovereenkomst")
    """
    Overeenkomst met betrekking tot het kopen van roerend of onroerend goed.
    """

    lease = Referentiedata(
        code="LEA",
        naam="Lease",
    )
    # lease = ("LEA", "Lease")
    """
    Leaseovereenkomst
    """

    onderhoudsovereenkomst = Referentiedata(
        code="OND",
        naam="Onderhoudsovereenkomst",
    )
    # onderhoudsovereenkomst = ("OND", "Onderhoudsovereenkomst")
    """
    Overeenkomst met betrekking tot het onderhouden of beheren van roerend of onroerend
    goed.
    """

    serviceovereenkomst = Referentiedata(
        code="SER",
        naam="Serviceovereenkomst",
    )
    # serviceovereenkomst = ("SER", "Serviceovereenkomst")
    """
    Overeenkomst met betrekking tot (aanvullende) dienstverlening zoals glazenwassen,
    reparaties, groenverzorging. Ook de verschillende vormen van inschrijvingen of
    abonnementen vallen onder de soort Service overeenkomst.
    """
