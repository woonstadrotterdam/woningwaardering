from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Authentiekgegevensoort(Enum):
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

    @property
    def code(self) -> str:
        if self.value.code is None:
            raise TypeError("de code van een Referentiedata object mag niet None zijn")
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam

    @property
    def parent(self) -> Referentiedata | None:
        return self.value.parent
