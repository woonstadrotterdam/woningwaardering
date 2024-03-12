
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class PROJECTBUDGETREGELSOORT:

    budget = Referentiedata(
        code="BUD",
        naam="Budget",
    )
    # budget = ("BUD", "Budget")
    """
    Projectbudgetregel betreft een budgetbedrag
    """

    prognose = Referentiedata(
        code="PRO",
        naam="Prognose",
    )
    # prognose = ("PRO", "Prognose")
    """
    Projectbudgetregel betreft een prognose-bedrag
    """
