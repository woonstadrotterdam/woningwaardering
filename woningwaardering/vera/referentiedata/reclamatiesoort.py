from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ReclamatiesoortReferentiedata(Referentiedata):
    pass


class Reclamatiesoort(Referentiedatasoort):
    bezwaar = ReclamatiesoortReferentiedata(
        code="BEZ",
        naam="Bezwaar",
    )
    """
    Een ingediend bezwaar over de uitvoering van de corporatie van het
    woonruimteverdeelproces.
    """

    klacht = ReclamatiesoortReferentiedata(
        code="KLA",
        naam="Klacht",
    )
    """
    Een klacht over de uitvoering van de corporatie van het woonruimteverdeelproces.
    """
