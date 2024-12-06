from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Tijdsbestedingsoort(Referentiedatasoort):
    declarabel = Referentiedata(
        code="DEC",
        naam="Declarabel",
    )

    niet_declarabel = Referentiedata(
        code="NDE",
        naam="Niet declarabel",
    )

    afwezig = Referentiedata(
        code="AFW",
        naam="Afwezig",
    )
