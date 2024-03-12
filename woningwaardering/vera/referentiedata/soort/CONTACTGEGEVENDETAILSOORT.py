
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class CONTACTGEGEVENDETAILSOORT:

    in_case_of_emergency = Referentiedata(
        code="ICE",
        naam="In case of emergency",
    )
    # in_case_of_emergency = ("ICE", "In case of emergency")

    prive = Referentiedata(
        code="PRI",
        naam="Privé",
    )
    # prive = ("PRI", "Privé")

    zakelijk = Referentiedata(
        code="ZAK",
        naam="Zakelijk",
    )
    # zakelijk = ("ZAK", "Zakelijk")
