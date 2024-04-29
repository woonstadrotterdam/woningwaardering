from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Huurklasse(Enum):
    betaalbaar = Referentiedata(
        code="BET",
        naam="Betaalbaar",
    )
    """
    Eenheid waarvan de netto huur (kale huur) per maand op of boven de
    kwaliteitskortingsgrens en onder de aftoppingsgrens (hoog) ligt.
    """

    boven_huurtoeslaggrens = Referentiedata(
        code="BOV",
        naam="Boven huurtoeslaggrens",
    )
    """
    Eenheid waarvan de netto huur (kale huur) per maand op of boven de huurtoeslaggrens
    (liberalisatiegrens) ligt.
    """

    duur = Referentiedata(
        code="DUU",
        naam="Duur",
    )
    """
    Eenheid waarvan de netto huur (kale huur) per maand op of boven de aftoppingsgrens
    (hoog) en onder de huurtoeslaggrens ligt.
    """

    goedkoop = Referentiedata(
        code="GOE",
        naam="Goedkoop",
    )
    """
    Eenheid waarvan de netto huur (kale huur) per maand onder de kwaliteitskortingsgrens
    ligt.
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
