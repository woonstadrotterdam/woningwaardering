
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class BOEKJAARPERIODESTATUS:

    gesloten_periode = Referentiedata(
        code="GSP",
        naam="Gesloten periode",
    )
    # gesloten_periode = ("GSP", "Gesloten periode")
    """
    Periode waarin gegevens niet meer kunnen worden gewijzigd, tiegevoegd of verwijderd.
    """

    open_periode = Referentiedata(
        code="OPP",
        naam="Open periode",
    )
    # open_periode = ("OPP", "Open periode")
    """
    Periode waarin gegevens kunnen worden gewijzigd, tiegevoegd of verwijderd.
    """
