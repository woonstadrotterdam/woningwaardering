
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class LENINGAFLOSVORM:

    annuitair = Referentiedata(
        code="ANN",
        naam="Annuitair",
    )
    # annuitair = ("ANN", "Annuitair")
    """
    Jaarlijks wordt met deze vorm een vast bedrag afgelost. Samenstelling van rente en
    aflossing.
    """

    fixe = Referentiedata(
        code="FIX",
        naam="Fixe",
    )
    # fixe = ("FIX", "Fixe")

    lineair = Referentiedata(
        code="LIN",
        naam="Lineair",
    )
    # lineair = ("LIN", "Lineair")
    """
    Met deze vorm van lenen wordt een vast bedrag als aflossing betaald. Hierdoor wordt
    de totale lasten (rente + aflossing) steeds lager.
    """
