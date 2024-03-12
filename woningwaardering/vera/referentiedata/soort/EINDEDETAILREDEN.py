
from enum import Enum
from woningwaardering.vera.bvg.models import Referentiedata


class EINDEDETAILREDEN:

    faillissement = Referentiedata(
        code="FAI",
        naam="Faillissement",
    )
    # faillissement = ("FAI", "Faillissement")
    """
    Een overeenkomst is beëindigd wegens faillissement
    """

    noorderzon = Referentiedata(
        code="NOO",
        naam="Noorderzon",
    )
    # noorderzon = ("NOO", "Noorderzon")
    """
    Een overeenkomst is beëindigd omdat de huurder(s) met de noorderzon is (zijn)
    vertrokken
    """

    ontruiming = Referentiedata(
        code="ONT",
        naam="Ontruiming",
    )
    # ontruiming = ("ONT", "Ontruiming")
    """
    Een overeenkomst is beëindigd omdat de woning is ontruimd
    """

    overlijden = Referentiedata(
        code="OVE",
        naam="Overlijden",
    )
    # overlijden = ("OVE", "Overlijden")
    """
    Een overeenkomst is beëindigd wegens overlijden
    """

    regulier = Referentiedata(
        code="REG",
        naam="Regulier",
    )
    # regulier = ("REG", "Regulier")
    """
    Er is geen bijzondere aanleiding voor het beëindigen van een overeenkomst, of de
    reden is niet bekend.
    """

    terugkoop = Referentiedata(
        code="TER",
        naam="Terugkoop",
    )
    # terugkoop = ("TER", "Terugkoop")
    """
    Een overeenkomst is beëindigd wegens terugkoop
    """

    verkoop = Referentiedata(
        code="VER",
        naam="Verkoop",
    )
    # verkoop = ("VER", "Verkoop")
    """
    Een overeenkomst is beëindigd wegens verkoop
    """

    wijziging_tenaamstelling = Referentiedata(
        code="WIJ",
        naam="Wijziging tenaamstelling",
    )
    # wijziging_tenaamstelling = ("WIJ", "Wijziging tenaamstelling")
    """
    Een overeenkomst is beëindigd omdat de tenaamstelling is gewijzigd (en is vervangen
    door een nieuwe overeenkomst)
    """

    woningruil = Referentiedata(
        code="WON",
        naam="Woningruil",
    )
    # woningruil = ("WON", "Woningruil")
    """
    Een overeenkomst is beëindigd wegens woningruil
    """
