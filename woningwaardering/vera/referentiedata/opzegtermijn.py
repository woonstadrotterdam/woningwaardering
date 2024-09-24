from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Opzegtermijn(Enum):
    opzegtermijn_12_maanden = Referentiedata(
        code="12M",
        naam="12 maanden",
    )
    """
    Voor de overeenkomst geldt een opzegtermijn van 12 maanden.
    """

    opzegtermijn_14_dagen = Referentiedata(
        code="14D",
        naam="14 dagen",
    )
    """
    Voor de overeenkomst geldt een opzegtermijn van 14 dagen.
    """

    opzegtermijn_1_maand = Referentiedata(
        code="1M",
        naam="1 maand",
    )
    """
    Voor de overeenkomst geldt een opzegtermijn van 1 maand.
    """

    opzegtermijn_2_maanden = Referentiedata(
        code="2M",
        naam="2 maanden",
    )
    """
    Voor de overeenkomst geldt een opzegtermijn van 2 maanden.
    """

    opzegtermijn_3_maanden = Referentiedata(
        code="3M",
        naam="3 maanden",
    )
    """
    Voor de overeenkomst geldt een opzegtermijn van 3 maanden.
    """

    opzegtermijn_4_weken = Referentiedata(
        code="4W",
        naam="4 weken",
    )
    """
    Voor de overeenkomst geldt een opzegtermijn van 4 weken.
    """

    opzegtermijn_6_maanden = Referentiedata(
        code="6M",
        naam="6 maanden",
    )
    """
    Voor de overeenkomst geldt een opzegtermijn van 6 maanden.
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
