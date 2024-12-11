from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EenheidcriteriasoortReferentiedata(Referentiedata):
    pass


class Eenheidcriteriasoort(Referentiedatasoort):
    selectie = EenheidcriteriasoortReferentiedata(
        code="SEL",
        naam="Selectie",
    )
    """
    Selectiecriteria die worden gebruikt om de passendheid van een woningzoekende voor
    de eenheid te bepalen.
    """

    sortering = EenheidcriteriasoortReferentiedata(
        code="SOR",
        naam="Sortering",
    )
    """
    Sorteercriteria die worden gebruikt om de positie van een woningzoekende voor de
    eenheid te bepalen.
    """
