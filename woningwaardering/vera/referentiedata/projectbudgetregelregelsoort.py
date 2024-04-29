from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Projectbudgetregelregelsoort(Enum):
    kostendetailregel = Referentiedata(
        code="KDT",
        naam="Kostendetailregel",
    )
    """
    Projectbudgetregel is een kostenregel binnen de stichtingskosten hiërarchie
    """

    opbrengstendetailregel = Referentiedata(
        code="ODT",
        naam="Opbrengstendetailregel",
    )
    """
    Projectbudgetregel is een opbrengstenregel binnen de stichtingskosten hiërarchie
    """

    subtotaalregel = Referentiedata(
        code="STR",
        naam="Subtotaalregel",
    )
    """
    Projectbudgetregel is een optelling van één of meer onderliggende kosten- of
    opbrengstenregels binnen de stichtingskosten hiërarchie
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
