from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Eenheidklimaatbeheersingsoort(Referentiedatasoort):
    individueel = Referentiedata(
        code="IND",
        naam="Individueel",
    )

    collectief = Referentiedata(
        code="COL",
        naam="Collectief",
    )
