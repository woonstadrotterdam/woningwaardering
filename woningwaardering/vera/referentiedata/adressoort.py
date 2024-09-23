from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Adressoort(Enum):
    buitenlands_adres = Referentiedata(
        code="BUI",
        naam="Buitenlands adres",
    )
    """
    Een buitenlands adres.
    """

    eenheid_adres = Referentiedata(
        code="EEN",
        naam="Eenheid adres",
    )
    """
    De adresgegevens van een eenheid, ook wel woonadres
    """

    postadres = Referentiedata(
        code="POS",
        naam="Postadres",
    )
    """
    Het postadres
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
