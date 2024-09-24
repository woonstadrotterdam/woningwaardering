from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Informatieobjectsoort(Enum):
    brochure = Referentiedata(
        code="BRO",
        naam="Brochure",
    )

    document = Referentiedata(
        code="DOC",
        naam="Document",
    )
    """
    Text bestand met (HTML) of zonder opmaak (Text)
    """

    foto = Referentiedata(
        code="FOT",
        naam="Foto",
    )
    """
    Foto, Image, Plaatje, Afbeelding
    """

    kopie = Referentiedata(
        code="KOP",
        naam="Kopie",
    )

    notitie = Referentiedata(
        code="NOT",
        naam="Notitie",
    )
    """
    Het informatieobject is een notitie- of memo (tekst)
    """

    overeenkomst = Referentiedata(
        code="OVE",
        naam="Overeenkomst",
    )

    plattegrond = Referentiedata(
        code="PLA",
        naam="Plattegrond",
    )

    plan = Referentiedata(
        code="PLN",
        naam="Plan",
    )

    rapport = Referentiedata(
        code="RAP",
        naam="Rapport",
    )

    verslag = Referentiedata(
        code="VER",
        naam="Verslag",
    )

    video = Referentiedata(
        code="VID",
        naam="Video",
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
