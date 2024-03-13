from woningwaardering.vera.bvg.models import Referentiedata


class GEOMETRIESOORT:
    omtrek = Referentiedata(
        code="OMT",
        naam="Omtrek",
    )
    """
    De geocoördinaten van de omtrek van een object
    """

    punt = Referentiedata(
        code="PUN",
        naam="Punt",
    )
    """
    De geocoördinaten van het middenpunt van een object
    """
