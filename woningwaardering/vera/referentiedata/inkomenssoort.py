from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class InkomenssoortReferentiedata(Referentiedata):
    pass


class Inkomenssoort(Referentiedatasoort):
    bruto_jaarinkomen = InkomenssoortReferentiedata(
        code="BRU",
        naam="Bruto jaarinkomen",
    )
    """
    Het bruto jaarinkomen kan bestaan uit een geregistreerd inkomen, schatting van het
    actuele inkomen of een zelf opgegeven inkomen.
    """

    netto_jaarinkomen = InkomenssoortReferentiedata(
        code="NET",
        naam="Netto jaarinkomen",
    )
    """
    Het netto jaarinkomen zoals verwacht voor het huidige jaar.
    """
