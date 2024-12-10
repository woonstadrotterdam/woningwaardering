from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class AanbiedingstatusReferentiedata(Referentiedata):
    pass


class Aanbiedingstatus(Referentiedatasoort):
    aangeboden = AanbiedingstatusReferentiedata(
        code="AAN",
        naam="Aangeboden",
    )
    """
    Er is aanbieding gedaan aan een of meer kandidaten.
    """

    geweigerd = AanbiedingstatusReferentiedata(
        code="GEW",
        naam="Geweigerd",
    )
    """
    Een kandidaat heeft een verstrekte aanbieding afgewezen.
    """

    ingetrokken = AanbiedingstatusReferentiedata(
        code="ING",
        naam="Ingetrokken",
    )
    """
    Een aan een kandidaat verstrekte aanbieding is ingetrokken.
    """

    toegewezen = AanbiedingstatusReferentiedata(
        code="TOE",
        naam="Toegewezen",
    )
    """
    Een eenheid is toegewezen aan een kandidaat.
    """
