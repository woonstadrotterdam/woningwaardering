
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class GROOTBOEKMUTATIEHERKOMST:

    activa_administratie = Referentiedata(
        code="ACT",
        naam="Activa-administratie",
    )
    # activa_administratie = ("ACT", "Activa-administratie")
    """
    Een boeking in de activa (sub-)administratie
    """

    batch = Referentiedata(
        code="BAT",
        naam="Batch",
    )
    # batch = ("BAT", "Batch")
    """
    Meest gebruikte betaalwijze waarbij een betaalbatch wordt gegenereerd dat
    elektronisch wordt verstuurd naar de bank
    """

    berekening = Referentiedata(
        code="BER",
        naam="Berekening",
    )
    # berekening = ("BER", "Berekening")

    bank = Referentiedata(
        code="BNK",
        naam="Bank",
    )
    # bank = ("BNK", "Bank")
    """
    Een boeking in de bank (sub-)administratie
    """

    crediteuren = Referentiedata(
        code="CRE",
        naam="Crediteuren",
    )
    # crediteuren = ("CRE", "Crediteuren")
    """
    Een boeking van een schuld in de crediteuren (sub-)administratie
    """

    debiteuren = Referentiedata(
        code="DEB",
        naam="Debiteuren",
    )
    # debiteuren = ("DEB", "Debiteuren")
    """
    Een boeking van een vordering in de debiteuren (sub-)administratie
    """

    huuradministratie = Referentiedata(
        code="HUU",
        naam="Huuradministratie",
    )
    # huuradministratie = ("HUU", "Huuradministratie")
    """
    Een boeking in de huur (sub-)administratie
    """

    inkoopadministratie = Referentiedata(
        code="INK",
        naam="Inkoopadministratie",
    )
    # inkoopadministratie = ("INK", "Inkoopadministratie")
    """
    Een boeking in de inkoop (sub-)administratie
    """

    kas = Referentiedata(
        code="KAS",
        naam="Kas",
    )
    # kas = ("KAS", "Kas")
    """
    Een boeking in de kas (sub-)administratie
    """

    leningenadministratie = Referentiedata(
        code="LEN",
        naam="Leningenadministratie",
    )
    # leningenadministratie = ("LEN", "Leningenadministratie")
    """
    Een boeking in de leningen (sub-)administratie
    """

    memoriaal = Referentiedata(
        code="MEM",
        naam="Memoriaal",
    )
    # memoriaal = ("MEM", "Memoriaal")
    """
    Overige handmatige boekingen die niet uit kas of bank voortkomen worden meestal
    geboekt onder de noemer memoriaal.
    """

    projectadministratie = Referentiedata(
        code="PRO",
        naam="Projectadministratie",
    )
    # projectadministratie = ("PRO", "Projectadministratie")
    """
    Een boeking in de project (sub-)administratie
    """

    salarisadministratie = Referentiedata(
        code="SAL",
        naam="Salarisadministratie",
    )
    # salarisadministratie = ("SAL", "Salarisadministratie")
    """
    Een boeking in de salaris (sub-)administratie
    """

    systeem = Referentiedata(
        code="SYS",
        naam="Systeem",
    )
    # systeem = ("SYS", "Systeem")
    """
    Overige (automatische) (correctie)boekingen
    """
