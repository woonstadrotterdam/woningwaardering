from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Betalingsregelingstatus(Enum):
    aangevraagd = Referentiedata(
        code="AAN",
        naam="Aangevraagd",
    )
    """
    Ook wel aangemaakt.
    """

    actief = Referentiedata(
        code="ACT",
        naam="Actief",
    )
    """
    Toegekende betalingsregeling die loopt.
    """

    geannuleerd = Referentiedata(
        code="ANN",
        naam="Geannuleerd",
    )
    """
    Tussentijds gestopte regeling.
    """

    beeindigd = Referentiedata(
        code="BEE",
        naam="Beëindigd",
    )
    """
    Ook wel afgerond. Alle betalingsverplichtingen zijn voldaan.
    """

    bevroren = Referentiedata(
        code="BEV",
        naam="Bevroren",
    )
    """
    Tussentijds bevroren betalingsregeling omdat het niet mogelijk is om te voldoen aan
    de regeling.
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
