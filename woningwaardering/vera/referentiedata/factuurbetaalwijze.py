from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Factuurbetaalwijze(Enum):
    automatische_incasso = Referentiedata(
        code="AIN",
        naam="Automatische incasso",
    )
    """
    Factuur wordt voldaan middels automatische incasso betaling.
    """

    contant = Referentiedata(
        code="CNT",
        naam="Contant",
    )
    """
    Factuur word voldaan middels contante betaling
    """

    op_rekening = Referentiedata(
        code="ORN",
        naam="Op rekening",
    )
    """
    Factuur wordt niet direct voldaan maar op rekening gezet. De rekening wordt (bijv.
    maandelijks) als 1 factuur aangeboden.
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
