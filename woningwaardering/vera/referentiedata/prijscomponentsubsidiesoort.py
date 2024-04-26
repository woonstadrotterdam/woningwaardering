from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Prijscomponentsubsidiesoort(Enum):
    niet_subsidiabel_prijscomponent = Referentiedata(
        code="NSU",
        naam="Niet subsidiabel prijscomponent",
    )
    """
    Het prijscomponent komt NIET in aanmerking voor subsidie omdat deze niet opgenomen
    is in de Wet op de huurtoeslag
    """

    subsidiabel_prijscomponent = Referentiedata(
        code="SUB",
        naam="Subsidiabel prijscomponent",
    )
    """
    Het prijscomponent komt in aanmerking voor subsidie en valt binnen de Wet op de
    huurtoeslag.  Gebruik eventueel PRIJSCOMPONENTDETAILSOORT om een nadere
    verbijzondering aan te duiden. De volgende prijscomponentdetailsoorten zijn
    subsidiabel: SCH - Schoonmaak van gemeenschappelijke ruimten / ENE - Energie
    voor gemeenschappelijke ruimten /  HUI - Huismeester / DIE - Dienst- en
    recreatieruimten
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
