from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Brandwerendheidscore(Enum):
    brandwerendheidscore_15_minuten = Referentiedata(
        code="15",
        naam="15 minuten",
    )
    """
    15 minuten brandwerendheid (Aedes ILS)
    """

    brandwerendheidscore_20_minuten = Referentiedata(
        code="20",
        naam="20 minuten",
    )
    """
    20 minuten brandwerendheid (Aedes ILS)
    """

    brandwerendheidscore_30_minuten = Referentiedata(
        code="30",
        naam="30 minuten",
    )
    """
    30 minuten brandwerendheid (Aedes ILS)
    """

    brandwerendheidscore_45_minuten = Referentiedata(
        code="45",
        naam="45 minuten",
    )
    """
    45 minuten brandwerendheid (Aedes ILS)
    """

    brandwerendheidscore_60_minuten = Referentiedata(
        code="60",
        naam="60 minuten",
    )
    """
    60 minuten brandwerendheid (Aedes ILS)
    """

    brandwerendheidscore_90_minuten = Referentiedata(
        code="90",
        naam="90 minuten",
    )
    """
    90 minuten brandwerendheid (Aedes ILS)
    """

    brandwerendheidscore_120_minuten = Referentiedata(
        code="120",
        naam="120 minuten",
    )
    """
    120 minuten brandwerendheid (Aedes ILS)
    """

    brandwerendheidscore_180_minuten = Referentiedata(
        code="180",
        naam="180 minuten",
    )
    """
    180 minuten brandwerendheid (Aedes ILS)
    """

    brandwerendheidscore_240_minuten = Referentiedata(
        code="240",
        naam="240 minuten",
    )
    """
    240 minuten brandwerendheid (Aedes ILS)
    """

    brandwerendheidscore_360_minuten = Referentiedata(
        code="360",
        naam="360 minuten",
    )
    """
    360 minuten brandwerendheid (Aedes ILS)
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
