"""Verification tests for GitHub issues #322 and #325 (onzelfstandig)."""

from datetime import date

import pytest

from woningwaardering.stelsels.gedeelde_logica import is_zolder_zonder_vaste_trap
from woningwaardering.stelsels.onzelfstandige_woonruimten import (
    OppervlakteVanOverigeRuimten,
)
from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenEenheid,
    EenhedenRuimte,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
)

PEILDATUM = date(2026, 7, 1)


def _kast(oppervlakte: float) -> EenhedenRuimte:
    return EenhedenRuimte(
        id="kast",
        soort=Ruimtesoort.overige_ruimten,
        detail_soort=Ruimtedetailsoort.kast,
        naam="Kast",
        oppervlakte=oppervlakte,
    )


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_issue_322_zoldercorrectie_telt_kast_op_berging_mee():
    berging = EenhedenRuimte(
        id="berging",
        soort=Ruimtesoort.overige_ruimten,
        detail_soort=Ruimtedetailsoort.berging,
        naam="Berging",
        oppervlakte=2.4,
        inhoud=6,
        verbonden_ruimten=[_kast(0.2)],
    )
    zolder = EenhedenRuimte(
        id="zolder",
        soort=Ruimtesoort.overige_ruimten,
        detail_soort=Ruimtedetailsoort.zolder,
        naam="Zolder",
        oppervlakte=2.4,
        inhoud=6,
        bouwkundige_elementen=[
            BouwkundigElementenBouwkundigElement(
                naam="Vlizotrap", detail_soort=Bouwkundigelementdetailsoort.vlizotrap
            )
        ],
    )
    resultaat = OppervlakteVanOverigeRuimten(peildatum=PEILDATUM).waardeer(
        EenhedenEenheid(id="e322", ruimten=[berging, zolder])
    )
    assert resultaat.punten == pytest.approx(2.25)


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_issue_322_zoldercorrectie_kast_op_zolder_zelf():
    zolder = EenhedenRuimte(
        id="zolder",
        soort=Ruimtesoort.overige_ruimten,
        detail_soort=Ruimtedetailsoort.zolder,
        naam="Zolder",
        oppervlakte=2.4,
        inhoud=6,
        verbonden_ruimten=[_kast(0.2)],
        bouwkundige_elementen=[
            BouwkundigElementenBouwkundigElement(
                naam="Vlizotrap", detail_soort=Bouwkundigelementdetailsoort.vlizotrap
            )
        ],
    )
    resultaat = OppervlakteVanOverigeRuimten(peildatum=PEILDATUM).waardeer(
        EenhedenEenheid(id="e322b", ruimten=[zolder])
    )
    assert resultaat.punten == pytest.approx(0.0)


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_issue_325_zolder_met_trap_en_vlizotrap_geen_correctie():
    zolder = EenhedenRuimte(
        id="zolder",
        soort=Ruimtesoort.overige_ruimten,
        detail_soort=Ruimtedetailsoort.zolder,
        naam="Zolder",
        oppervlakte=10.0,
        inhoud=25.0,
        bouwkundige_elementen=[
            BouwkundigElementenBouwkundigElement(
                naam="Trap", detail_soort=Bouwkundigelementdetailsoort.trap
            ),
            BouwkundigElementenBouwkundigElement(
                naam="Vlizotrap", detail_soort=Bouwkundigelementdetailsoort.vlizotrap
            ),
        ],
    )
    assert is_zolder_zonder_vaste_trap(zolder) is False
    resultaat = OppervlakteVanOverigeRuimten(peildatum=PEILDATUM).waardeer(
        EenhedenEenheid(id="e325", ruimten=[zolder])
    )
    assert resultaat.punten == pytest.approx(7.5)
