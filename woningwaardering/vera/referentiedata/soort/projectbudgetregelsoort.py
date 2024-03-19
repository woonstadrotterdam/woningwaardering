from vera.bvg.generated import Referentiedata


class Projectbudgetregelsoort:
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
