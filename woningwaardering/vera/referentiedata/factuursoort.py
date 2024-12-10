from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class FactuursoortReferentiedata(Referentiedata):
    pass


class Factuursoort(Referentiedatasoort):
    credit_factuur_extern = FactuursoortReferentiedata(
        code="CEX",
        naam="Credit factuur extern",
    )
    """
    Credit factuur extern
    """

    credit_factuur_intern = FactuursoortReferentiedata(
        code="CIF",
        naam="Credit factuur intern",
    )
    """
    Credit factuur intern
    """

    debet_factuur_extern = FactuursoortReferentiedata(
        code="DEX",
        naam="Debet factuur extern",
    )
    """
    Debet factuur extern
    """

    debet_factuur_intern = FactuursoortReferentiedata(
        code="DIF",
        naam="Debet factuur intern",
    )
    """
    Debet factuur intern
    """
