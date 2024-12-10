from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class RedenontbindingReferentiedata(Referentiedata):
    pass


class Redenontbinding(Referentiedatasoort):
    niet_betaald = RedenontbindingReferentiedata(
        code="BET",
        naam="Niet betaald",
    )
    """
    Het verschuldigde bedrag van de overeenkomst is niet voldaan.
    """

    wanprestatie = RedenontbindingReferentiedata(
        code="WAN",
        naam="Wanprestatie",
    )
    """
    De overeenkomst wordt ontbonden omdat contractant tekortschiet in het nakomen van de
    afspraken.
    """
