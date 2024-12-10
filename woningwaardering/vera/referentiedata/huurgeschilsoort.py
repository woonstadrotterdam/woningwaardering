from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class HuurgeschilsoortReferentiedata(Referentiedata):
    pass


class Huurgeschilsoort(Referentiedatasoort):
    bezwaarschrift = HuurgeschilsoortReferentiedata(
        code="BEZ",
        naam="Bezwaarschrift",
    )
    """
    Huurgeschil met als aanleiding een (niet nader gespecificeerd) bezwaarschrift
    """

    inkomen = HuurgeschilsoortReferentiedata(
        code="INK",
        naam="Inkomen",
    )
    """
    Huurgeschil met als aanleiding een dispuut over het inkomen van de huurder
    """

    onderhoud = HuurgeschilsoortReferentiedata(
        code="OND",
        naam="Onderhoud",
    )
    """
    Huurgeschil met als aanleiding een dispuut over de onderhoudsstaat van de woning, of
    over kosten die voortvloeien uit uitgevoerd onderhoud
    """

    verzoekschrift = HuurgeschilsoortReferentiedata(
        code="VER",
        naam="Verzoekschrift",
    )
    """
    Huurgeschil met als aanleiding een (niet nader gespecificeerd) verzoekschrift
    """

    woningwaardering = HuurgeschilsoortReferentiedata(
        code="WON",
        naam="Woningwaardering",
    )
    """
    Huurgeschil met als aanleiding een dispuut over het woningwaarderingsresultaat
    """
