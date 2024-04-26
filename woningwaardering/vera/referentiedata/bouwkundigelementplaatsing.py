from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Bouwkundigelementplaatsing(Enum):
    individuele_wmo_voorziening = Referentiedata(
        code="IWV",
        naam="Individuele WMO voorziening",
    )
    """
    Het bouwkundig element is aangebracht als individuele WMO voorziening.
    """

    overig = Referentiedata(
        code="OVE",
        naam="Overig",
    )
    """
    Het bouwkundig element is aangebracht zonder dat deze onder een specifieke regeling
    (ZAV, WMO) valt.
    """

    wet_maatschappelijke_ondersteuning = Referentiedata(
        code="WMO",
        naam="Wet maatschappelijke ondersteuning",
    )
    """
    Het bouwkundig element is aangebracht onder de voorwaarden van de Wet
    Maatschappelijke Ondersteuning.
    """

    zelf_aangebrachte_voorziening = Referentiedata(
        code="ZAV",
        naam="Zelf aangebrachte voorziening",
    )
    """
    Het bouwkundig element is aangebracht als zelf aangebrachte voorziening.
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
