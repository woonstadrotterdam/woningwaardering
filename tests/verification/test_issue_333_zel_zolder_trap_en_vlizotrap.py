"""Verification tests for GitHub issue #333."""

from datetime import date

import pytest

from woningwaardering.stelsels.zelfstandige_woonruimten import (
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
PUNTEN_ZONDER_CORRECTIE = 7.5


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_issue_333_trap_en_vlizotrap_geen_zoldercorrectie():
    zolder = EenhedenRuimte(
        id="zolder",
        soort=Ruimtesoort.overige_ruimten,
        detail_soort=Ruimtedetailsoort.zolder,
        naam="Zolder",
        oppervlakte=10.0,
        bouwkundige_elementen=[
            BouwkundigElementenBouwkundigElement(
                naam="Trap", detail_soort=Bouwkundigelementdetailsoort.trap
            ),
            BouwkundigElementenBouwkundigElement(
                naam="Vlizotrap", detail_soort=Bouwkundigelementdetailsoort.vlizotrap
            ),
        ],
    )
    groep = OppervlakteVanOverigeRuimten(peildatum=PEILDATUM).waardeer(
        EenhedenEenheid(id="issue-333", ruimten=[zolder])
    )
    assert groep.punten == PUNTEN_ZONDER_CORRECTIE


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_issue_333_alleen_vlizotrap_behoudt_correctie():
    zolder = EenhedenRuimte(
        id="zolder",
        soort=Ruimtesoort.overige_ruimten,
        detail_soort=Ruimtedetailsoort.zolder,
        naam="Zolder",
        oppervlakte=10.0,
        bouwkundige_elementen=[
            BouwkundigElementenBouwkundigElement(
                naam="Vlizotrap", detail_soort=Bouwkundigelementdetailsoort.vlizotrap
            ),
        ],
    )
    groep = OppervlakteVanOverigeRuimten(peildatum=PEILDATUM).waardeer(
        EenhedenEenheid(id="issue-333-ref", ruimten=[zolder])
    )
    assert groep.punten == PUNTEN_ZONDER_CORRECTIE - 5.0
