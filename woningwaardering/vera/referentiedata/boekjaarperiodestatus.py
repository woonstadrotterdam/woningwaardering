from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Boekjaarperiodestatus(Enum):
    gesloten_periode = Referentiedata(
        code="GSP",
        naam="Gesloten periode",
    )
    """
    Periode waarin gegevens niet meer kunnen worden gewijzigd, tiegevoegd of verwijderd.
    """

    open_periode = Referentiedata(
        code="OPP",
        naam="Open periode",
    )
    """
    Periode waarin gegevens kunnen worden gewijzigd, tiegevoegd of verwijderd.
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
