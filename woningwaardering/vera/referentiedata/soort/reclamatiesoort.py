from vera.bvg.generated import Referentiedata


class Reclamatiesoort:
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
