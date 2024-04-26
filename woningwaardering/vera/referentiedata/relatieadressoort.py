from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Relatieadressoort(Enum):
    bezoekadres = Referentiedata(
        code="BEZ",
        naam="Bezoekadres",
    )

    factuuradres = Referentiedata(
        code="FAC",
        naam="Factuuradres",
    )

    leveringsadres = Referentiedata(
        code="LEV",
        naam="Leveringsadres",
    )
    """
    Het adres waar eventuele goederen afgeleverd of bezorgd dienen te worden.
    """

    postadres = Referentiedata(
        code="POS",
        naam="Postadres",
    )

    woonadres = Referentiedata(
        code="WOO",
        naam="Woonadres",
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
