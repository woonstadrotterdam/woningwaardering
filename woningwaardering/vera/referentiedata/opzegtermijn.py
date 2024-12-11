from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class OpzegtermijnReferentiedata(Referentiedata):
    pass


class Opzegtermijn(Referentiedatasoort):
    opzegtermijn_12_maanden = OpzegtermijnReferentiedata(
        code="12M",
        naam="12 maanden",
    )
    """
    Voor de overeenkomst geldt een opzegtermijn van 12 maanden.
    """

    opzegtermijn_14_dagen = OpzegtermijnReferentiedata(
        code="14D",
        naam="14 dagen",
    )
    """
    Voor de overeenkomst geldt een opzegtermijn van 14 dagen.
    """

    opzegtermijn_1_maand = OpzegtermijnReferentiedata(
        code="1M",
        naam="1 maand",
    )
    """
    Voor de overeenkomst geldt een opzegtermijn van 1 maand.
    """

    opzegtermijn_2_maanden = OpzegtermijnReferentiedata(
        code="2M",
        naam="2 maanden",
    )
    """
    Voor de overeenkomst geldt een opzegtermijn van 2 maanden.
    """

    opzegtermijn_3_maanden = OpzegtermijnReferentiedata(
        code="3M",
        naam="3 maanden",
    )
    """
    Voor de overeenkomst geldt een opzegtermijn van 3 maanden.
    """

    opzegtermijn_4_weken = OpzegtermijnReferentiedata(
        code="4W",
        naam="4 weken",
    )
    """
    Voor de overeenkomst geldt een opzegtermijn van 4 weken.
    """

    opzegtermijn_6_maanden = OpzegtermijnReferentiedata(
        code="6M",
        naam="6 maanden",
    )
    """
    Voor de overeenkomst geldt een opzegtermijn van 6 maanden.
    """
