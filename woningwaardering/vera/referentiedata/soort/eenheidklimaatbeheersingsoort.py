from vera.referentiedata.models import Referentiedata


class Eenheidklimaatbeheersingsoort:
    individueel = Referentiedata(
        code="IND",
        naam="Individueel",
    )

    collectief = Referentiedata(
        code="COL",
        naam="Collectief",
    )
