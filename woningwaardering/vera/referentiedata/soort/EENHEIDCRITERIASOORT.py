
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class EENHEIDCRITERIASOORT:

    selectie = Referentiedata(
        code="SEL",
        naam="Selectie",
    )
    # selectie = ("SEL", "Selectie")
    """
    Selectiecriteria die worden gebruikt om de passendheid van een woningzoekende voor
    de eenheid te bepalen.
    """

    sortering = Referentiedata(
        code="SOR",
        naam="Sortering",
    )
    # sortering = ("SOR", "Sortering")
    """
    Sorteercriteria die worden gebruikt om de positie van een woningzoekende voor de
    eenheid te bepalen.
    """
