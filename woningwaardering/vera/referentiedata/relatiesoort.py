from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Relatiesoort(Enum):
    relatiegroep = Referentiedata(
        code="GRO",
        naam="Relatiegroep",
    )
    """
    Een verzameling relaties (bijvoorbeeld een huishouden)
    """

    natuurlijke_persoon = Referentiedata(
        code="NAT",
        naam="Natuurlijke persoon",
    )
    """
    Een natuurlijk persoon is iemand, een mens van vlees en bloed, die rechten en
    plichten heeft.
    """

    rechtspersoon = Referentiedata(
        code="REC",
        naam="Rechtspersoon",
    )
    """
    Een rechtspersoon is een juridische constructie waardoor een abstracte entiteit of
    organisatie op kan treden als een volwaardig en handelingsbekwaam persoon in het
    rechtsverkeer behept met rechten en plichten zoals een natuurlijk persoon dat
    kan doen.
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
