import pytest

from woningwaardering.stelsels.gedeelde_logica.oppervlakte_van_overige_ruimten import (
    is_zolder_zonder_vaste_trap,
)
from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Bouwkundigelementsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
)

TRAP = BouwkundigElementenBouwkundigElement(
    soort=Bouwkundigelementsoort.voorziening,
    detail_soort=Bouwkundigelementdetailsoort.trap,
)
VLIZOTRAP = BouwkundigElementenBouwkundigElement(
    soort=Bouwkundigelementsoort.voorziening,
    detail_soort=Bouwkundigelementdetailsoort.vlizotrap,
)


def maak_ruimte(detail_soort, soort, oppervlakte, bouwkundige_elementen):
    return EenhedenRuimte(
        id="Space_1",
        naam="Zolder",
        soort=soort,
        detail_soort=detail_soort,
        oppervlakte=oppervlakte,
        bouwkundige_elementen=bouwkundige_elementen,
    )


@pytest.mark.parametrize(
    "detail_soort", [Ruimtedetailsoort.zolder, Ruimtedetailsoort.zoldervertrek]
)
@pytest.mark.parametrize("soort", [Ruimtesoort.overige_ruimten, Ruimtesoort.vertrek])
def test_is_zolder_zonder_vaste_trap_bij_vlizotrap(detail_soort, soort):
    """2.2.2.3 geldt voor elke zolderruimte, ongeacht de aangeleverde detailsoort.

    `zoldervertrek` is net als `zolder` een zolderruimte en krijgt daarom dezelfde
    puntenaftrek wanneer er geen vaste trap is.
    """
    ruimte = maak_ruimte(detail_soort, soort, 10, [VLIZOTRAP])

    assert is_zolder_zonder_vaste_trap(ruimte)


@pytest.mark.parametrize(
    "detail_soort", [Ruimtedetailsoort.zolder, Ruimtedetailsoort.zoldervertrek]
)
def test_is_zolder_zonder_vaste_trap_niet_bij_vaste_trap(detail_soort):
    ruimte = maak_ruimte(detail_soort, Ruimtesoort.overige_ruimten, 10, [TRAP])

    assert not is_zolder_zonder_vaste_trap(ruimte)


@pytest.mark.parametrize(
    "detail_soort", [Ruimtedetailsoort.zolder, Ruimtedetailsoort.zoldervertrek]
)
def test_is_zolder_zonder_vaste_trap_niet_bij_trap_en_vlizotrap(detail_soort):
    """Een expliciete vaste trap wint van een vlizotrap: geen aftrek."""
    ruimte = maak_ruimte(
        detail_soort, Ruimtesoort.overige_ruimten, 10, [TRAP, VLIZOTRAP]
    )

    assert not is_zolder_zonder_vaste_trap(ruimte)


@pytest.mark.parametrize(
    "detail_soort", [Ruimtedetailsoort.zolder, Ruimtedetailsoort.zoldervertrek]
)
def test_is_zolder_zonder_vaste_trap_niet_zonder_trap_elementen(detail_soort):
    """Zonder trap-elementen stelt de detailsoort de vaste trap: geen aftrek."""
    ruimte = maak_ruimte(detail_soort, Ruimtesoort.overige_ruimten, 10, [])

    assert not is_zolder_zonder_vaste_trap(ruimte)


@pytest.mark.parametrize(
    "detail_soort", [Ruimtedetailsoort.zolder, Ruimtedetailsoort.zoldervertrek]
)
def test_is_zolder_zonder_vaste_trap_niet_bij_ongewaardeerde_zolder(detail_soort):
    """Een zolder die zelf niet gewaardeerd wordt, krijgt ook geen aftrek."""
    ruimte = maak_ruimte(detail_soort, Ruimtesoort.overige_ruimten, 1.99, [VLIZOTRAP])

    assert not is_zolder_zonder_vaste_trap(ruimte)


def test_is_zolder_zonder_vaste_trap_niet_bij_andere_detailsoort():
    ruimte = maak_ruimte(
        Ruimtedetailsoort.berging, Ruimtesoort.overige_ruimten, 10, [VLIZOTRAP]
    )

    assert not is_zolder_zonder_vaste_trap(ruimte)
