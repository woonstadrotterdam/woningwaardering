
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class PUBLICATIEMODEL:

    aanbodmodel = Referentiedata(
        code="AAN",
        naam="Aanbodmodel",
    )
    # aanbodmodel = ("AAN", "Aanbodmodel")
    """
    Vastgoed wordt aangeboden aan alle passende woningzoekenden. Deze kunnen vervolgens
    hun interesse aangeven voor het vastgoed en na toepassen van de spelregels krijgt de
    woningzoekende met de hoogste positie de eenheid aangeboden.
    """

    distributiemodel = Referentiedata(
        code="DIS",
        naam="Distributiemodel",
    )
    # distributiemodel = ("DIS", "Distributiemodel")
    """
    Woningzoekenden worden direct gekoppeld aan een vrijgekomen eenheid op basis van een
    beslissing van de vastgoedeigenaar. (De Woningzoekende kan in dit geval ook een
    rechtspersoon zijn, die namens een woningzoekende acteert.)
    """

    eerste_reageerder = Referentiedata(
        code="EER",
        naam="Eerste reageerder",
    )
    # eerste_reageerder = ("EER", "Eerste reageerder")
    """
    Aanbieden vindt plaats op basis van volgorde van reageren. Wie het eerst reageert,
    staat bovenaan de lijst.
    """

    lotingmodel = Referentiedata(
        code="LOT",
        naam="Lotingmodel",
    )
    # lotingmodel = ("LOT", "Lotingmodel")
    """
    Vastgoed wordt verloot onder geïnteresseerde woningzoekenden. Hierbij kan ook sprake
    zijn van 'gewogen' loting of andere combinaties van spelregels.
    """

    optiemodel = Referentiedata(
        code="OPT",
        naam="Optiemodel",
    )
    # optiemodel = ("OPT", "Optiemodel")
    """
    Woningzoekenden kunnen zichzelf op een wachtlijst zetten voor een cluster van
    vastgoed. Zodra een eenheid vrijkomt krijgt de woningzoekende met de hoogste positie
    de eenheid aangeboden.
    """

    vrijesectormodel = Referentiedata(
        code="VRI",
        naam="Vrijesectormodel",
    )
    # vrijesectormodel = ("VRI", "Vrijesectormodel")
    """
    Vastgoed wordt regelvrij aangeboden aan alle woningzoekenden. Deze kunnen vervolgens
    hun interesse aangeven voor het vastgoed. Voor het betrekken van de woning kunnen
    overigens wel degelijk eisen gesteld worden (bijv. minimaal inkomen.)
    """

    woningruilmodel = Referentiedata(
        code="WON",
        naam="Woningruilmodel",
    )
    # woningruilmodel = ("WON", "Woningruilmodel")
    """
    Woningzoekenden kunnen onderling eenheden ruilen.
    """
