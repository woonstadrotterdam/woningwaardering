from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Begrotingversie(Enum):
    actueel_budget = Referentiedata(
        code="ACB",
        naam="Actueel budget",
    )
    """
    Som van mutatie en oorspronkelijk budget van een budgetregel voor een jaar of
    periode.
    """

    mutatie_budget = Referentiedata(
        code="MUB",
        naam="Mutatie budget",
    )
    """
    Gewijzigd bedrag van een budgetregel voor een jaar of periode.
    """

    oorspronkelijk_budget = Referentiedata(
        code="OOB",
        naam="Oorspronkelijk budget",
    )
    """
    Oorspronkelijk bedrag van een budgetregel voor een jaar of een periode.
    """

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
