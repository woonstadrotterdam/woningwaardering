from vera.referentiedata.models import Referentiedata


class Eenheidcriteriumtoepassing:
    selectie = Referentiedata(
        code="SEL",
        naam="Selectie",
    )
    """
    Selectiecriteria die worden gebruikt om de passendheid van een woningzoekende voor
    de eenheid te bepalen.
    """

    sortering = Referentiedata(
        code="SOR",
        naam="Sortering",
    )
    """
    Sorteercriteria die worden gebruikt om de positie van een woningzoekende voor de
    eenheid te bepalen.
    """
