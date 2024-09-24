from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Boekingstatus(Enum):
    gefiatteerd = Referentiedata(
        code="FIA",
        naam="Gefiatteerd",
    )
    """
    Boeking is definitief en niet meer wijzigbaar.
    """

    historisch = Referentiedata(
        code="HIS",
        naam="Historisch",
    )
    """
    Boeking is onderdeel van een afgesloten administratieve periode of boekjaar.
    """

    voorlopig = Referentiedata(
        code="VRL",
        naam="Voorlopig",
    )
    """
    Boeking is niet definitief en kan worden gewijzigd of verwijderd.
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
