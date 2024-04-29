from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Vragenlijstregelherkomst(Enum):
    aedes_benchmark = Referentiedata(
        code="AED",
        naam="Aedes-benchmark",
    )
    """
    De herkomst van de vraag is van de Aedes benchmark.
    """

    kwh_keurmerk = Referentiedata(
        code="KWH",
        naam="KWH Keurmerk",
    )
    """
    De herkomst van de vraag is van KWH in het kader van het eigen keurmerk.
    """

    eigen_vraag = Referentiedata(
        code="EIG",
        naam="Eigen vraag",
    )
    """
    De kwaliteitsmetingsvraag is door de eigen organisatie opgesteld
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
