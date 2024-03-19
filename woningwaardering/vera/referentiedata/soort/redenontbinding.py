from vera.bvg.generated import Referentiedata


class Redenontbinding:
    niet_betaald = Referentiedata(
        code="BET",
        naam="Niet betaald",
    )
    """
    Het verschuldigde bedrag van de overeenkomst is niet voldaan.
    """

    wanprestatie = Referentiedata(
        code="WAN",
        naam="Wanprestatie",
    )
    """
    De overeenkomst wordt ontbonden omdat contractant tekortschiet in het nakomen van de
    afspraken.
    """
