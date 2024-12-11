from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class GeslachtReferentiedata(Referentiedata):
    pass


class Geslacht(Referentiedatasoort):
    mannelijk = GeslachtReferentiedata(
        code="M",
        naam="Mannelijk",
    )
    """
    Mannelijk geslacht
    """

    onbekend = GeslachtReferentiedata(
        code="O",
        naam="Onbekend",
    )
    """
    Manier om genderneutraal aan te duiden of wanneer geslacht niet ter zake doet.
    """

    vrouwelijk = GeslachtReferentiedata(
        code="V",
        naam="Vrouwelijk",
    )
    """
    Vrouwelijk geslacht
    """
