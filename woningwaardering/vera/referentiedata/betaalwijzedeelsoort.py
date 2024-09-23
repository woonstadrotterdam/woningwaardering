from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Betaalwijzedeelsoort(Enum):
    maximaal_bedrag = Referentiedata(
        code="MAX",
        naam="Maximaal bedrag",
    )
    """
    Het maximale bedrag dat door de betaler wordt bijgedragen aan de huur. Bijvoorbeeld
    de ouders van de student dragen maximaal EUR 300 bij aan de huur.
    """

    percentage = Referentiedata(
        code="PER",
        naam="Percentage",
    )
    """
    Het percentage van de huur dat door de betaler wordt bijgedragen. Bijvoorbeeld een
    stel waarbij beiden de helft van de huur betalen.
    """

    restant_bedrag = Referentiedata(
        code="RES",
        naam="Restant bedrag",
    )
    """
    Het restant van de huur dat door de betreffende betaler wordt bijgedragen.
    Bijvoorbeeld de student die het restant van de huur betaalt na aftrek van de
    bijdrage van zijn/haar ouders.
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
