from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Publicatiestatus(Enum):
    in_aanbieding = Referentiedata(
        code="AAN",
        naam="In aanbieding",
    )
    """
    Het gepubliceerde vastgoed is in aanbieding.
    """

    afgerond = Referentiedata(
        code="AFG",
        naam="Afgerond",
    )
    """
    De publicatie van het vastgoed is afgerond.
    """

    gepubliceerd = Referentiedata(
        code="GEP",
        naam="Gepubliceerd",
    )
    """
    Het beschikbaar vastgoed is gepubliceerd.
    """

    gereed_voor_publicatie = Referentiedata(
        code="GER",
        naam="Gereed voor publicatie",
    )
    """
    De publicatie van beschikbaar vastgoed is gereed voor publicatie.
    """

    ingetrokken = Referentiedata(
        code="ING",
        naam="Ingetrokken",
    )
    """
    De publicatie van het vastgoed is ingetrokken.
    """

    in_voorbereiding = Referentiedata(
        code="VOO",
        naam="In voorbereiding",
    )
    """
    De publicatie van beschikbaar vastgoed is in voorbereiding.
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
