
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class GEOMETRIESOORT:

    omtrek = Referentiedata(
        code="OMT",
        naam="Omtrek",
    )
    # omtrek = ("OMT", "Omtrek")
    """
    De geocoördinaten van de omtrek van een object
    """

    punt = Referentiedata(
        code="PUN",
        naam="Punt",
    )
    # punt = ("PUN", "Punt")
    """
    De geocoördinaten van het middenpunt van een object
    """
