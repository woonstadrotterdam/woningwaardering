from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Inkomensverklaringsoort(Enum):
    ib60 = Referentiedata(
        code="IB6",
        naam="IB60",
    )

    inkomensverklaring_belastingdienst = Referentiedata(
        code="IBD",
        naam="Inkomensverklaring belastingdienst",
    )

    ibri = Referentiedata(
        code="IBR",
        naam="IBRI",
    )

    jaaropgave = Referentiedata(
        code="JAA",
        naam="Jaaropgave",
    )

    loonstrook = Referentiedata(
        code="LOO",
        naam="Loonstrook",
    )

    uitkeringsspecificatie = Referentiedata(
        code="UIT",
        naam="Uitkeringsspecificatie",
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
