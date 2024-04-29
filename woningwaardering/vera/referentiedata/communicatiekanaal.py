from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Communicatiekanaal(Enum):
    whatsapp = Referentiedata(
        code="APP",
        naam="Whatsapp",
    )

    balie = Referentiedata(
        code="BAL",
        naam="Balie",
    )

    huisbezoek = Referentiedata(
        code="BEZ",
        naam="Huisbezoek",
    )

    brief = Referentiedata(
        code="BRI",
        naam="Brief",
    )

    e_mail = Referentiedata(
        code="EMA",
        naam="E-mail",
    )

    inspectie = Referentiedata(
        code="INS",
        naam="Inspectie",
    )

    internet_en_of_klantportaal = Referentiedata(
        code="INT",
        naam="Internet / klantportaal",
    )

    sms = Referentiedata(
        code="SMS",
        naam="SMS",
    )

    telefoon = Referentiedata(
        code="TEL",
        naam="Telefoon",
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
