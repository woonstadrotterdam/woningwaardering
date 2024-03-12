
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class EXTERNEINCASSOSOORT:

    deurwaarder = Referentiedata(
        code="DEU",
        naam="Deurwaarder",
    )
    # deurwaarder = ("DEU", "Deurwaarder")

    incassobureau = Referentiedata(
        code="INC",
        naam="Incassobureau",
    )
    # incassobureau = ("INC", "Incassobureau")
