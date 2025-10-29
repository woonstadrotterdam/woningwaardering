from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class AuthentiekgegevensoortReferentiedata(Referentiedata):
    pass


class Authentiekgegevensoort(Referentiedatasoort):
    actueel_inkomen = AuthentiekgegevensoortReferentiedata(
        code="AIN",
        naam="Actueel inkomen",
    )
    """
    Actueel inkomen voor als iemands inkomenssituatie is veranderd.
    """

    digitale_identiteit = AuthentiekgegevensoortReferentiedata(
        code="DID",
        naam="Digitale identiteit",
    )
    """
    Versleuteld BSN nummer.
    """

    geregistreerd_inkomen = AuthentiekgegevensoortReferentiedata(
        code="GIN",
        naam="Geregistreerd inkomen",
    )
    """
    Geregistreerde inkomen.
    """

    huidhoudsamenstelling = AuthentiekgegevensoortReferentiedata(
        code="HUI",
        naam="Huidhoudsamenstelling",
    )
    """
    Huidhoudsamenstelling uit BRP.
    """

    naam_adres_woonplaats = AuthentiekgegevensoortReferentiedata(
        code="NAW",
        naam="Naam Adres Woonplaats",
    )
    """
    NAW gegevens van een natuurlijke persoon.
    """

    opleiding = AuthentiekgegevensoortReferentiedata(
        code="OPL",
        naam="Opleiding",
    )
    """
    Opleiding en studennummer.
    """

    werkgevers = AuthentiekgegevensoortReferentiedata(
        code="WER",
        naam="Werkgevers",
    )
    """
    Actuele werkgevers.
    """

    woongeschiedenis = AuthentiekgegevensoortReferentiedata(
        code="WOO",
        naam="Woongeschiedenis",
    )
    """
    De woongeschiedenis voor het bepalen in welke gemeenten men wanneer heeft gewoond.
    """
