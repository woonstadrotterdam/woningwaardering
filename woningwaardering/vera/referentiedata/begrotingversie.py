from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class BegrotingversieReferentiedata(Referentiedata):
    pass


class Begrotingversie(Referentiedatasoort):
    actueel_budget = BegrotingversieReferentiedata(
        code="ACB",
        naam="Actueel budget",
    )
    """
    Som van mutatie en oorspronkelijk budget van een budgetregel voor een jaar of
    periode.
    """

    mutatie_budget = BegrotingversieReferentiedata(
        code="MUB",
        naam="Mutatie budget",
    )
    """
    Gewijzigd bedrag van een budgetregel voor een jaar of periode.
    """

    oorspronkelijk_budget = BegrotingversieReferentiedata(
        code="OOB",
        naam="Oorspronkelijk budget",
    )
    """
    Oorspronkelijk bedrag van een budgetregel voor een jaar of een periode.
    """
