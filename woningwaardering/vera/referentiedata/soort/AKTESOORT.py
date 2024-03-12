
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class AKTESOORT:

    notariele_akte = Referentiedata(
        code="NOT",
        naam="Notariële akte",
    )
    # notariele_akte = ("NOT", "Notariële akte")
    """
    Akte vastgelegd bij de notaris.
    """

    onderhandse_akte = Referentiedata(
        code="OND",
        naam="Onderhandse akte",
    )
    # onderhandse_akte = ("OND", "Onderhandse akte")
    """
    Akte die door twee of meer partijen is vastgesteld (onderhands)
    """
