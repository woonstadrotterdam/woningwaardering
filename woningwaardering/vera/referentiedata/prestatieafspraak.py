from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Prestatieafspraak(Enum):
    huurverhoging_t_b_v_investering = Referentiedata(
        code="HUU",
        naam="Huurverhoging t.b.v. investering",
    )
    """
    Inkomensafhankelijke huurverhoging boven normpercentage waarvoor gemeente,
    corporatie en huurdersorganisatie hebben afgesproken dat zij de meeropbrengsten
    van die hogere huurverhoging gebruiken voor investeringen.
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
