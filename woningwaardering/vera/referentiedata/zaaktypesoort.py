from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class ZaaktypesoortReferentiedata(Referentiedata):
    pass


class Zaaktypesoort(Referentiedatasoort):
    financiele_problematiek = ZaaktypesoortReferentiedata(
        code="FIN",
        naam="Financiële problematiek",
    )
    """
    Zaken met betrekking tot financiële achterstanden, betalingsproblemen of
    gerelateerde problematiek
    """

    leefbaarheid = ZaaktypesoortReferentiedata(
        code="LEE",
        naam="Leefbaarheid",
    )
    """
    Op initiatief van de corporatie verbeteren van de buurt
    """

    omgevingsoverlast = ZaaktypesoortReferentiedata(
        code="OMG",
        naam="Omgevingsoverlast",
    )
    """
    Overlast in de omgeving
    """

    klacht_over_organisatie = ZaaktypesoortReferentiedata(
        code="ORG",
        naam="Klacht over organisatie",
    )
    """
    Klachten over de corporatie als organisatie
    """

    sociale_melding = ZaaktypesoortReferentiedata(
        code="SOC",
        naam="Sociale melding",
    )
    """
    Overige sociale gerelateerde meldingen
    """

    woonfraude = ZaaktypesoortReferentiedata(
        code="WOO",
        naam="Woonfraude",
    )
    """
    Fraude door bewoner
    """
