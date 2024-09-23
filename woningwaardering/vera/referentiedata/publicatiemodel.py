from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Publicatiemodel(Enum):
    aanbodmodel = Referentiedata(
        code="AAN",
        naam="Aanbodmodel",
    )
    """
    Vastgoed wordt aangeboden aan alle passende woningzoekenden. Deze kunnen vervolgens
    hun interesse aangeven voor het vastgoed en na toepassen van de spelregels
    krijgt de woningzoekende met de hoogste positie de eenheid aangeboden.
    """

    distributiemodel = Referentiedata(
        code="DIS",
        naam="Distributiemodel",
    )
    """
    Woningzoekenden worden direct gekoppeld aan een vrijgekomen eenheid op basis van een
    beslissing van de vastgoedeigenaar. (De Woningzoekende kan in dit geval ook een
    rechtspersoon zijn, die namens een woningzoekende acteert.)
    """

    eerste_reageerder = Referentiedata(
        code="EER",
        naam="Eerste reageerder",
    )
    """
    Aanbieden vindt plaats op basis van volgorde van reageren. Wie het eerst reageert,
    staat bovenaan de lijst.
    """

    lotingmodel = Referentiedata(
        code="LOT",
        naam="Lotingmodel",
    )
    """
    Vastgoed wordt verloot onder geïnteresseerde woningzoekenden. Hierbij kan ook sprake
    zijn van 'gewogen' loting of andere combinaties van spelregels.
    """

    optiemodel = Referentiedata(
        code="OPT",
        naam="Optiemodel",
    )
    """
    Woningzoekenden kunnen zichzelf op een wachtlijst zetten voor een cluster van
    vastgoed. Zodra een eenheid vrijkomt krijgt de woningzoekende met de hoogste
    positie de eenheid aangeboden.
    """

    vrijesectormodel = Referentiedata(
        code="VRI",
        naam="Vrijesectormodel",
    )
    """
    Vastgoed wordt regelvrij aangeboden aan alle woningzoekenden. Deze kunnen vervolgens
    hun interesse aangeven voor het vastgoed. Voor het betrekken van de woning
    kunnen overigens wel degelijk eisen gesteld worden (bijv. minimaal inkomen.)
    """

    woningruilmodel = Referentiedata(
        code="WON",
        naam="Woningruilmodel",
    )
    """
    Woningzoekenden kunnen onderling eenheden ruilen.
    """

    @property
    def code(self) -> str:
        if self.value.code is None:
            raise TypeError("de code van een Referentiedata object mag niet None zijn")
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
