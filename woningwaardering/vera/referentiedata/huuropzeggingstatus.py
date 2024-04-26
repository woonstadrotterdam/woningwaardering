from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Huuropzeggingstatus(Enum):
    aangemaakt = Referentiedata(
        code="AAN",
        naam="Aangemaakt",
    )
    """
    De huuropzegging (c.q. het verzoek tot huuropzegging) is geregistreerd, maar nog
    niet in behandeling genomen.
    """

    afgewezen = Referentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    """
    De huuropzegging voldoet niet aan de voorwaarden en is afgewezen.
    """

    geannuleerd = Referentiedata(
        code="GEA",
        naam="Geannuleerd",
    )
    """
    De huuropzegging is geannuleerd, voordat de beoordeling heeft plaatsgevonden.
    """

    goedgekeurd = Referentiedata(
        code="GOE",
        naam="Goedgekeurd",
    )
    """
    De huuropzegging voldoet aan de voorwaarden en is goedgekeurd.
    """

    in_behandeling = Referentiedata(
        code="INB",
        naam="In behandeling",
    )
    """
    De huuropzegging is geregistreerd en in behandeling genomen, maar nog niet
    beoordeeld.
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
