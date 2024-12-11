from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ExterneincassosoortReferentiedata(Referentiedata):
    pass


class Externeincassosoort(Referentiedatasoort):
    deurwaarder = ExterneincassosoortReferentiedata(
        code="DEU",
        naam="Deurwaarder",
    )

    incassobureau = ExterneincassosoortReferentiedata(
        code="INC",
        naam="Incassobureau",
    )
