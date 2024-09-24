from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Eenheidinterieur(Enum):
    gemeubileerd = Referentiedata(
        code="GEM",
        naam="Gemeubileerd",
    )

    gestoffeerd = Referentiedata(
        code="GES",
        naam="Gestoffeerd",
    )

    houten_vloer = Referentiedata(
        code="HOU",
        naam="Houten vloer",
    )

    laminaat = Referentiedata(
        code="LAM",
        naam="Laminaat",
    )

    plavuizen = Referentiedata(
        code="PLA",
        naam="Plavuizen",
    )
    """
    Plavuizen of tegels
    """

    vloerbedekking = Referentiedata(
        code="VLB",
        naam="Vloerbedekking",
    )

    zelf_inrichten = Referentiedata(
        code="ZEL",
        naam="Zelf inrichten",
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
