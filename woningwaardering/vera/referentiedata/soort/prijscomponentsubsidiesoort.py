from woningwaardering.vera.bvg.generated import Referentiedata


class Prijscomponentsubsidiesoort:
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
    subsidiabel: SCH - Schoonmaak van gemeenschappelijke ruimten / ENE - Energie voor
    gemeenschappelijke ruimten /  HUI - Huismeester / DIE - Dienst- en recreatieruimten
    """
