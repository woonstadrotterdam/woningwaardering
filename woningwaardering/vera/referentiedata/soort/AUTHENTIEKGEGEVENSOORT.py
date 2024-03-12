
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class AUTHENTIEKGEGEVENSOORT:

    actueel_inkomen = Referentiedata(
        code="AIN",
        naam="Actueel inkomen",
    )
    # actueel_inkomen = ("AIN", "Actueel inkomen")
    """
    Actueel inkomen voor als iemands inkomenssituatie is veranderd.
    """

    digitale_identiteit = Referentiedata(
        code="DID",
        naam="Digitale identiteit",
    )
    # digitale_identiteit = ("DID", "Digitale identiteit")
    """
    Versleuteld BSN nummer.
    """

    geregistreerd_inkomen = Referentiedata(
        code="GIN",
        naam="Geregistreerd inkomen",
    )
    # geregistreerd_inkomen = ("GIN", "Geregistreerd inkomen")
    """
    Geregistreerde inkomen.
    """

    huidhoudsamenstelling = Referentiedata(
        code="HUI",
        naam="Huidhoudsamenstelling",
    )
    # huidhoudsamenstelling = ("HUI", "Huidhoudsamenstelling")
    """
    Huidhoudsamenstelling uit BRP.
    """

    naam_adres_woonplaats = Referentiedata(
        code="NAW",
        naam="Naam Adres Woonplaats",
    )
    # naam_adres_woonplaats = ("NAW", "Naam Adres Woonplaats")
    """
    NAW gegevens van een natuurlijke persoon.
    """

    opleiding = Referentiedata(
        code="OPL",
        naam="Opleiding",
    )
    # opleiding = ("OPL", "Opleiding")
    """
    Opleiding en studennummer.
    """

    werkgevers = Referentiedata(
        code="WER",
        naam="Werkgevers",
    )
    # werkgevers = ("WER", "Werkgevers")
    """
    Actuele werkgevers.
    """

    woongeschiedenis = Referentiedata(
        code="WOO",
        naam="Woongeschiedenis",
    )
    # woongeschiedenis = ("WOO", "Woongeschiedenis")
    """
    De woongeschiedenis voor het bepalen in welke gemeenten men wanneer heeft gewoond.
    """
