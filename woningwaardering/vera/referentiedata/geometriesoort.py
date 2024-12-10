from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class GeometriesoortReferentiedata(Referentiedata):
    pass


class Geometriesoort(Referentiedatasoort):
    omtrek = GeometriesoortReferentiedata(
        code="OMT",
        naam="Omtrek",
    )
    """
    De geocoördinaten van de omtrek van een object
    """

    punt = GeometriesoortReferentiedata(
        code="PUN",
        naam="Punt",
    )
    """
    De geocoördinaten van het middenpunt van een object
    """
