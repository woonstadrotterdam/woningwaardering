
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class RELATIEADRESSOORT:

    bezoekadres = Referentiedata(
        code="BEZ",
        naam="Bezoekadres",
    )
    # bezoekadres = ("BEZ", "Bezoekadres")

    factuuradres = Referentiedata(
        code="FAC",
        naam="Factuuradres",
    )
    # factuuradres = ("FAC", "Factuuradres")

    leveringsadres = Referentiedata(
        code="LEV",
        naam="Leveringsadres",
    )
    # leveringsadres = ("LEV", "Leveringsadres")
    """
    Het adres waar eventuele goederen afgeleverd of bezorgd dienen te worden.
    """

    postadres = Referentiedata(
        code="POS",
        naam="Postadres",
    )
    # postadres = ("POS", "Postadres")

    woonadres = Referentiedata(
        code="WOO",
        naam="Woonadres",
    )
    # woonadres = ("WOO", "Woonadres")
