from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class UitvoerendesoortReferentiedata(Referentiedata):
    pass


class Uitvoerendesoort(Referentiedatasoort):
    leverancier = UitvoerendesoortReferentiedata(
        code="LEV",
        naam="Leverancier",
    )
    """
    Uitvoering vindt plaats door een externe partij
    """

    vakgroep = UitvoerendesoortReferentiedata(
        code="VAK",
        naam="Vakgroep",
    )
    """
    Uitvoering vindt plaats door een interne vakgroep / eigen dienst
    """
