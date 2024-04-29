from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Inkoopopdrachtregelsoort(Enum):
    initieel = Referentiedata(
        code="INI",
        naam="Initieel",
    )
    """
    De inkoopopdrachtregel betreft &#39;standaard&#39; overeengekomen werkzaamheden
    """

    meerwerk = Referentiedata(
        code="MEE",
        naam="Meerwerk",
    )
    """
    De inkoopopdrachtregel betreft meerwerk t.o.v. de initiële inkoopopdracht
    """

    minderwerk = Referentiedata(
        code="MIN",
        naam="Minderwerk",
    )
    """
    De inkoopopdrachtregel betreft minderwerk t.o.v. de initiële inkoopopdracht
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
