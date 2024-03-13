from woningwaardering.vera.bvg.models import Referentiedata


class PROJECTBUDGETREGELSOORT:
    budget = Referentiedata(
        code="BUD",
        naam="Budget",
    )
    """
    Projectbudgetregel betreft een budgetbedrag
    """

    prognose = Referentiedata(
        code="PRO",
        naam="Prognose",
    )
    """
    Projectbudgetregel betreft een prognose-bedrag
    """
