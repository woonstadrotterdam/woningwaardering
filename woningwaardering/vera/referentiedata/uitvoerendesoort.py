from woningwaardering.vera.bvg.generated import Referentiedata


class Uitvoerendesoort:
    leverancier = Referentiedata(
        code="LEV",
        naam="Leverancier",
    )
    """
    Uitvoering vindt plaats door een externe partij
    """

    vakgroep = Referentiedata(
        code="VAK",
        naam="Vakgroep",
    )
    """
    Uitvoering vindt plaats door een interne vakgroep / eigen dienst
    """
