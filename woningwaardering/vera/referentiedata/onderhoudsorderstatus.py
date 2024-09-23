from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata


class Onderhoudsorderstatus(Enum):
    afgehandeld = Referentiedata(
        code="AFG",
        naam="Afgehandeld",
    )
    """
    De order is volledig technisch en financieel afgehandeld
    """

    financieel_afwikkelen = Referentiedata(
        code="FIN",
        naam="Financieel afwikkelen",
    )
    """
    De order is technisch beoordeeld  en akkoord voor financiele afwikkeling. Op dat
    moment kan een eventueel externe onderhoudspartner de facturatie verzorgen van
    de onderhoudsorder
    """

    geannuleerd = Referentiedata(
        code="GEA",
        naam="Geannuleerd",
    )
    """
    De order is geannuleerd
    """

    order_gegund = Referentiedata(
        code="GUN",
        naam="Order gegund",
    )
    """
    De order is verstrekt aan de uitvoerende partij
    """

    in_behandeling = Referentiedata(
        code="INB",
        naam="In behandeling",
    )
    """
    De order is opgepakt door de uitvoerende partij (vakgroep of externe
    onderhoudspartner) nadat deze gepland is. Deze status kan ook gebruikt worden
    als algemene status voor het in behandeling hebben van de order door de
    uitvoerende partij (geen differentiatie tussen gegeund, gepland, etc)
    """

    offertetraject = Referentiedata(
        code="OFF",
        naam="Offertetraject",
    )
    """
    Voor de order loopt een offertetraject bij 1 of meerdere partijen voordat gestart
    wordt met de uitvoering van de werkzaamheden.
    """

    order_gepland = Referentiedata(
        code="PLN",
        naam="Order gepland",
    )
    """
    De order is gepland door de uitvoerende partij
    """

    geregistreerd = Referentiedata(
        code="REG",
        naam="Geregistreerd",
    )
    """
    De onderhoudsorder is slechts geregistreerd/vastgelegd
    """

    order_in_steekproef = Referentiedata(
        code="STE",
        naam="Order in steekproef",
    )
    """
    De order is na uitvoering van de werkzaamheden in de steekproef gevallen en moet
    worden beoordeeld door de corporatie
    """

    technisch_gereed = Referentiedata(
        code="TEC",
        naam="Technisch gereed",
    )
    """
    De order is technisch gereed en de uitvoering kan inhoudelijk beoordeeld worden
    """

    wacht_op_goedkeuring = Referentiedata(
        code="WOG",
        naam="Wacht op goedkeuring",
    )
    """
    Order wordt voordat deze gegund kan worden intern eerst beoordeeld.
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
