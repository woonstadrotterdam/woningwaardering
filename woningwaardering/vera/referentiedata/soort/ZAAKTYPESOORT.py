
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class ZAAKTYPESOORT:

    leefbaarheid = Referentiedata(
        code="LEE",
        naam="Leefbaarheid",
    )
    # leefbaarheid = ("LEE", "Leefbaarheid")
    """
    Op initiatief van de corporatie verbeteren van de buurt
    """

    omgevingsoverlast = Referentiedata(
        code="OMG",
        naam="Omgevingsoverlast",
    )
    # omgevingsoverlast = ("OMG", "Omgevingsoverlast")
    """
    Overlast in de omgeving
    """

    klacht_over_organisatie = Referentiedata(
        code="ORG",
        naam="Klacht over organisatie",
    )
    # klacht_over_organisatie = ("ORG", "Klacht over organisatie")
    """
    Klachten over de corporatie als organisatie
    """

    sociale_melding = Referentiedata(
        code="SOC",
        naam="Sociale melding",
    )
    # sociale_melding = ("SOC", "Sociale melding")
    """
    Overige sociale gerelateerde meldingen
    """

    woonfraude = Referentiedata(
        code="WOO",
        naam="Woonfraude",
    )
    # woonfraude = ("WOO", "Woonfraude")
    """
    Fraude door bewoner
    """
