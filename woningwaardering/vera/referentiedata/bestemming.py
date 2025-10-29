from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BestemmingReferentiedata(Referentiedata):
    pass


class Bestemming(Referentiedatasoort):
    huur = BestemmingReferentiedata(
        code="HUU",
        naam="Huur",
    )
    """
    Eenheid is bestemd voor verhuur bij mutatie.
    """

    koop = BestemmingReferentiedata(
        code="KOO",
        naam="Koop",
    )
    """
    Eenheid is bestemd voor verkoop bij mutatie.
    """

    sloop = BestemmingReferentiedata(
        code="SLO",
        naam="Sloop",
    )
    """
    Eenheid is bestemd voor sloop bij mutatie.
    """
