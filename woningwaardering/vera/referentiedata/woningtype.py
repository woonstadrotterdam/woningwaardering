from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Woningtype(Enum):
    eengezinswoning = Referentiedata(
        code="EGW",
        naam="Eengezinswoning",
        parent=Referentiedata(
            code="WOO",
            naam="Woonruimte",
        ),
    )
    """
    Een woning die tevens een geheel pand vormt.
    """

    meergezinswoning = Referentiedata(
        code="MGW",
        naam="Meergezinswoning",
        parent=Referentiedata(
            code="WOO",
            naam="Woonruimte",
        ),
    )
    """
    Een woning die samen met andere woonruimten c.q. bedrijfsruimten een geheel pand
    vormt.
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
