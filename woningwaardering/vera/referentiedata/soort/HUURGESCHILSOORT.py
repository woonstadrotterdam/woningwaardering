
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class HUURGESCHILSOORT:

    bezwaarschrift = Referentiedata(
        code="BEZ",
        naam="Bezwaarschrift",
    )
    # bezwaarschrift = ("BEZ", "Bezwaarschrift")
    """
    Huurgeschil met als aanleiding een (niet nader gespecificeerd) bezwaarschrift
    """

    inkomen = Referentiedata(
        code="INK",
        naam="Inkomen",
    )
    # inkomen = ("INK", "Inkomen")
    """
    Huurgeschil met als aanleiding een dispuut over het inkomen van de huurder
    """

    onderhoud = Referentiedata(
        code="OND",
        naam="Onderhoud",
    )
    # onderhoud = ("OND", "Onderhoud")
    """
    Huurgeschil met als aanleiding een dispuut over de onderhoudsstaat van de woning, of
    over kosten die voortvloeien uit uitgevoerd onderhoud
    """

    verzoekschrift = Referentiedata(
        code="VER",
        naam="Verzoekschrift",
    )
    # verzoekschrift = ("VER", "Verzoekschrift")
    """
    Huurgeschil met als aanleiding een (niet nader gespecificeerd) verzoekschrift
    """

    woningwaardering = Referentiedata(
        code="WON",
        naam="Woningwaardering",
    )
    # woningwaardering = ("WON", "Woningwaardering")
    """
    Huurgeschil met als aanleiding een dispuut over het woningwaarderingsresultaat
    """
