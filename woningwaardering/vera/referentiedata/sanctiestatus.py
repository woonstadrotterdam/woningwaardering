from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Sanctiestatus(Enum):
    aangemaakt = Referentiedata(
        code="AAN",
        naam="Aangemaakt",
    )
    """
    Aangemaakt
    """

    definitief = Referentiedata(
        code="DEF",
        naam="Definitief",
    )
    """
    Definitief (na 1e van de volgende kalendermaand)
    """

    ingetrokken = Referentiedata(
        code="ING",
        naam="Ingetrokken",
    )
    """
    Ingetrokken
    """

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
