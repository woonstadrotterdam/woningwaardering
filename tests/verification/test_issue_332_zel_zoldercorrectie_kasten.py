"""Verification tests for GitHub issue #332."""

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


def _zolder_met_vlizotrap(
    *, oppervlakte: float, kast_oppervlakte: float | None = None
) -> EenhedenRuimte:
    verbonden: list[EenhedenRuimte] = []
    if kast_oppervlakte is not None:
        verbonden.append(
            EenhedenRuimte(
                id="kast",
                soort=Ruimtesoort.overige_ruimten,
                detail_soort=Ruimtedetailsoort.kast,
                naam="Kast",
                oppervlakte=kast_oppervlakte,
            )
        )
    return EenhedenRuimte(
        id="zolder",
        soort=Ruimtesoort.overige_ruimten,
        detail_soort=Ruimtedetailsoort.zolder,
        naam="Zolder",
        oppervlakte=oppervlakte,
        bouwkundige_elementen=[
            BouwkundigElementenBouwkundigElement(
                naam="Vlizotrap",
                detail_soort=Bouwkundigelementdetailsoort.vlizotrap,
            )
        ],
        verbonden_ruimten=verbonden or None,
    )


def _berging_met_kast(*, oppervlakte: float, kast_oppervlakte: float) -> EenhedenRuimte:
    return EenhedenRuimte(
        id="berging",
        soort=Ruimtesoort.overige_ruimten,
        detail_soort=Ruimtedetailsoort.berging,
        naam="Berging",
        oppervlakte=oppervlakte,
        verbonden_ruimten=[
            EenhedenRuimte(
                id="kast",
                soort=Ruimtesoort.overige_ruimten,
                detail_soort=Ruimtedetailsoort.kast,
                naam="Kast",
                oppervlakte=kast_oppervlakte,
            )
        ],
    )


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_issue_332_kast_op_berging_beinvloedt_zoldercorrectie():
    eenheid = EenhedenEenheid(
        id="issue-332-1",
        ruimten=[
            _berging_met_kast(oppervlakte=2.4, kast_oppervlakte=0.2),
            _zolder_met_vlizotrap(oppervlakte=2.4),
        ],
    )
    groep = OppervlakteVanOverigeRuimten(peildatum=PEILDATUM).waardeer(eenheid)
    assert groep.punten == 2.25


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_issue_332_kast_op_zolder_volledige_correctie():
    eenheid = EenhedenEenheid(
        id="issue-332-2",
        ruimten=[_zolder_met_vlizotrap(oppervlakte=2.4, kast_oppervlakte=0.2)],
    )
    groep = OppervlakteVanOverigeRuimten(peildatum=PEILDATUM).waardeer(eenheid)
    assert groep.punten == 0.0
