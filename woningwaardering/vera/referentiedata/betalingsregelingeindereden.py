from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Betalingsregelingeindereden(Enum):
    afbetaald = Referentiedata(
        code="AFB",
        naam="Afbetaald",
    )
    """
    De betalingsregeling is beëindigd omdat deze is afbetaald.
    """

    oninbaar = Referentiedata(
        code="ONI",
        naam="Oninbaar",
    )
    """
    De betalingsregeling is beëindigd omdat deze oninbaar is gebleken.
    """

    restschuld_gesaneerd = Referentiedata(
        code="SAN",
        naam="Restschuld gesaneerd",
    )
    """
    De betalingsregeling is beëindigd omdat de restschuld is gesaneerd.
    """

    regeling_voldoet_niet = Referentiedata(
        code="VOL",
        naam="Regeling voldoet niet",
    )
    """
    De betalingsregeling is (voortijdig) beëindigd omdat de regeling niet voldoet in de
    specifieke situatie.
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
