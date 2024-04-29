from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Uitvoerendesoort(Enum):
    leverancier = Referentiedata(
        code="LEV",
        naam="Leverancier",
    )
    """
    Uitvoering vindt plaats door een externe partij
    """

    vakgroep = Referentiedata(
        code="VAK",
        naam="Vakgroep",
    )
    """
    Uitvoering vindt plaats door een interne vakgroep / eigen dienst
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
