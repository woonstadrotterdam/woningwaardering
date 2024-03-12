
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class FACTUURBETAALWIJZE:

    automatische_incasso = Referentiedata(
        code="AIN",
        naam="Automatische incasso",
    )
    # automatische_incasso = ("AIN", "Automatische incasso")
    """
    Factuur wordt voldaan middels automatische incasso betaling.
    """

    contant = Referentiedata(
        code="CNT",
        naam="Contant",
    )
    # contant = ("CNT", "Contant")
    """
    Factuur word voldaan middels contante betaling
    """

    op_rekening = Referentiedata(
        code="ORN",
        naam="Op rekening",
    )
    # op_rekening = ("ORN", "Op rekening")
    """
    Factuur wordt niet direct voldaan maar op rekening gezet. De rekening wordt (bijv.
    maandelijks) als 1 factuur aangeboden.
    """
