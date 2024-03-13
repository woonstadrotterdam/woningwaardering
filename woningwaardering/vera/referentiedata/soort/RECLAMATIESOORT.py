from woningwaardering.vera.bvg.models import Referentiedata


class RECLAMATIESOORT:
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
