
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class RECLAMATIESOORT:

    bezwaar = Referentiedata(
        code="BEZ",
        naam="Bezwaar",
    )
    # bezwaar = ("BEZ", "Bezwaar")
    """
    Een ingediend bezwaar over de uitvoering van de corporatie van het
    woonruimteverdeelproces.
    """

    klacht = Referentiedata(
        code="KLA",
        naam="Klacht",
    )
    # klacht = ("KLA", "Klacht")
    """
    Een klacht over de uitvoering van de corporatie van het woonruimteverdeelproces.
    """
