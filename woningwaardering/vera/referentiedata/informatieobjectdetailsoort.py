from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Informatieobjectdetailsoort(Enum):
    advertentietekst = Referentiedata(
        code="ADT",
        naam="Advertentietekst",
    )
    """
    Advertentietekst met (HTML) of zonder opmaak (Text).
    """

    advies = Referentiedata(
        code="ADV",
        naam="Advies",
    )

    agenda = Referentiedata(
        code="AGE",
        naam="Agenda",
    )

    dag = Referentiedata(
        code="DAG",
        naam="Dag",
    )

    evaluatie = Referentiedata(
        code="EVA",
        naam="Evaluatie",
    )

    inspectie = Referentiedata(
        code="INS",
        naam="Inspectie",
    )

    jaar = Referentiedata(
        code="JAA",
        naam="Jaar",
    )

    kwartaal = Referentiedata(
        code="KWA",
        naam="Kwartaal",
    )

    maand = Referentiedata(
        code="MAA",
        naam="Maand",
    )

    notulen = Referentiedata(
        code="NOT",
        naam="Notulen",
    )

    onderhoud = Referentiedata(
        code="OND",
        naam="Onderhoud",
    )

    programma = Referentiedata(
        code="PRG",
        naam="Programma",
    )

    project = Referentiedata(
        code="PRJ",
        naam="Project",
    )

    week = Referentiedata(
        code="WEE",
        naam="Week",
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
