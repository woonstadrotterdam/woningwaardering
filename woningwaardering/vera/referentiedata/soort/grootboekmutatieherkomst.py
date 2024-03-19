from vera.referentiedata.models import Referentiedata


class Grootboekmutatieherkomst:
    activa_administratie = Referentiedata(
        code="ACT",
        naam="Activa-administratie",
    )
    """
    Een boeking in de activa (sub-)administratie
    """

    batch = Referentiedata(
        code="BAT",
        naam="Batch",
    )
    """
    Meest gebruikte betaalwijze waarbij een betaalbatch wordt gegenereerd dat
    elektronisch wordt verstuurd naar de bank
    """

    berekening = Referentiedata(
        code="BER",
        naam="Berekening",
    )

    bank = Referentiedata(
        code="BNK",
        naam="Bank",
    )
    """
    Een boeking in de bank (sub-)administratie
    """

    crediteuren = Referentiedata(
        code="CRE",
        naam="Crediteuren",
    )
    """
    Een boeking van een schuld in de crediteuren (sub-)administratie
    """

    debiteuren = Referentiedata(
        code="DEB",
        naam="Debiteuren",
    )
    """
    Een boeking van een vordering in de debiteuren (sub-)administratie
    """

    huuradministratie = Referentiedata(
        code="HUU",
        naam="Huuradministratie",
    )
    """
    Een boeking in de huur (sub-)administratie
    """

    inkoopadministratie = Referentiedata(
        code="INK",
        naam="Inkoopadministratie",
    )
    """
    Een boeking in de inkoop (sub-)administratie
    """

    kas = Referentiedata(
        code="KAS",
        naam="Kas",
    )
    """
    Een boeking in de kas (sub-)administratie
    """

    leningenadministratie = Referentiedata(
        code="LEN",
        naam="Leningenadministratie",
    )
    """
    Een boeking in de leningen (sub-)administratie
    """

    memoriaal = Referentiedata(
        code="MEM",
        naam="Memoriaal",
    )
    """
    Overige handmatige boekingen die niet uit kas of bank voortkomen worden meestal
    geboekt onder de noemer memoriaal.
    """

    projectadministratie = Referentiedata(
        code="PRO",
        naam="Projectadministratie",
    )
    """
    Een boeking in de project (sub-)administratie
    """

    salarisadministratie = Referentiedata(
        code="SAL",
        naam="Salarisadministratie",
    )
    """
    Een boeking in de salaris (sub-)administratie
    """

    systeem = Referentiedata(
        code="SYS",
        naam="Systeem",
    )
    """
    Overige (automatische) (correctie)boekingen
    """
