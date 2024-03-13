from woningwaardering.vera.bvg.models import Referentiedata


class EENHEIDKLIMAATBEHEERSINGSOORT:
    individueel = Referentiedata(
        code="IND",
        naam="Individueel",
    )

    collectief = Referentiedata(
        code="COL",
        naam="Collectief",
    )
