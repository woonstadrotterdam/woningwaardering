from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Medewerkerrol(Enum):
    bhv_er = Referentiedata(
        code="BHV",
        naam="BHV-er",
    )

    scrummaster = Referentiedata(
        code="SCR",
        naam="Scrummaster",
    )

    vertrouwenspersoon = Referentiedata(
        code="VER",
        naam="Vertrouwenspersoon",
    )

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
