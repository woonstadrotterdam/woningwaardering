from vera.referentiedata.models import Referentiedata


class Geslacht:
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
