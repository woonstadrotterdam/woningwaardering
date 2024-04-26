from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Materiaalsoort(Enum):
    beton = Referentiedata(
        code="BET",
        naam="Beton",
    )

    bitumen = Referentiedata(
        code="BIT",
        naam="Bitumen",
    )

    cement = Referentiedata(
        code="CEM",
        naam="Cement",
    )

    gips = Referentiedata(
        code="GIP",
        naam="Gips",
    )

    glas = Referentiedata(
        code="GLA",
        naam="Glas",
    )

    grondstof = Referentiedata(
        code="GRO",
        naam="Grondstof",
    )

    hout = Referentiedata(
        code="HOU",
        naam="Hout",
    )

    isolatie = Referentiedata(
        code="ISO",
        naam="Isolatie",
    )

    kunststof = Referentiedata(
        code="KUN",
        naam="Kunststof",
    )

    metaal = Referentiedata(
        code="MET",
        naam="Metaal",
    )

    natuursteen = Referentiedata(
        code="NAT",
        naam="Natuursteen",
    )

    ntb = Referentiedata(
        code="NTB",
        naam="Ntb",
    )

    rubber = Referentiedata(
        code="RUB",
        naam="Rubber",
    )

    samengesteld = Referentiedata(
        code="SAM",
        naam="Samengesteld",
    )

    steenachtig = Referentiedata(
        code="STE",
        naam="Steenachtig",
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
