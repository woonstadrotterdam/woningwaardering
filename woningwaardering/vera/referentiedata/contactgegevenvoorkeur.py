from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Contactgegevenvoorkeur(Referentiedatasoort):
    eerste = Referentiedata(
        code="EER",
        naam="Eerste",
    )

    tweede = Referentiedata(
        code="TWE",
        naam="Tweede",
    )
