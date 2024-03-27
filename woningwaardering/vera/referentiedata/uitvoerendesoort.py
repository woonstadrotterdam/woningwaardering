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
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
