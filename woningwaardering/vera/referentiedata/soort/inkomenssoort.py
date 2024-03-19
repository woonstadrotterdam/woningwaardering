from vera.bvg.generated import Referentiedata


class Inkomenssoort:
    bruto_jaarinkomen = Referentiedata(
        code="BRU",
        naam="Bruto jaarinkomen",
    )
    """
    Het bruto jaarinkomen kan bestaan uit een geregistreerd inkomen, schatting van het
    actuele inkomen of een zelf opgegeven inkomen.
    """

    netto_jaarinkomen = Referentiedata(
        code="NET",
        naam="Netto jaarinkomen",
    )
    """
    Het netto jaarinkomen zoals verwacht voor het huidige jaar.
    """
