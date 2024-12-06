from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Leningsoort(Referentiedatasoort):
    kredietfaciliteit = Referentiedata(
        code="KRE",
        naam="Kredietfaciliteit",
    )

    lening = Referentiedata(
        code="LEN",
        naam="Lening",
    )
