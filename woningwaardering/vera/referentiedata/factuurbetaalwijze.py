from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class FactuurbetaalwijzeReferentiedata(Referentiedata):
    pass


class Factuurbetaalwijze(Referentiedatasoort):
    automatische_incasso = FactuurbetaalwijzeReferentiedata(
        code="AIN",
        naam="Automatische incasso",
    )
    """
    Factuur wordt voldaan middels automatische incasso betaling.
    """

    contant = FactuurbetaalwijzeReferentiedata(
        code="CNT",
        naam="Contant",
    )
    """
    Factuur word voldaan middels contante betaling
    """

    op_rekening = FactuurbetaalwijzeReferentiedata(
        code="ORN",
        naam="Op rekening",
    )
    """
    Factuur wordt niet direct voldaan maar op rekening gezet. De rekening wordt (bijv.
    maandelijks) als 1 factuur aangeboden.
    """
