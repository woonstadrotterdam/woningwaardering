
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class HUURGESCHILSTATUS:

    afgewezen = Referentiedata(
        code="AFG",
        naam="Afgewezen",
    )
    # afgewezen = ("AFG", "Afgewezen")
    """
    Het huurgeschil is afgewezen, en daarmee tevens afgehandeld
    """

    in_behandeling = Referentiedata(
        code="INB",
        naam="In behandeling",
    )
    # in_behandeling = ("INB", "In behandeling")
    """
    Het huurgeschil is (nog) in behandeling
    """

    toegekend = Referentiedata(
        code="TOE",
        naam="Toegekend",
    )
    # toegekend = ("TOE", "Toegekend")
    """
    Het huurgeschil is toegekend, en daarmee tevens afgehandeld
    """
