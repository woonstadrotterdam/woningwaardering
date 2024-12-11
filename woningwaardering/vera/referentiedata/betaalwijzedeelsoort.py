from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BetaalwijzedeelsoortReferentiedata(Referentiedata):
    pass


class Betaalwijzedeelsoort(Referentiedatasoort):
    maximaal_bedrag = BetaalwijzedeelsoortReferentiedata(
        code="MAX",
        naam="Maximaal bedrag",
    )
    """
    Het maximale bedrag dat door de betaler wordt bijgedragen aan de huur. Bijvoorbeeld
    de ouders van de student dragen maximaal EUR 300 bij aan de huur.
    """

    percentage = BetaalwijzedeelsoortReferentiedata(
        code="PER",
        naam="Percentage",
    )
    """
    Het percentage van de huur dat door de betaler wordt bijgedragen. Bijvoorbeeld een
    stel waarbij beiden de helft van de huur betalen.
    """

    restant_bedrag = BetaalwijzedeelsoortReferentiedata(
        code="RES",
        naam="Restant bedrag",
    )
    """
    Het restant van de huur dat door de betreffende betaler wordt bijgedragen.
    Bijvoorbeeld de student die het restant van de huur betaalt na aftrek van de
    bijdrage van zijn/haar ouders.
    """
