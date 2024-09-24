from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Verantwoordingregime(Enum):
    administratieve_scheiding = Referentiedata(
        code="ADM",
        naam="Administratieve scheiding",
    )
    """
    De DAEB- en niet-DAEB activiteiten van de coporatie worden administratief van elkaar
    gescheiden
    """

    hybride = Referentiedata(
        code="HYB",
        naam="Hybride",
    )
    """
    Een scheiding is hybride indien er bezit wordt overgeheveld van de TI naar een
    dochtervennootschap, terwijl ook niet-DAEB bezit achterblijft in de TI.
    """

    juridische_scheiding = Referentiedata(
        code="JUR",
        naam="Juridische scheiding",
    )
    """
    De DAEB- en niet-DAEB activiteiten van de corporatie zijn in aparte juridische
    entiteiten ondergebracht, elk met een eigen financiële administratie
    """

    verlicht_regime = Referentiedata(
        code="VER",
        naam="Verlicht regime",
    )
    """
    De corporatie voldoet aan de voorwaarden waaronder geen gescheiden administraties
    voor DAEB- en niet-DAEB activiteiten gevoerd hoeven te worden.
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
