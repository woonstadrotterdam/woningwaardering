from woningwaardering.vera.bvg.generated import Referentiedata


class Relatieadressoort:
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
