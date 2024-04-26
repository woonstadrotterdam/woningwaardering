from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Afspraakverzoeksoort(Enum):
    eindinspectie = Referentiedata(
        code="EIN",
        naam="Eindinspectie",
    )
    """
    Verzoek voor het maken van een afspraak voor een eindinspectie naar aanleiding van
    de ontvangst van een huuropzegging.
    """

    voorinspectie = Referentiedata(
        code="VOO",
        naam="Voorinspectie",
    )
    """
    Verzoek voor het maken van een afspraak voor een voorinspectie naar aanleiding van
    de ontvangst van een huuropzegging.
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
