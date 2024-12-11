from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ZaakobjectsoortReferentiedata(Referentiedata):
    pass


class Zaakobjectsoort(Referentiedatasoort):
    cluster = ZaakobjectsoortReferentiedata(
        code="CLU",
        naam="Cluster",
    )

    collectief_object = ZaakobjectsoortReferentiedata(
        code="COL",
        naam="Collectief object",
    )

    eenheid = ZaakobjectsoortReferentiedata(
        code="EEN",
        naam="Eenheid",
    )

    onderhoudsverzoek = ZaakobjectsoortReferentiedata(
        code="OND",
        naam="Onderhoudsverzoek",
    )

    overeenkomst = ZaakobjectsoortReferentiedata(
        code="OVE",
        naam="Overeenkomst",
    )
