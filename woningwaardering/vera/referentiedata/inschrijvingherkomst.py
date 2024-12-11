from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class InschrijvingherkomstReferentiedata(Referentiedata):
    pass


class Inschrijvingherkomst(Referentiedatasoort):
    heropend = InschrijvingherkomstReferentiedata(
        code="HER",
        naam="Heropend",
    )
    """
    De inschrijving is aangemaakt naar aanleiding van een heropening van een bestaande
    inschrijving.
    """

    medewerker = InschrijvingherkomstReferentiedata(
        code="MED",
        naam="Medewerker",
    )
    """
    De inschrijving is aangemaakt door een medewerker.
    """

    migratie = InschrijvingherkomstReferentiedata(
        code="MIG",
        naam="Migratie",
    )
    """
    De inschrijving is aangemaakt tijdens een migratie van gegevens.
    """

    gesplitst = InschrijvingherkomstReferentiedata(
        code="SPL",
        naam="Gesplitst",
    )
    """
    De inschrijving is aangemaakt naar aanleiding van een splitsing van een bestaande
    inschrijving waarbij de hoofd- en medeaanvrager een eigen inschrijving krijgen.
    """

    urgentie = InschrijvingherkomstReferentiedata(
        code="URG",
        naam="Urgentie",
    )
    """
    De inschrijving is aangemaakt naar aanleiding van het toekennen van een urgentie.
    """

    woningzoekende = InschrijvingherkomstReferentiedata(
        code="WOO",
        naam="Woningzoekende",
    )
    """
    De inschrijving is aangemaakt door de woningzoekende.
    """
