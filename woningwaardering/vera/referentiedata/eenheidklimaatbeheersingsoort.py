from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EenheidklimaatbeheersingsoortReferentiedata(Referentiedata):
    pass


class Eenheidklimaatbeheersingsoort(Referentiedatasoort):
    individueel = EenheidklimaatbeheersingsoortReferentiedata(
        code="IND",
        naam="Individueel",
    )

    collectief = EenheidklimaatbeheersingsoortReferentiedata(
        code="COL",
        naam="Collectief",
    )
