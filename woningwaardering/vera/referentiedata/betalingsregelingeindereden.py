from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BetalingsregelingeinderedenReferentiedata(Referentiedata):
    pass


class Betalingsregelingeindereden(Referentiedatasoort):
    afbetaald = BetalingsregelingeinderedenReferentiedata(
        code="AFB",
        naam="Afbetaald",
    )
    """
    De betalingsregeling is beëindigd omdat deze is afbetaald.
    """

    oninbaar = BetalingsregelingeinderedenReferentiedata(
        code="ONI",
        naam="Oninbaar",
    )
    """
    De betalingsregeling is beëindigd omdat deze oninbaar is gebleken.
    """

    restschuld_gesaneerd = BetalingsregelingeinderedenReferentiedata(
        code="SAN",
        naam="Restschuld gesaneerd",
    )
    """
    De betalingsregeling is beëindigd omdat de restschuld is gesaneerd.
    """

    regeling_voldoet_niet = BetalingsregelingeinderedenReferentiedata(
        code="VOL",
        naam="Regeling voldoet niet",
    )
    """
    De betalingsregeling is (voortijdig) beëindigd omdat de regeling niet voldoet in de
    specifieke situatie.
    """
