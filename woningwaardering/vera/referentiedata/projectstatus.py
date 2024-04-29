from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Projectstatus(Enum):
    actief = Referentiedata(
        code="ACT",
        naam="Actief",
    )
    """
    Het project is actief, en bevindt zich in een van de projectfasen
    """

    afgerond = Referentiedata(
        code="AFG",
        naam="Afgerond",
    )
    """
    Het project is afgerond, en bevindt zich niet meer in een van de projectfasen
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
