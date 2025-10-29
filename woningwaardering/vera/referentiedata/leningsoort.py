from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class LeningsoortReferentiedata(Referentiedata):
    pass


class Leningsoort(Referentiedatasoort):
    kredietfaciliteit = LeningsoortReferentiedata(
        code="KRE",
        naam="Kredietfaciliteit",
    )

    lening = LeningsoortReferentiedata(
        code="LEN",
        naam="Lening",
    )
