from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Passendheiddetailsoort(Enum):
    bijzondere_gezinssituatie = Referentiedata(
        code="BIJ",
        naam="Bijzondere gezinssituatie",
    )
    """
    Niet-passende toewijzing, noodzakelijk geacht omdat sprake is van een bijzondere
    woonbehoefte waarvoor geen regulier passende woning beschikbaar is. Bijvoorbeeld
    een zeer groot gezin of een bijzondere gezinssamenstelling.
    """

    herstructurering = Referentiedata(
        code="HER",
        naam="Herstructurering",
    )
    """
    Niet-passende toewijzing, noodzakelijk geacht i.v.m. herstructurering
    """

    herhuisvesting = Referentiedata(
        code="HHV",
        naam="Herhuisvesting",
    )
    """
    Niet-passende toewijzing, noodzakelijk geacht i.v.m. calamiteit of andere dringende
    oorzaak. Let op: voor herhuisvesting in verband met herstructurering gebruik
    passenheiddetailsoort 'Herstructurering'
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
