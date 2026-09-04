from woningwaardering.stelsels.gedeelde_logica.aanrecht import (
    AANRECHT_MINIMALE_LENGTE_MM,
    heeft_valide_aanrecht,
    is_valide_aanrechtlengte,
)
from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import Bouwkundigelementdetailsoort


def test_is_valide_aanrechtlengte_vanaf_minimale_lengte():
    assert not is_valide_aanrechtlengte(None)
    assert not is_valide_aanrechtlengte(AANRECHT_MINIMALE_LENGTE_MM - 1)
    assert is_valide_aanrechtlengte(AANRECHT_MINIMALE_LENGTE_MM)
    assert is_valide_aanrechtlengte(AANRECHT_MINIMALE_LENGTE_MM + 1)


def test_heeft_valide_aanrecht():
    ruimte_zonder = EenhedenRuimte(
        id="zonder",
        bouwkundige_elementen=[
            BouwkundigElementenBouwkundigElement(
                id="kort",
                detail_soort=Bouwkundigelementdetailsoort.aanrecht,
                lengte=500,
            )
        ],
    )
    ruimte_met = EenhedenRuimte(
        id="met",
        bouwkundige_elementen=[
            BouwkundigElementenBouwkundigElement(
                id="lang",
                detail_soort=Bouwkundigelementdetailsoort.aanrecht,
                lengte=AANRECHT_MINIMALE_LENGTE_MM,
            )
        ],
    )

    assert not heeft_valide_aanrecht(ruimte_zonder)
    assert heeft_valide_aanrecht(ruimte_met)
