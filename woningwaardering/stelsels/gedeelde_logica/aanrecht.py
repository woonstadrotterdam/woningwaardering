from woningwaardering.stelsels.utils import (
    BUITENRUIMTE_DETAIL_SOORTEN,
    PARKEERPLEK_DETAIL_SOORTEN,
)
from woningwaardering.vera.bvg.generated import EenhedenRuimte
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtesoort,
)
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


def telt_aanrecht_mee(ruimte: EenhedenRuimte) -> bool:
    """Of een aanrecht in deze ruimte meetelt voor de keuken- en sanitairwaardering.

    Wettekst Bijlage I A rubriek 5 stelt eisen aan de keuken zelf — aan- en afvoer
    van water, een kookaansluitpunt, een aanrechtblad van minimaal 1 m, twee
    inbouwkasten en een waterdichte afwerking — maar stelt geen enkele eis aan de
    ruimte waarin die keuken ligt. Een aanrecht telt daarom in beginsel overal mee,
    ook in bijvoorbeeld een bijkeuken, berging of gang.

    Uitgesloten zijn alleen buitenruimten en parkeervoorzieningen: daar is een
    aanrecht geen voorziening van de woonruimte. Een `garage` valt hier bewust
    buiten en telt dus wél mee, omdat die als privé overige ruimte wordt
    gewaardeerd.

    Dezelfde grens geldt voor rubriek 6.1, waar een spoelbak in een aanrecht korter
    dan 1 m als wastafel meetelt: waar een aanrecht vanaf 1 m een keuken oplevert,
    levert een korter aanrecht een wastafel op.

    Args:
        ruimte (EenhedenRuimte): De ruimte om te controleren.

    Returns:
        bool: True als een aanrecht in deze ruimte meetelt, anders False.
    """
    # De detailsoort doet hier het werk, niet de soort: een gemeenschappelijke
    # keuken, een gemeenschappelijk balkon en een gemeenschappelijke parkeerplek
    # komen alle drie binnen als `Ruimtesoort.gemeenschappelijke_ruimten_en_voorzieningen`.
    # Omdat we die soort moeten toelaten voor gemeenschappelijke keukens, kan
    # alleen de detailsoort ze uit elkaar houden.
    if ruimte.detail_soort in BUITENRUIMTE_DETAIL_SOORTEN:
        return False
    if ruimte.detail_soort in PARKEERPLEK_DETAIL_SOORTEN:
        return False
    # backstop voor buitenruimte-detailsoorten buiten de lijst hierboven
    return ruimte.soort != Ruimtesoort.buitenruimte
