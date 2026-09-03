from decimal import Decimal

import pytest

from woningwaardering.stelsels.gedeelde_logica.oppervlakte_van_overige_ruimten import (
    bereken_zolder_correctie,
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
    """Een expliciete `trap` wint van een `vlizotrap`: `is_zolder_zonder_vaste_trap` is False."""
    ruimte = maak_ruimte(
        detail_soort, Ruimtesoort.overige_ruimten, 10, [TRAP, VLIZOTRAP]
    )

    assert not is_zolder_zonder_vaste_trap(ruimte)


@pytest.mark.parametrize(
    "detail_soort", [Ruimtedetailsoort.zolder, Ruimtedetailsoort.zoldervertrek]
)
def test_is_zolder_zonder_vaste_trap_niet_zonder_trap_elementen(detail_soort):
    """Zonder trap-elementen stelt de detailsoort de vaste trap: `is_zolder_zonder_vaste_trap` is False."""
    ruimte = maak_ruimte(detail_soort, Ruimtesoort.overige_ruimten, 10, [])

    assert not is_zolder_zonder_vaste_trap(ruimte)


@pytest.mark.parametrize(
    "detail_soort", [Ruimtedetailsoort.zolder, Ruimtedetailsoort.zoldervertrek]
)
def test_is_zolder_zonder_vaste_trap_niet_bij_ongewaardeerde_zolder(detail_soort):
    """Onder 2 m² classificeert de ruimte niet als overige ruimte: `is_zolder_zonder_vaste_trap` is False."""
    ruimte = maak_ruimte(detail_soort, Ruimtesoort.overige_ruimten, 1.99, [VLIZOTRAP])

    assert not is_zolder_zonder_vaste_trap(ruimte)


def test_is_zolder_zonder_vaste_trap_niet_bij_andere_detailsoort():
    ruimte = maak_ruimte(
        Ruimtedetailsoort.berging, Ruimtesoort.overige_ruimten, 10, [VLIZOTRAP]
    )

    assert not is_zolder_zonder_vaste_trap(ruimte)


def test_bereken_zolder_correctie_prive_volledige_cap() -> None:
    assert bereken_zolder_correctie(Decimal("10"), Decimal("10")) == Decimal("-5")


def test_bereken_zolder_correctie_gedeelde_grote_zolder() -> None:
    """Privé 10,40 + zolder 40,40 / 4 → toe te rekenen totaal 20,50 waarvan 10,10 voor de zolder → −1,25."""
    assert bereken_zolder_correctie(
        Decimal("20.50"),
        Decimal("10.10"),
        max_aftrek=Decimal("5") / Decimal("4"),
    ) == Decimal("-1.25")


def test_bereken_zolder_correctie_gedeelde_kleine_zolder() -> None:
    """Privé 10,40 + zolder 4 / 4 → toe te rekenen totaal 11,40 waarvan 1,00 voor de zolder → −0,75."""
    assert bereken_zolder_correctie(
        Decimal("11.40"),
        Decimal("1.00"),
        max_aftrek=Decimal("5") / Decimal("4"),
    ) == Decimal("-0.75")
