from vera.referentiedata.models import Referentiedata


class Authentiekgegevensoort:
    actueel_inkomen = Referentiedata(
        code="AIN",
        naam="Actueel inkomen",
    )
    """
    Actueel inkomen voor als iemands inkomenssituatie is veranderd.
    """

    digitale_identiteit = Referentiedata(
        code="DID",
        naam="Digitale identiteit",
    )
    """
    Versleuteld BSN nummer.
    """

    geregistreerd_inkomen = Referentiedata(
        code="GIN",
        naam="Geregistreerd inkomen",
    )
    """
    Geregistreerde inkomen.
    """

    huidhoudsamenstelling = Referentiedata(
        code="HUI",
        naam="Huidhoudsamenstelling",
    )
    """
    Huidhoudsamenstelling uit BRP.
    """

    naam_adres_woonplaats = Referentiedata(
        code="NAW",
        naam="Naam Adres Woonplaats",
    )
    """
    NAW gegevens van een natuurlijke persoon.
    """

    opleiding = Referentiedata(
        code="OPL",
        naam="Opleiding",
    )
    """
    Opleiding en studennummer.
    """

    werkgevers = Referentiedata(
        code="WER",
        naam="Werkgevers",
    )
    """
    Actuele werkgevers.
    """

    woongeschiedenis = Referentiedata(
        code="WOO",
        naam="Woongeschiedenis",
    )
    """
    De woongeschiedenis voor het bepalen in welke gemeenten men wanneer heeft gewoond.
    """
