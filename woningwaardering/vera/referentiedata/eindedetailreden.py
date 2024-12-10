from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.eindereden import (
    Eindereden,
)
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class EindedetailredenReferentiedata(Referentiedata):
    pass


class Eindedetailreden(Referentiedatasoort):
    faillissement = EindedetailredenReferentiedata(
        code="FAI",
        naam="Faillissement",
        parent=Eindereden.ontbinding,
    )
    """
    Een overeenkomst is beëindigd wegens faillissement
    """

    noorderzon = EindedetailredenReferentiedata(
        code="NOO",
        naam="Noorderzon",
        parent=Eindereden.ontbinding,
    )
    """
    Een overeenkomst is beëindigd omdat de huurder(s) met de noorderzon is (zijn)
    vertrokken
    """

    ontruiming = EindedetailredenReferentiedata(
        code="ONT",
        naam="Ontruiming",
        parent=Eindereden.ontbinding,
    )
    """
    Een overeenkomst is beëindigd omdat de woning is ontruimd
    """

    overlijden = EindedetailredenReferentiedata(
        code="OVE",
        naam="Overlijden",
        parent=Eindereden.ontbinding,
    )
    """
    Een overeenkomst is beëindigd wegens overlijden
    """

    regulier = EindedetailredenReferentiedata(
        code="REG",
        naam="Regulier",
        parent=Eindereden.opzegging,
    )
    """
    Er is geen bijzondere aanleiding voor het beëindigen van een overeenkomst, of de
    reden is niet bekend.
    """

    terugkoop = EindedetailredenReferentiedata(
        code="TER",
        naam="Terugkoop",
        parent=Eindereden.opzegging,
    )
    """
    Een overeenkomst is beëindigd wegens terugkoop
    """

    verkoop = EindedetailredenReferentiedata(
        code="VER",
        naam="Verkoop",
        parent=Eindereden.opzegging,
    )
    """
    Een overeenkomst is beëindigd wegens verkoop
    """

    wijziging_tenaamstelling = EindedetailredenReferentiedata(
        code="WIJ",
        naam="Wijziging tenaamstelling",
        parent=Eindereden.opzegging,
    )
    """
    Een overeenkomst is beëindigd omdat de tenaamstelling is gewijzigd (en is vervangen
    door een nieuwe overeenkomst)
    """

    woningruil = EindedetailredenReferentiedata(
        code="WON",
        naam="Woningruil",
        parent=Eindereden.opzegging,
    )
    """
    Een overeenkomst is beëindigd wegens woningruil
    """
