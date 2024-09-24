from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Inschrijvingherkomst(Enum):
    heropend = Referentiedata(
        code="HER",
        naam="Heropend",
    )
    """
    De inschrijving is aangemaakt naar aanleiding van een heropening van een bestaande
    inschrijving.
    """

    medewerker = Referentiedata(
        code="MED",
        naam="Medewerker",
    )
    """
    De inschrijving is aangemaakt door een medewerker.
    """

    migratie = Referentiedata(
        code="MIG",
        naam="Migratie",
    )
    """
    De inschrijving is aangemaakt tijdens een migratie van gegevens.
    """

    gesplitst = Referentiedata(
        code="SPL",
        naam="Gesplitst",
    )
    """
    De inschrijving is aangemaakt naar aanleiding van een splitsing van een bestaande
    inschrijving waarbij de hoofd- en medeaanvrager een eigen inschrijving krijgen.
    """

    urgentie = Referentiedata(
        code="URG",
        naam="Urgentie",
    )
    """
    De inschrijving is aangemaakt naar aanleiding van het toekennen van een urgentie.
    """

    woningzoekende = Referentiedata(
        code="WOO",
        naam="Woningzoekende",
    )
    """
    De inschrijving is aangemaakt door de woningzoekende.
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
