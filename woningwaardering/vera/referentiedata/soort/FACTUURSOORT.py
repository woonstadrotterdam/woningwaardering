
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class FACTUURSOORT:

    credit_factuur_extern = Referentiedata(
        code="CEX",
        naam="Credit factuur extern",
    )
    # credit_factuur_extern = ("CEX", "Credit factuur extern")
    """
    Credit factuur extern
    """

    credit_factuur_intern = Referentiedata(
        code="CIF",
        naam="Credit factuur intern",
    )
    # credit_factuur_intern = ("CIF", "Credit factuur intern")
    """
    Credit factuur intern
    """

    debet_factuur_extern = Referentiedata(
        code="DEX",
        naam="Debet factuur extern",
    )
    # debet_factuur_extern = ("DEX", "Debet factuur extern")
    """
    Debet factuur extern
    """

    debet_factuur_intern = Referentiedata(
        code="DIF",
        naam="Debet factuur intern",
    )
    # debet_factuur_intern = ("DIF", "Debet factuur intern")
    """
    Debet factuur intern
    """
