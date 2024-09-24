from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Reclamatiesoort(Enum):
    bezwaar = Referentiedata(
        code="BEZ",
        naam="Bezwaar",
    )
    """
    Een ingediend bezwaar over de uitvoering van de corporatie van het
    woonruimteverdeelproces.
    """

    klacht = Referentiedata(
        code="KLA",
        naam="Klacht",
    )
    """
    Een klacht over de uitvoering van de corporatie van het woonruimteverdeelproces.
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
