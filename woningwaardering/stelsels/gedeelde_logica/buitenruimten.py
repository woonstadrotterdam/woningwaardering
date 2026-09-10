from woningwaardering.vera.bvg.generated import EenhedenRuimte

# Beleidsboek §2.8.2: minimumafmeting van 2,00 m × 1,50 m × 1,50 m
# (hoogte, breedte, diepte). VERA documenteert lengte/breedte/hoogte in mm.
MINIMUM_HOOGTE_GEMEENSCHAPPELIJKE_BUITENRUIMTE_MM = 2000
MINIMUM_LENGTE_GEMEENSCHAPPELIJKE_BUITENRUIMTE_MM = 1500
MINIMUM_BREEDTE_GEMEENSCHAPPELIJKE_BUITENRUIMTE_MM = 1500


def voldoet_aan_minimumafmeting_gemeenschappelijke_buitenruimte(
    ruimte: EenhedenRuimte,
) -> bool:
    """Of een gemeenschappelijke buitenruimte voldoet aan de minimumafmeting.

    Beleidsboek §2.8.2: er moet sprake zijn van een minimumafmeting van
    2,00 meter × 1,50 meter × 1,50 meter (hoogte, breedte, diepte).

    Alleen gezette velden worden getoetst (VERA: millimeter). Ontbrekende
    afmetingen leiden niet tot afkeuring: systemen zonder bounding box
    (niet-rechthoekige ruimten) kunnen dan op oppervlakte worden gewaardeerd.
    """
    if (
        ruimte.hoogte is not None
        and ruimte.hoogte < MINIMUM_HOOGTE_GEMEENSCHAPPELIJKE_BUITENRUIMTE_MM
    ):
        return False
    if (
        ruimte.lengte is not None
        and ruimte.lengte < MINIMUM_LENGTE_GEMEENSCHAPPELIJKE_BUITENRUIMTE_MM
    ):
        return False
    if (
        ruimte.breedte is not None
        and ruimte.breedte < MINIMUM_BREEDTE_GEMEENSCHAPPELIJKE_BUITENRUIMTE_MM
    ):
        return False
    return True
