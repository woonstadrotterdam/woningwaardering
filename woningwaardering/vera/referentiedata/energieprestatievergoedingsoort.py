from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Energieprestatievergoedingsoort(Enum):
    epv_basis = Referentiedata(
        code="BAS",
        naam="EPV Basis",
    )
    """
    De maximale EPV geldt voor: een woning die ten minste duurzame energie levert voor
    het volledige gebouwgebonden gebruik (EGW) of een woning die ten minste duurzame
    energie levert voor het volledige gebouwgebonden deel (MGW).
    """

    epv_hoogwaardig = Referentiedata(
        code="HOO",
        naam="EPV Hoogwaardig",
    )
    """
    De maximale EPV geldt voor: een woning die ten minste duurzame energie levert voor
    het volledige gebouwgebonden deel én ten minste 2100 kWh/jaar voor het
    gebruikersgebonden deel (EGW) of een woning die ten minste duurzame energie
    levert voor het volledige gebouwgebonden deel én 530 kWh/jaar voor het
    gebruikersgebonden deel (MGW).
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
