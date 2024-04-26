from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Huurgeschilsoort(Enum):
    bezwaarschrift = Referentiedata(
        code="BEZ",
        naam="Bezwaarschrift",
    )
    """
    Huurgeschil met als aanleiding een (niet nader gespecificeerd) bezwaarschrift
    """

    inkomen = Referentiedata(
        code="INK",
        naam="Inkomen",
    )
    """
    Huurgeschil met als aanleiding een dispuut over het inkomen van de huurder
    """

    onderhoud = Referentiedata(
        code="OND",
        naam="Onderhoud",
    )
    """
    Huurgeschil met als aanleiding een dispuut over de onderhoudsstaat van de woning, of
    over kosten die voortvloeien uit uitgevoerd onderhoud
    """

    verzoekschrift = Referentiedata(
        code="VER",
        naam="Verzoekschrift",
    )
    """
    Huurgeschil met als aanleiding een (niet nader gespecificeerd) verzoekschrift
    """

    woningwaardering = Referentiedata(
        code="WON",
        naam="Woningwaardering",
    )
    """
    Huurgeschil met als aanleiding een dispuut over het woningwaarderingsresultaat
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
