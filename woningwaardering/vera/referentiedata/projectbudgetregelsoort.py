from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ProjectbudgetregelsoortReferentiedata(Referentiedata):
    pass


class Projectbudgetregelsoort(Referentiedatasoort):
    budget = ProjectbudgetregelsoortReferentiedata(
        code="BUD",
        naam="Budget",
    )
    """
    Projectbudgetregel betreft een budgetbedrag
    """

    prognose = ProjectbudgetregelsoortReferentiedata(
        code="PRO",
        naam="Prognose",
    )
    """
    Projectbudgetregel betreft een prognose-bedrag
    """
