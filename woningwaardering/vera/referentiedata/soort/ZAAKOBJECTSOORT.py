
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class ZAAKOBJECTSOORT:

    cluster = Referentiedata(
        code="CLU",
        naam="Cluster",
    )
    # cluster = ("CLU", "Cluster")

    collectief_object = Referentiedata(
        code="COL",
        naam="Collectief object",
    )
    # collectief_object = ("COL", "Collectief object")

    eenheid = Referentiedata(
        code="EEN",
        naam="Eenheid",
    )
    # eenheid = ("EEN", "Eenheid")

    onderhoudsverzoek = Referentiedata(
        code="OND",
        naam="Onderhoudsverzoek",
    )
    # onderhoudsverzoek = ("OND", "Onderhoudsverzoek")

    overeenkomst = Referentiedata(
        code="OVE",
        naam="Overeenkomst",
    )
    # overeenkomst = ("OVE", "Overeenkomst")
