from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Redenvernietiging(Enum):
    bedreiging = Referentiedata(
        code="DRE",
        naam="Bedreiging",
    )
    """
    De overeenkomst is nietig aangezien deze tot stand is gekomen onder bedreiging.
    """

    bedrog = Referentiedata(
        code="DRO",
        naam="Bedrog",
    )
    """
    De overeenkomst is nietig aangezien deze tot stand is gekomen  door bedrog.
    """

    dwaling = Referentiedata(
        code="DWA",
        naam="Dwaling",
    )
    """
    De overeenkomst is nietig aangezien deze tot stand is gekomen als het gevolg van
    dwaling.
    """

    misbruik = Referentiedata(
        code="MIS",
        naam="Misbruik",
    )
    """
    De overeenkomst is nietig aangezien deze tot stand is gekomen door misbruik van
    omstandigheden.
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
