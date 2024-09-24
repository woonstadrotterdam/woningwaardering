from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Kandidaatstatus(Enum):
    aangeboden = Referentiedata(
        code="AAN",
        naam="Aangeboden",
    )
    """
    Kandidaat zit  in aanbiedingsproces.
    """

    afgewezen = Referentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    """
    Kandidaat is afgewezen door de aanbieder, corporatie, medebewoners etc.
    """

    geweigerd = Referentiedata(
        code="GEW",
        naam="Geweigerd",
    )
    """
    Kandidaat heeft de aanbieiding geweigerd.
    """

    potentiele_kandidaat = Referentiedata(
        code="POT",
        naam="Potentiele kandidaat",
    )
    """
    Kandidaat voldoet aan de spelregels van de publicatie.
    """

    gereageerd = Referentiedata(
        code="REA",
        naam="Gereageerd",
    )
    """
    Kandidaat heeft gereageerd op de publicatie.
    """

    geselecteerd = Referentiedata(
        code="SEL",
        naam="Geselecteerd",
    )
    """
    Kandidaat staat op vrijgegeven kandidatenlijst.
    """

    toegewezen = Referentiedata(
        code="TOE",
        naam="Toegewezen",
    )
    """
    Kandidaat is de toegewezen gebruiker van de eenheid.
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
