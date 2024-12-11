from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class GrootboekmutatieherkomstReferentiedata(Referentiedata):
    pass


class Grootboekmutatieherkomst(Referentiedatasoort):
    activa_administratie = GrootboekmutatieherkomstReferentiedata(
        code="ACT",
        naam="Activa-administratie",
    )
    """
    Een boeking in de activa (sub-)administratie
    """

    batch = GrootboekmutatieherkomstReferentiedata(
        code="BAT",
        naam="Batch",
    )
    """
    Meest gebruikte betaalwijze waarbij een betaalbatch wordt gegenereerd dat
    elektronisch wordt verstuurd naar de bank
    """

    beginbalans = GrootboekmutatieherkomstReferentiedata(
        code="BEG",
        naam="Beginbalans",
    )
    """
    Een boeking van het eindsaldo van een balansrekening uit een voorgaand boekjaar
    """

    berekening = GrootboekmutatieherkomstReferentiedata(
        code="BER",
        naam="Berekening",
    )

    bank = GrootboekmutatieherkomstReferentiedata(
        code="BNK",
        naam="Bank",
    )
    """
    Een boeking in de bank (sub-)administratie
    """

    crediteuren = GrootboekmutatieherkomstReferentiedata(
        code="CRE",
        naam="Crediteuren",
    )
    """
    Een boeking van een schuld in de crediteuren (sub-)administratie
    """

    debiteuren = GrootboekmutatieherkomstReferentiedata(
        code="DEB",
        naam="Debiteuren",
    )
    """
    Een boeking van een vordering in de debiteuren (sub-)administratie
    """

    huuradministratie = GrootboekmutatieherkomstReferentiedata(
        code="HUU",
        naam="Huuradministratie",
    )
    """
    Een boeking in de huur (sub-)administratie
    """

    inkoopadministratie = GrootboekmutatieherkomstReferentiedata(
        code="INK",
        naam="Inkoopadministratie",
    )
    """
    Een boeking in de inkoop (sub-)administratie
    """

    kas = GrootboekmutatieherkomstReferentiedata(
        code="KAS",
        naam="Kas",
    )
    """
    Een boeking in de kas (sub-)administratie
    """

    leningenadministratie = GrootboekmutatieherkomstReferentiedata(
        code="LEN",
        naam="Leningenadministratie",
    )
    """
    Een boeking in de leningen (sub-)administratie
    """

    memoriaal = GrootboekmutatieherkomstReferentiedata(
        code="MEM",
        naam="Memoriaal",
    )
    """
    Overige handmatige boekingen die niet uit kas of bank voortkomen worden meestal
    geboekt onder de noemer memoriaal.
    """

    projectadministratie = GrootboekmutatieherkomstReferentiedata(
        code="PRO",
        naam="Projectadministratie",
    )
    """
    Een boeking in de project (sub-)administratie
    """

    salarisadministratie = GrootboekmutatieherkomstReferentiedata(
        code="SAL",
        naam="Salarisadministratie",
    )
    """
    Een boeking in de salaris (sub-)administratie
    """

    systeem = GrootboekmutatieherkomstReferentiedata(
        code="SYS",
        naam="Systeem",
    )
    """
    Overige (automatische) (correctie)boekingen
    """
