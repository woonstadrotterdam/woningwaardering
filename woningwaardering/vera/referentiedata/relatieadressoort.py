from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Relatieadressoort(Referentiedatasoort):
    bezoekadres = Referentiedata(
        code="BEZ",
        naam="Bezoekadres",
    )

    factuuradres = Referentiedata(
        code="FAC",
        naam="Factuuradres",
    )

    leveringsadres = Referentiedata(
        code="LEV",
        naam="Leveringsadres",
    )
    """
    Het adres waar eventuele goederen afgeleverd of bezorgd dienen te worden.
    """

    postadres = Referentiedata(
        code="POS",
        naam="Postadres",
    )

    woonadres = Referentiedata(
        code="WOO",
        naam="Woonadres",
    )
