from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.publicatiemodel import Publicatiemodel


class Publicatieintakevorm(Enum):
    cooptatie = Referentiedata(
        code="COO",
        naam="Coöptatie",
        parent=Publicatiemodel.aanbodmodel.value,
    )
    """
    Medebewoners bepalen welke woningzoekende de eenheid krijgt.
    """

    intakegesprek = Referentiedata(
        code="INT",
        naam="Intakegesprek",
        parent=Publicatiemodel.aanbodmodel.value,
    )
    """
    Er vindt een intake gesprek plaats met de eigenaar van de woning.
    """

    motivatie = Referentiedata(
        code="MOT",
        naam="Motivatie",
        parent=Publicatiemodel.aanbodmodel.value,
    )
    """
    Toewijzing vindt plaats op basis van de beoordeling van een motivatiebrief of
    -gesprek.
    """

    sociale_spelregels = Referentiedata(
        code="SOC",
        naam="Sociale spelregels",
        parent=Publicatiemodel.aanbodmodel.value,
    )
    """
    Sociale spelregels bepalen welke woningzoekende de eenheid krijgt.
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
