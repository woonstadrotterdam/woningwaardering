from vera.referentiedata.models import Referentiedata


class Zaaktypesoort:
    leefbaarheid = Referentiedata(
        code="LEE",
        naam="Leefbaarheid",
    )
    """
    Op initiatief van de corporatie verbeteren van de buurt
    """

    omgevingsoverlast = Referentiedata(
        code="OMG",
        naam="Omgevingsoverlast",
    )
    """
    Overlast in de omgeving
    """

    klacht_over_organisatie = Referentiedata(
        code="ORG",
        naam="Klacht over organisatie",
    )
    """
    Klachten over de corporatie als organisatie
    """

    sociale_melding = Referentiedata(
        code="SOC",
        naam="Sociale melding",
    )
    """
    Overige sociale gerelateerde meldingen
    """

    woonfraude = Referentiedata(
        code="WOO",
        naam="Woonfraude",
    )
    """
    Fraude door bewoner
    """
