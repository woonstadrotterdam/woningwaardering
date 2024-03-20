from woningwaardering.vera.bvg.generated import Referentiedata


class Factuurbetaalwijze:
    automatische_incasso = Referentiedata(
        code="AIN",
        naam="Automatische incasso",
    )
    """
    Factuur wordt voldaan middels automatische incasso betaling.
    """

    contant = Referentiedata(
        code="CNT",
        naam="Contant",
    )
    """
    Factuur word voldaan middels contante betaling
    """

    op_rekening = Referentiedata(
        code="ORN",
        naam="Op rekening",
    )
    """
    Factuur wordt niet direct voldaan maar op rekening gezet. De rekening wordt (bijv.
    maandelijks) als 1 factuur aangeboden.
    """
