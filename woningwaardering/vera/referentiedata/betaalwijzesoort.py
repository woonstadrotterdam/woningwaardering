from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Betaalwijzesoort(Enum):
    handmatige_overboeking = Referentiedata(
        code="HND",
        naam="Handmatige overboeking",
    )
    """
    Een door de betaler geïnitieerde betaling, via een bankoverboeking , een voldaan
    betaalverzoek of via een PIN-betaling.
    """

    incasso = Referentiedata(
        code="INC",
        naam="Incasso",
    )
    """
    Een door de ontvanger geïnitieerde incasso, er moet een Incassomachtiging aan ten
    grondslag liggen.
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
