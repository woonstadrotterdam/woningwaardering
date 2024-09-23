from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Vertrouwelijkheid(Enum):
    geheim = Referentiedata(
        code="GEH",
        naam="Geheim",
    )
    """
    Informatie is alleen toegankelijk voor direct geadresseerde(n) (bv: zorggegevens en
    strafrechtelijke informatie)
    """

    intern = Referentiedata(
        code="INT",
        naam="Intern",
    )
    """
    Informatie is toegankelijk voor alle medewerkers van de organisatie (bv: intranet)
    """

    openbaar = Referentiedata(
        code="OPE",
        naam="Openbaar",
    )
    """
    Informatie mag door iedereen worden ingezien (bv: algemene informatie op de website)
    """

    vertrouwelijk = Referentiedata(
        code="VER",
        naam="Vertrouwelijk",
    )
    """
    Informatie is alleen toegankelijk voor een beperkte groep gebruikers  (bv:
    persoonsgegevens, financiële gegevens)
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
