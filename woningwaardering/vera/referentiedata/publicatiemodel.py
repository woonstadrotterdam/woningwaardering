from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class PublicatiemodelReferentiedata(Referentiedata):
    pass


class Publicatiemodel(Referentiedatasoort):
    aanbodmodel = PublicatiemodelReferentiedata(
        code="AAN",
        naam="Aanbodmodel",
    )
    """
    Vastgoed wordt aangeboden aan alle passende woningzoekenden. Deze kunnen vervolgens
    hun interesse aangeven voor het vastgoed en na toepassen van de spelregels
    krijgt de woningzoekende met de hoogste positie de eenheid aangeboden.
    """

    distributiemodel = PublicatiemodelReferentiedata(
        code="DIS",
        naam="Distributiemodel",
    )
    """
    Woningzoekenden worden direct gekoppeld aan een vrijgekomen eenheid op basis van een
    beslissing van de vastgoedeigenaar. (De Woningzoekende kan in dit geval ook een
    rechtspersoon zijn, die namens een woningzoekende acteert.)
    """

    eerste_reageerder = PublicatiemodelReferentiedata(
        code="EER",
        naam="Eerste reageerder",
    )
    """
    Aanbieden vindt plaats op basis van volgorde van reageren. Wie het eerst reageert,
    staat bovenaan de lijst.
    """

    lotingmodel = PublicatiemodelReferentiedata(
        code="LOT",
        naam="Lotingmodel",
    )
    """
    Vastgoed wordt verloot onder geïnteresseerde woningzoekenden. Hierbij kan ook sprake
    zijn van 'gewogen' loting of andere combinaties van spelregels.
    """

    optiemodel = PublicatiemodelReferentiedata(
        code="OPT",
        naam="Optiemodel",
    )
    """
    Woningzoekenden kunnen zichzelf op een wachtlijst zetten voor een cluster van
    vastgoed. Zodra een eenheid vrijkomt krijgt de woningzoekende met de hoogste
    positie de eenheid aangeboden.
    """

    vrijesectormodel = PublicatiemodelReferentiedata(
        code="VRI",
        naam="Vrijesectormodel",
    )
    """
    Vastgoed wordt regelvrij aangeboden aan alle woningzoekenden. Deze kunnen vervolgens
    hun interesse aangeven voor het vastgoed. Voor het betrekken van de woning
    kunnen overigens wel degelijk eisen gesteld worden (bijv. minimaal inkomen.)
    """

    woningruilmodel = PublicatiemodelReferentiedata(
        code="WON",
        naam="Woningruilmodel",
    )
    """
    Woningzoekenden kunnen onderling eenheden ruilen.
    """
