from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Sanctiesoort(Enum):
    milde_sanctie = Referentiedata(
        code="MIL",
        naam="Milde sanctie",
    )
    """
    Milde sanctie
    """

    no_show_sanctie = Referentiedata(
        code="NOS",
        naam="No-show sanctie",
    )
    """
    No-show sanctie, , verlies van alle zoek-, situatie en zoekpunten
    """

    zware_sanctie = Referentiedata(
        code="ZWA",
        naam="Zware sanctie",
    )
    """
    Zware sanctie, verlies van alle zoek-, situatie en zoekpunten
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
