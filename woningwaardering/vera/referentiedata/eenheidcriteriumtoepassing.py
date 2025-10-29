from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EenheidcriteriumtoepassingReferentiedata(Referentiedata):
    pass


class Eenheidcriteriumtoepassing(Referentiedatasoort):
    selectie = EenheidcriteriumtoepassingReferentiedata(
        code="SEL",
        naam="Selectie",
    )
    """
    Selectiecriteria die worden gebruikt om de passendheid van een woningzoekende voor
    de eenheid te bepalen.
    """

    sortering = EenheidcriteriumtoepassingReferentiedata(
        code="SOR",
        naam="Sortering",
    )
    """
    Sorteercriteria die worden gebruikt om de positie van een woningzoekende voor de
    eenheid te bepalen.
    """
