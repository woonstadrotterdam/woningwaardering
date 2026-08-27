from woningwaardering.vera.bvg.generated import EenhedenRuimte
from woningwaardering.vera.referentiedata import Bouwkundigelementdetailsoort
from woningwaardering.vera.utils import get_bouwkundige_elementen

# Wettekst Bijlage I A rubriek 5: aanrechtblad met aaneengesloten lengte van minimaal 1 m
AANRECHT_MINIMALE_LENGTE_MM = 1000


def is_valide_aanrechtlengte(lengte: float | None) -> bool:
    """Of een aanrechtlengte voldoet aan de minimale basisvoorziening (vanaf 1 m)."""
    return lengte is not None and lengte >= AANRECHT_MINIMALE_LENGTE_MM


def heeft_valide_aanrecht(ruimte: EenhedenRuimte) -> bool:
    """Of de ruimte minstens één aanrecht met lengte vanaf 1 meter heeft."""
    return any(
        is_valide_aanrechtlengte(element.lengte)
        for element in get_bouwkundige_elementen(
            ruimte, Bouwkundigelementdetailsoort.aanrecht
        )
    )
