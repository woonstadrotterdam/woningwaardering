
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class UITVOERENDESOORT:

    leverancier = Referentiedata(
        code="LEV",
        naam="Leverancier",
    )
    # leverancier = ("LEV", "Leverancier")
    """
    Uitvoering vindt plaats door een externe partij
    """

    vakgroep = Referentiedata(
        code="VAK",
        naam="Vakgroep",
    )
    # vakgroep = ("VAK", "Vakgroep")
    """
    Uitvoering vindt plaats door een interne vakgroep / eigen dienst
    """
