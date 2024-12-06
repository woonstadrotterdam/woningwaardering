from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Afspraakverzoeksoort(Referentiedatasoort):
    eindinspectie = Referentiedata(
        code="EIN",
        naam="Eindinspectie",
    )
    """
    Verzoek voor het maken van een afspraak voor een eindinspectie naar aanleiding van
    de ontvangst van een huuropzegging.
    """

    voorinspectie = Referentiedata(
        code="VOO",
        naam="Voorinspectie",
    )
    """
    Verzoek voor het maken van een afspraak voor een voorinspectie naar aanleiding van
    de ontvangst van een huuropzegging.
    """
