from woningwaardering.vera.bvg.models import Referentiedata


class GESLACHT:
    mannelijk = Referentiedata(
        code="M",
        naam="Mannelijk",
    )
    """
    Mannelijk geslacht
    """

    neutraal = Referentiedata(
        code="N",
        naam="Neutraal",
    )
    """
    Gender-neutraal
    """

    vrouwelijk = Referentiedata(
        code="V",
        naam="Vrouwelijk",
    )
    """
    Vrouwelijk geslacht
    """
