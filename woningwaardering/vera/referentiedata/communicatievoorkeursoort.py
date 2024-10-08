from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Communicatievoorkeursoort(Enum):
    klantcontact = Referentiedata(
        code="KLA",
        naam="Klantcontact",
    )
    """
    Direct contact voor ondersteuning, vragen, of klachten
    """

    nieuwsbrief = Referentiedata(
        code="NIE",
        naam="Nieuwsbrief",
    )
    """
    Periodieke updates over projecten, evenementen, en relevante informatie voor
    huurders
    """

    kennisgeving = Referentiedata(
        code="KEN",
        naam="Kennisgeving",
    )
    """
    Informereren over onderhoudswerkzaamheden, aankondiging storingen,
    beleidswijzigingen, etc.
    """

    formele_communicatie = Referentiedata(
        code="FOR",
        naam="Formele communicatie",
    )
    """
    Officiële documenten zoals facturen, huurovereenkomsten, serviceovereenkomsten,
    betalingsherrinneringen, informatie over huurverhogingen
    """

    overige_communicatie = Referentiedata(
        code="OVE",
        naam="Overige communicatie",
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
