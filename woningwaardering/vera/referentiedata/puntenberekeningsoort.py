from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Puntenberekeningsoort(Enum):
    intrekken_gebeurtenis_of_sanctie = Referentiedata(
        code="INT",
        naam="Intrekken gebeurtenis of sanctie",
    )

    intrekken_toewijzing = Referentiedata(
        code="ITO",
        naam="Intrekken toewijzing",
    )
    """
    Intrekken toewijzing van de eenheid.
    """

    koppelen_inschrijving = Referentiedata(
        code="KOP",
        naam="Koppelen inschrijving",
    )

    maandelijkse_herberekening = Referentiedata(
        code="MAA",
        naam="Maandelijkse herberekening",
    )

    nieuwe_inschrijving = Referentiedata(
        code="NIE",
        naam="Nieuwe inschrijving",
    )

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
