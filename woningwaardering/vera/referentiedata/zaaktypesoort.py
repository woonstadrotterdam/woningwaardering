from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Zaaktypesoort(Enum):
    leefbaarheid = Referentiedata(
        code="LEE",
        naam="Leefbaarheid",
    )
    """
    Op initiatief van de corporatie verbeteren van de buurt
    """

    omgevingsoverlast = Referentiedata(
        code="OMG",
        naam="Omgevingsoverlast",
    )
    """
    Overlast in de omgeving
    """

    klacht_over_organisatie = Referentiedata(
        code="ORG",
        naam="Klacht over organisatie",
    )
    """
    Klachten over de corporatie als organisatie
    """

    sociale_melding = Referentiedata(
        code="SOC",
        naam="Sociale melding",
    )
    """
    Overige sociale gerelateerde meldingen
    """

    woonfraude = Referentiedata(
        code="WOO",
        naam="Woonfraude",
    )
    """
    Fraude door bewoner
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
