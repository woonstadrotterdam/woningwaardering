from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Geslacht(Referentiedatasoort):
    mannelijk = Referentiedata(
        code="M",
        naam="Mannelijk",
    )
    """
    Mannelijk geslacht
    """

    onbekend = Referentiedata(
        code="O",
        naam="Onbekend",
    )
    """
    Manier om genderneutraal aan te duiden of wanneer geslacht niet ter zake doet.
    """

    vrouwelijk = Referentiedata(
        code="V",
        naam="Vrouwelijk",
    )
    """
    Vrouwelijk geslacht
    """
