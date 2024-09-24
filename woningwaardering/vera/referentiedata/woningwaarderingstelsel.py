from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Woningwaarderingstelsel(Enum):
    onzelfstandige_woonruimten = Referentiedata(
        code="ONZ",
        naam="Onzelfstandige woonruimten",
    )
    """
    Het puntensysteem binnen het woningwaarderingstelsel dat van toepassing is voor
    onzelfstandig woonruimten
    """

    standplaatsen = Referentiedata(
        code="STA",
        naam="Standplaatsen",
    )
    """
    Het puntensysteem binnen het woningwaarderingstelsel dat van toepassing is voor
    standplaatsen
    """

    woonwagens = Referentiedata(
        code="WOO",
        naam="Woonwagens",
    )
    """
    Het puntensysteem binnen het woningwaarderingstelsel dat van toepassing is voor
    woonwagens
    """

    zelfstandige_woonruimten = Referentiedata(
        code="ZEL",
        naam="Zelfstandige woonruimten",
    )
    """
    Het puntensysteem binnen het woningwaarderingstelsel dat van toepassing is voor
    zelfstandig woonruimten
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
