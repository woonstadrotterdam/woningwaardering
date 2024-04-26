from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Woonsituatiesoort(Enum):
    doorstromer = Referentiedata(
        code="DOO",
        naam="Doorstromer",
    )
    """
    Een doorstromer is een woningzoekende die een zelfstandige woning achterlaat.
    """

    starter = Referentiedata(
        code="STA",
        naam="Starter",
    )
    """
    Een woningzoekende die geen zelfstandige woning achterlaat. Bijvoorbeeld omdat deze
    nog thuis of in een onzelfstandige woning woont, of dat men gaat scheiden.
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
