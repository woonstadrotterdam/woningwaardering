from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class AfspraakverzoeksoortReferentiedata(Referentiedata):
    pass


class Afspraakverzoeksoort(Referentiedatasoort):
    eindinspectie = AfspraakverzoeksoortReferentiedata(
        code="EIN",
        naam="Eindinspectie",
    )
    """
    Verzoek voor het maken van een afspraak voor een eindinspectie naar aanleiding van
    de ontvangst van een huuropzegging.
    """

    voorinspectie = AfspraakverzoeksoortReferentiedata(
        code="VOO",
        naam="Voorinspectie",
    )
    """
    Verzoek voor het maken van een afspraak voor een voorinspectie naar aanleiding van
    de ontvangst van een huuropzegging.
    """
