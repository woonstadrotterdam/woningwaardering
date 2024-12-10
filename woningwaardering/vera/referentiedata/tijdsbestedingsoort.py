from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class TijdsbestedingsoortReferentiedata(Referentiedata):
    pass


class Tijdsbestedingsoort(Referentiedatasoort):
    declarabel = TijdsbestedingsoortReferentiedata(
        code="DEC",
        naam="Declarabel",
    )

    niet_declarabel = TijdsbestedingsoortReferentiedata(
        code="NDE",
        naam="Niet declarabel",
    )

    afwezig = TijdsbestedingsoortReferentiedata(
        code="AFW",
        naam="Afwezig",
    )
