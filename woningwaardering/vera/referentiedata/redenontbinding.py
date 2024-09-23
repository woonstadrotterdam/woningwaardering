from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Redenontbinding(Enum):
    niet_betaald = Referentiedata(
        code="BET",
        naam="Niet betaald",
    )
    """
    Het verschuldigde bedrag van de overeenkomst is niet voldaan.
    """

    wanprestatie = Referentiedata(
        code="WAN",
        naam="Wanprestatie",
    )
    """
    De overeenkomst wordt ontbonden omdat contractant tekortschiet in het nakomen van de
    afspraken.
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
