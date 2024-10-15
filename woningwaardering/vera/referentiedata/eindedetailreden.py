from enum import Enum

from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedata.eindereden import Eindereden


class Eindedetailreden(Enum):
    faillissement = Referentiedata(
        code="FAI",
        naam="Faillissement",
        parent=Eindereden.ontbinding.value,
    )
    """
    Een overeenkomst is beëindigd wegens faillissement
    """

    noorderzon = Referentiedata(
        code="NOO",
        naam="Noorderzon",
        parent=Eindereden.ontbinding.value,
    )
    """
    Een overeenkomst is beëindigd omdat de huurder(s) met de noorderzon is (zijn)
    vertrokken
    """

    ontruiming = Referentiedata(
        code="ONT",
        naam="Ontruiming",
        parent=Eindereden.ontbinding.value,
    )
    """
    Een overeenkomst is beëindigd omdat de woning is ontruimd
    """

    overlijden = Referentiedata(
        code="OVE",
        naam="Overlijden",
        parent=Eindereden.ontbinding.value,
    )
    """
    Een overeenkomst is beëindigd wegens overlijden
    """

    regulier = Referentiedata(
        code="REG",
        naam="Regulier",
        parent=Eindereden.opzegging.value,
    )
    """
    Er is geen bijzondere aanleiding voor het beëindigen van een overeenkomst, of de
    reden is niet bekend.
    """

    terugkoop = Referentiedata(
        code="TER",
        naam="Terugkoop",
        parent=Eindereden.opzegging.value,
    )
    """
    Een overeenkomst is beëindigd wegens terugkoop
    """

    verkoop = Referentiedata(
        code="VER",
        naam="Verkoop",
        parent=Eindereden.opzegging.value,
    )
    """
    Een overeenkomst is beëindigd wegens verkoop
    """

    wijziging_tenaamstelling = Referentiedata(
        code="WIJ",
        naam="Wijziging tenaamstelling",
        parent=Eindereden.opzegging.value,
    )
    """
    Een overeenkomst is beëindigd omdat de tenaamstelling is gewijzigd (en is vervangen
    door een nieuwe overeenkomst)
    """

    woningruil = Referentiedata(
        code="WON",
        naam="Woningruil",
        parent=Eindereden.opzegging.value,
    )
    """
    Een overeenkomst is beëindigd wegens woningruil
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
