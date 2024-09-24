from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Leningaflosvorm(Enum):
    annuitair = Referentiedata(
        code="ANN",
        naam="Annuitair",
    )
    """
    Jaarlijks wordt met deze vorm een vast bedrag afgelost. Samenstelling van rente en
    aflossing.
    """

    fixe = Referentiedata(
        code="FIX",
        naam="Fixe",
    )

    lineair = Referentiedata(
        code="LIN",
        naam="Lineair",
    )
    """
    Met deze vorm van lenen wordt een vast bedrag als aflossing betaald. Hierdoor wordt
    de totale lasten (rente + aflossing) steeds lager.
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
