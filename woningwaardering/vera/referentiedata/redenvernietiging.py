from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class RedenvernietigingReferentiedata(Referentiedata):
    pass


class Redenvernietiging(Referentiedatasoort):
    bedreiging = RedenvernietigingReferentiedata(
        code="DRE",
        naam="Bedreiging",
    )
    """
    De overeenkomst is nietig aangezien deze tot stand is gekomen onder bedreiging.
    """

    bedrog = RedenvernietigingReferentiedata(
        code="DRO",
        naam="Bedrog",
    )
    """
    De overeenkomst is nietig aangezien deze tot stand is gekomen  door bedrog.
    """

    dwaling = RedenvernietigingReferentiedata(
        code="DWA",
        naam="Dwaling",
    )
    """
    De overeenkomst is nietig aangezien deze tot stand is gekomen als het gevolg van
    dwaling.
    """

    misbruik = RedenvernietigingReferentiedata(
        code="MIS",
        naam="Misbruik",
    )
    """
    De overeenkomst is nietig aangezien deze tot stand is gekomen door misbruik van
    omstandigheden.
    """
