from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Contactgegevenstatus(Enum):
    aangemaakt = Referentiedata(
        code="AAN",
        naam="Aangemaakt",
    )
    """
    Het contactgegeven is aangemaakt.
    """

    gevalideerd = Referentiedata(
        code="GEV",
        naam="Gevalideerd",
    )
    """
    Het contactgeggeven is gevalideerd via een mail, sms etc.
    """

    ongeldig = Referentiedata(
        code="ONG",
        naam="Ongeldig",
    )
    """
    Het contactgegeven is niet (meer) geldig.
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
