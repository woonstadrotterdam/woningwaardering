
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class GESLACHT:

    mannelijk = Referentiedata(
        code="M",
        naam="Mannelijk",
    )
    # mannelijk = ("M", "Mannelijk")
    """
    Mannelijk geslacht
    """

    neutraal = Referentiedata(
        code="N",
        naam="Neutraal",
    )
    # neutraal = ("N", "Neutraal")
    """
    Gender-neutraal
    """

    vrouwelijk = Referentiedata(
        code="V",
        naam="Vrouwelijk",
    )
    # vrouwelijk = ("V", "Vrouwelijk")
    """
    Vrouwelijk geslacht
    """
