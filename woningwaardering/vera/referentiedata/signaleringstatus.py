from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Signaleringstatus(Referentiedatasoort):
    actief = Referentiedata(
        code="ACT",
        naam="Actief",
    )

    passief = Referentiedata(
        code="PAS",
        naam="Passief",
    )

    vervallen = Referentiedata(
        code="VER",
        naam="Vervallen",
    )
