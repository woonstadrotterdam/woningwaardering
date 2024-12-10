from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class RelatieadressoortReferentiedata(Referentiedata):
    pass


class Relatieadressoort(Referentiedatasoort):
    bezoekadres = RelatieadressoortReferentiedata(
        code="BEZ",
        naam="Bezoekadres",
    )

    factuuradres = RelatieadressoortReferentiedata(
        code="FAC",
        naam="Factuuradres",
    )

    leveringsadres = RelatieadressoortReferentiedata(
        code="LEV",
        naam="Leveringsadres",
    )
    """
    Het adres waar eventuele goederen afgeleverd of bezorgd dienen te worden.
    """

    postadres = RelatieadressoortReferentiedata(
        code="POS",
        naam="Postadres",
    )

    woonadres = RelatieadressoortReferentiedata(
        code="WOO",
        naam="Woonadres",
    )
