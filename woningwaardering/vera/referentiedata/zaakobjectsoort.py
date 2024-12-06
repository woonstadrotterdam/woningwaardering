from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Zaakobjectsoort(Referentiedatasoort):
    cluster = Referentiedata(
        code="CLU",
        naam="Cluster",
    )

    collectief_object = Referentiedata(
        code="COL",
        naam="Collectief object",
    )

    eenheid = Referentiedata(
        code="EEN",
        naam="Eenheid",
    )

    onderhoudsverzoek = Referentiedata(
        code="OND",
        naam="Onderhoudsverzoek",
    )

    overeenkomst = Referentiedata(
        code="OVE",
        naam="Overeenkomst",
    )
