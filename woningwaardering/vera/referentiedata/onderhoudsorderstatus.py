from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class OnderhoudsorderstatusReferentiedata(Referentiedata):
    pass


class Onderhoudsorderstatus(Referentiedatasoort):
    afgehandeld = OnderhoudsorderstatusReferentiedata(
        code="AFG",
        naam="Afgehandeld",
    )
    """
    De order is volledig technisch en financieel afgehandeld
    """

    financieel_afwikkelen = OnderhoudsorderstatusReferentiedata(
        code="FIN",
        naam="Financieel afwikkelen",
    )
    """
    De order is technisch beoordeeld  en akkoord voor financiele afwikkeling. Op dat
    moment kan een eventueel externe onderhoudspartner de facturatie verzorgen van
    de onderhoudsorder
    """

    geannuleerd = OnderhoudsorderstatusReferentiedata(
        code="GEA",
        naam="Geannuleerd",
    )
    """
    De order is geannuleerd
    """

    order_gegund = OnderhoudsorderstatusReferentiedata(
        code="GUN",
        naam="Order gegund",
    )
    """
    De order is verstrekt aan de uitvoerende partij
    """

    in_behandeling = OnderhoudsorderstatusReferentiedata(
        code="INB",
        naam="In behandeling",
    )
    """
    De order is opgepakt door de uitvoerende partij (vakgroep of externe
    onderhoudspartner) nadat deze gepland is. Deze status kan ook gebruikt worden
    als algemene status voor het in behandeling hebben van de order door de
    uitvoerende partij (geen differentiatie tussen gegeund, gepland, etc)
    """

    offertetraject = OnderhoudsorderstatusReferentiedata(
        code="OFF",
        naam="Offertetraject",
    )
    """
    Voor de order loopt een offertetraject bij 1 of meerdere partijen voordat gestart
    wordt met de uitvoering van de werkzaamheden.
    """

    order_gepland = OnderhoudsorderstatusReferentiedata(
        code="PLN",
        naam="Order gepland",
    )
    """
    De order is gepland door de uitvoerende partij
    """

    geregistreerd = OnderhoudsorderstatusReferentiedata(
        code="REG",
        naam="Geregistreerd",
    )
    """
    De onderhoudsorder is slechts geregistreerd/vastgelegd
    """

    order_in_steekproef = OnderhoudsorderstatusReferentiedata(
        code="STE",
        naam="Order in steekproef",
    )
    """
    De order is na uitvoering van de werkzaamheden in de steekproef gevallen en moet
    worden beoordeeld door de corporatie
    """

    technisch_gereed = OnderhoudsorderstatusReferentiedata(
        code="TEC",
        naam="Technisch gereed",
    )
    """
    De order is technisch gereed en de uitvoering kan inhoudelijk beoordeeld worden
    """

    wacht_op_goedkeuring = OnderhoudsorderstatusReferentiedata(
        code="WOG",
        naam="Wacht op goedkeuring",
    )
    """
    Order wordt voordat deze gegund kan worden intern eerst beoordeeld.
    """
