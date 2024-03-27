from enum import Enum
from woningwaardering.vera.bvg.generated import Referentiedata


class Eindedetailreden(Enum):
    faillissement = Referentiedata(
        code="FAI",
        naam="Faillissement",
    )
    """
    Een overeenkomst is beëindigd wegens faillissement
    """

    noorderzon = Referentiedata(
        code="NOO",
        naam="Noorderzon",
    )
    """
    Een overeenkomst is beëindigd omdat de huurder(s) met de noorderzon is (zijn)
    vertrokken
    """

    ontruiming = Referentiedata(
        code="ONT",
        naam="Ontruiming",
    )
    """
    Een overeenkomst is beëindigd omdat de woning is ontruimd
    """

    overlijden = Referentiedata(
        code="OVE",
        naam="Overlijden",
    )
    """
    Een overeenkomst is beëindigd wegens overlijden
    """

    regulier = Referentiedata(
        code="REG",
        naam="Regulier",
    )
    """
    Er is geen bijzondere aanleiding voor het beëindigen van een overeenkomst, of de
    reden is niet bekend.
    """

    terugkoop = Referentiedata(
        code="TER",
        naam="Terugkoop",
    )
    """
    Een overeenkomst is beëindigd wegens terugkoop
    """

    verkoop = Referentiedata(
        code="VER",
        naam="Verkoop",
    )
    """
    Een overeenkomst is beëindigd wegens verkoop
    """

    wijziging_tenaamstelling = Referentiedata(
        code="WIJ",
        naam="Wijziging tenaamstelling",
    )
    """
    Een overeenkomst is beëindigd omdat de tenaamstelling is gewijzigd (en is vervangen
    door een nieuwe overeenkomst)
    """

    woningruil = Referentiedata(
        code="WON",
        naam="Woningruil",
    )
    """
    Een overeenkomst is beëindigd wegens woningruil
    """

    @property
    def code(self) -> str | None:
        return self.value.code

    @property
    def naam(self) -> str | None:
        return self.value.naam
