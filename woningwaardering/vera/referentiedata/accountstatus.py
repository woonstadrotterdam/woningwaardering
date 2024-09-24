from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Accountstatus(Enum):
    beeindigd = Referentiedata(
        code="BEE",
        naam="Beëindigd",
    )
    """
    Het account is beeïndigd.
    """

    geactiveerd = Referentiedata(
        code="GEA",
        naam="Geactiveerd",
    )
    """
    Het account is geactiveerd.
    """

    geblokkeerd = Referentiedata(
        code="GEB",
        naam="Geblokkeerd",
    )
    """
    Het account is (tijdelijk) geblokkeerd. Bijvoorbeeld door onjuiste invoer
    wachtwoord.
    """

    geregistreerd = Referentiedata(
        code="GER",
        naam="Geregistreerd",
    )
    """
    Het account is aangevraagd.
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
