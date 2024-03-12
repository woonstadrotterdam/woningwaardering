
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class INKOMENSSOORT:

    bruto_jaarinkomen = Referentiedata(
        code="BRU",
        naam="Bruto jaarinkomen",
    )
    # bruto_jaarinkomen = ("BRU", "Bruto jaarinkomen")
    """
    Het bruto jaarinkomen kan bestaan uit een geregistreerd inkomen, schatting van het
    actuele inkomen of een zelf opgegeven inkomen.
    """

    netto_jaarinkomen = Referentiedata(
        code="NET",
        naam="Netto jaarinkomen",
    )
    # netto_jaarinkomen = ("NET", "Netto jaarinkomen")
    """
    Het netto jaarinkomen zoals verwacht voor het huidige jaar.
    """
