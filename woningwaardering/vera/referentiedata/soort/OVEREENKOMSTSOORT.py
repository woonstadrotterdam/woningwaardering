from woningwaardering.vera.bvg.models import Referentiedata


class OVEREENKOMSTSOORT:
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
