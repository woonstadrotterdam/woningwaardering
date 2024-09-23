from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Inkomenssoort(Enum):
    bruto_jaarinkomen = Referentiedata(
        code="BRU",
        naam="Bruto jaarinkomen",
    )
    """
    Het bruto jaarinkomen kan bestaan uit een geregistreerd inkomen, schatting van het
    actuele inkomen of een zelf opgegeven inkomen.
    """

    netto_jaarinkomen = Referentiedata(
        code="NET",
        naam="Netto jaarinkomen",
    )
    """
    Het netto jaarinkomen zoals verwacht voor het huidige jaar.
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
