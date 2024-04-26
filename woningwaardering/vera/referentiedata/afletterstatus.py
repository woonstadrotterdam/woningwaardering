from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Afletterstatus(Enum):
    deels_afgeletterd = Referentiedata(
        code="DEE",
        naam="Deels afgeletterd",
    )
    """
    Boeking is deels afgeletterd tegen andere boekingen. Voor vorderingen houdt dit in
    dat er betalingen zijn gedaan maar dat er nog een openstaand saldo is. Voor
    ontvangsten betekent dit dat een deel van de ontvangst is afgeletterd tegen een
    vordering maar dat er nog saldo op de boeking staat die nog gekoppeld moet
    worden.
    """

    niet_afgeletterd = Referentiedata(
        code="NIE",
        naam="Niet afgeletterd",
    )
    """
    Boeking is (nog) niet afgeletterd tegen andere boekingen. Voor vorderingen houdt dit
    in dat deze nog volledig open staat. Voor ontvangsten betekent dit dat deze nog
    niet gekoppeld is aan een vordering.
    """

    volledig_afgeletterd = Referentiedata(
        code="VOL",
        naam="Volledig afgeletterd",
    )
    """
    Boeking is volledig afgeletterd tegen andere boekingen. Voor vorderingen houdt dit
    in dat er geen openstaand saldo meer is. Voor ontvangsten betekent dit dat de
    ontvangst volledig is afgeletterd tegen vordering(en).
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
