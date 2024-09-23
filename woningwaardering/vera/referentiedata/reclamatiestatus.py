from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Reclamatiestatus(Enum):
    afgewezen = Referentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    """
    De reclamatie is afgewezen door commissie.
    """

    in_beroep = Referentiedata(
        code="BER",
        naam="In beroep",
    )
    """
    De reclamatie is in beroep gegaan door de woningzoekende.
    """

    in_behandeling = Referentiedata(
        code="INB",
        naam="In behandeling",
    )
    """
    De reclamatie is in behandeling genomen door de commissie.
    """

    ingediend = Referentiedata(
        code="ING",
        naam="Ingediend",
    )
    """
    De reclamatie is ingediend door de woningzoekende.
    """

    toegekend = Referentiedata(
        code="TOE",
        naam="Toegekend",
    )
    """
    De reclamatie is toegekend door de comissie.
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
