from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Externeincassosoort(Referentiedatasoort):
    deurwaarder = Referentiedata(
        code="DEU",
        naam="Deurwaarder",
    )

    incassobureau = Referentiedata(
        code="INC",
        naam="Incassobureau",
    )
