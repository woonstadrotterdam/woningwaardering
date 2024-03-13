from woningwaardering.vera.bvg.models import Referentiedata


class AFSPRAAKVERZOEKSOORT:
    eindinspectie = Referentiedata(
        code="EIN",
        naam="Eindinspectie",
    )
    """
    Verzoek voor het maken van een afspraak voor een voorinspectie naar aanleiding van
    de ontvangst van een huuropzegging.
    """

    voorinspectie = Referentiedata(
        code="VOO",
        naam="Voorinspectie",
    )
    """
    Verzoek voor het maken van een afspraak voor een eindinspectie naar aanleiding van
    de ontvangst van een huuropzegging.
    """
