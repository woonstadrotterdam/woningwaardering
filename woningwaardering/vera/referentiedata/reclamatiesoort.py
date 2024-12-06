from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class Reclamatiesoort(Referentiedatasoort):
    bezwaar = Referentiedata(
        code="BEZ",
        naam="Bezwaar",
    )
    """
    Een ingediend bezwaar over de uitvoering van de corporatie van het
    woonruimteverdeelproces.
    """

    klacht = Referentiedata(
        code="KLA",
        naam="Klacht",
    )
    """
    Een klacht over de uitvoering van de corporatie van het woonruimteverdeelproces.
    """
