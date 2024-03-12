
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class OPZEGTERMIJN:

    opzegtermijn_12_maanden = Referentiedata(
        code="12M",
        naam="12 maanden",
    )
    # opzegtermijn_12_maanden = ("12M", "12 maanden")
    """
    Voor de overeenkomst geldt een opzegtermijn van 12 maanden.
    """

    opzegtermijn_14_dagen = Referentiedata(
        code="14D",
        naam="14 dagen",
    )
    # opzegtermijn_14_dagen = ("14D", "14 dagen")
    """
    Voor de overeenkomst geldt een opzegtermijn van 14 dagen.
    """

    opzegtermijn_1_maand = Referentiedata(
        code="1M",
        naam="1 maand",
    )
    # opzegtermijn_1_maand = ("1M", "1 maand")
    """
    Voor de overeenkomst geldt een opzegtermijn van 1 maand.
    """

    opzegtermijn_2_maanden = Referentiedata(
        code="2M",
        naam="2 maanden",
    )
    # opzegtermijn_2_maanden = ("2M", "2 maanden")
    """
    Voor de overeenkomst geldt een opzegtermijn van 2 maanden.
    """

    opzegtermijn_3_maanden = Referentiedata(
        code="3M",
        naam="3 maanden",
    )
    # opzegtermijn_3_maanden = ("3M", "3 maanden")
    """
    Voor de overeenkomst geldt een opzegtermijn van 3 maanden.
    """

    opzegtermijn_4_weken = Referentiedata(
        code="4W",
        naam="4 weken",
    )
    # opzegtermijn_4_weken = ("4W", "4 weken")
    """
    Voor de overeenkomst geldt een opzegtermijn van 4 weken.
    """

    opzegtermijn_6_maanden = Referentiedata(
        code="6M",
        naam="6 maanden",
    )
    # opzegtermijn_6_maanden = ("6M", "6 maanden")
    """
    Voor de overeenkomst geldt een opzegtermijn van 6 maanden.
    """
