
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class INSCHRIJVINGHERKOMST:

    heropend = Referentiedata(
        code="HER",
        naam="Heropend",
    )
    # heropend = ("HER", "Heropend")
    """
    De inschrijving is aangemaakt naar aanleiding van een heropening van een bestaande
    inschrijving.
    """

    medewerker = Referentiedata(
        code="MED",
        naam="Medewerker",
    )
    # medewerker = ("MED", "Medewerker")
    """
    De inschrijving is aangemaakt door een medewerker.
    """

    migratie = Referentiedata(
        code="MIG",
        naam="Migratie",
    )
    # migratie = ("MIG", "Migratie")
    """
    De inschrijving is aangemaakt tijdens een migratie van gegevens.
    """

    gesplitst = Referentiedata(
        code="SPL",
        naam="Gesplitst",
    )
    # gesplitst = ("SPL", "Gesplitst")
    """
    De inschrijving is aangemaakt naar aanleiding van een splitsing van een bestaande
    inschrijving waarbij de hoofd- en medeaanvrager een eigen inschrijving krijgen.
    """

    urgentie = Referentiedata(
        code="URG",
        naam="Urgentie",
    )
    # urgentie = ("URG", "Urgentie")
    """
    De inschrijving is aangemaakt naar aanleiding van het toekennen van een urgentie.
    """

    woningzoekende = Referentiedata(
        code="WOO",
        naam="Woningzoekende",
    )
    # woningzoekende = ("WOO", "Woningzoekende")
    """
    De inschrijving is aangemaakt door de woningzoekende.
    """
