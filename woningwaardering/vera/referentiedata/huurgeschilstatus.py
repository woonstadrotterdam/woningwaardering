from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Huurgeschilstatus(Enum):
    afgewezen = Referentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    """
    Het huurgeschil is afgewezen, en daarmee tevens afgehandeld
    """

    in_behandeling = Referentiedata(
        code="INB",
        naam="In behandeling",
    )
    """
    Het huurgeschil is (nog) in behandeling
    """

    toegekend = Referentiedata(
        code="TOE",
        naam="Toegekend",
    )
    """
    Het huurgeschil is toegekend, en daarmee tevens afgehandeld
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
