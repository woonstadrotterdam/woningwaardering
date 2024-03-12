
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class BETALINGSREGELINGEINDEREDEN:

    afbetaald = Referentiedata(
        code="AFB",
        naam="Afbetaald",
    )
    # afbetaald = ("AFB", "Afbetaald")
    """
    De betalingsregeling is beëindigd omdat deze is afbetaald.
    """

    oninbaar = Referentiedata(
        code="ONI",
        naam="Oninbaar",
    )
    # oninbaar = ("ONI", "Oninbaar")
    """
    De betalingsregeling is beëindigd omdat deze oninbaar is gebleken.
    """

    restschuld_gesaneerd = Referentiedata(
        code="SAN",
        naam="Restschuld gesaneerd",
    )
    # restschuld_gesaneerd = ("SAN", "Restschuld gesaneerd")
    """
    De betalingsregeling is beëindigd omdat de restschuld is gesaneerd.
    """

    regeling_voldoet_niet = Referentiedata(
        code="VOL",
        naam="Regeling voldoet niet",
    )
    # regeling_voldoet_niet = ("VOL", "Regeling voldoet niet")
    """
    De betalingsregeling is (voortijdig) beëindigd omdat de regeling niet voldoet in de
    specifieke situatie.
    """
