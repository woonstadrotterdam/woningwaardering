from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Pandsoort(Enum):
    eengezinswoning = Referentiedata(
        code="EGW",
        naam="Eengezinswoning",
    )
    """
    Een eengezinswoning is een zelfstandige woning die bedoeld is om door één huishouden
    bewoond te worden.
    """

    meergezinswoning = Referentiedata(
        code="MGW",
        naam="Meergezinswoning",
    )
    """
    Een meergezinswoning is een gebouw waarin meerdere zelfstandige wooneenheden,
    bedoeld voor bewoning door verschillende huishoudens, zijn ondergebracht.
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
