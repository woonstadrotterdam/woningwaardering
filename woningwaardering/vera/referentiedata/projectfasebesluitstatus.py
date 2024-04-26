from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Projectfasebesluitstatus(Enum):
    afgewezen = Referentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    """
    Projectfasebesluit (-versie) is afgewezen
    """

    aangeboden_ter_goedkeuring = Referentiedata(
        code="ATG",
        naam="Aangeboden ter goedkeuring",
    )
    """
    Projectfasebesluit wacht op goedkeuring, is in behandeling
    """

    concept = Referentiedata(
        code="CON",
        naam="Concept",
    )
    """
    Projectfasebesluit(-versie) in concept
    """

    definitief = Referentiedata(
        code="DEF",
        naam="Definitief",
    )
    """
    Projectfasebesluit definitief maar nog niet ter goedkeuring aangeboden
    """

    goedgekeurd = Referentiedata(
        code="GOE",
        naam="Goedgekeurd",
    )
    """
    Projectfasebesluit is formeel goedgekeurd
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
