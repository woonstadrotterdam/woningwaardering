
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class LENINGSOORT:

    kredietfaciliteit = Referentiedata(
        code="KRE",
        naam="Kredietfaciliteit",
    )
    # kredietfaciliteit = ("KRE", "Kredietfaciliteit")

    lening = Referentiedata(
        code="LEN",
        naam="Lening",
    )
    # lening = ("LEN", "Lening")
