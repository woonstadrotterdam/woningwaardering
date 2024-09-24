from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Onderhoudslabel(Enum):
    basis_onderhoud = Referentiedata(
        code="BAS",
        naam="Basis onderhoud",
    )

    geen_onderhoud = Referentiedata(
        code="GEE",
        naam="Geen onderhoud",
    )

    monument_onderhoud = Referentiedata(
        code="MON",
        naam="Monument onderhoud",
    )

    volledig_onderhoud = Referentiedata(
        code="VOL",
        naam="Volledig onderhoud",
    )

    wind_en_waterdicht_houden = Referentiedata(
        code="WIN",
        naam="Wind en waterdicht houden",
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
