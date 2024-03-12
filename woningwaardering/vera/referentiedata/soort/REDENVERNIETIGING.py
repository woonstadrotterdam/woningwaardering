
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class REDENVERNIETIGING:

    bedreiging = Referentiedata(
        code="DRE",
        naam="Bedreiging",
    )
    # bedreiging = ("DRE", "Bedreiging")
    """
    De overeenkomst is nietig aangezien deze tot stand is gekomen onder bedreiging.
    """

    bedrog = Referentiedata(
        code="DRO",
        naam="Bedrog",
    )
    # bedrog = ("DRO", "Bedrog")
    """
    De overeenkomst is nietig aangezien deze tot stand is gekomen door bedrog.
    """

    dwaling = Referentiedata(
        code="DWA",
        naam="Dwaling",
    )
    # dwaling = ("DWA", "Dwaling")
    """
    De overeenkomst is nietig aangezien deze tot stand is gekomen als het gevolg van
    dwaling.
    """

    misbruik = Referentiedata(
        code="MIS",
        naam="Misbruik",
    )
    # misbruik = ("MIS", "Misbruik")
    """
    De overeenkomst is nietig aangezien deze tot stand is gekomen door misbruik van
    omstandigheden.
    """
