"""Tests voor verbonden kasten in gemeenschappelijke bergingen."""

from datetime import date

import pytest

from woningwaardering.stelsels.zelfstandige_woonruimten import (
    GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid, EenhedenRuimte
from woningwaardering.vera.referentiedata import Ruimtedetailsoort, Ruimtesoort

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
def test_gemeenschappelijke_berging_telt_kast_mee():
    berging = EenhedenRuimte(
        id="berg",
        soort=Ruimtesoort.overige_ruimten,
        detail_soort=Ruimtedetailsoort.berging,
        naam="Berging",
        oppervlakte=8.0,
        gedeeld_met_aantal_adressen=2,
        verbonden_ruimten=[_kast(2.0)],
    )
    resultaat = GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen(
        peildatum=PEILDATUM
    ).waardeer(EenhedenEenheid(id="e324", ruimten=[berging]))
    assert resultaat.punten == pytest.approx(3.75)


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_gemeenschappelijke_berging_drempel_met_kast():
    berging = EenhedenRuimte(
        id="berg",
        soort=Ruimtesoort.overige_ruimten,
        detail_soort=Ruimtedetailsoort.berging,
        naam="Berging",
        oppervlakte=3.0,
        gedeeld_met_aantal_adressen=2,
        verbonden_ruimten=[_kast(2.0)],
    )
    resultaat = GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen(
        peildatum=PEILDATUM
    ).waardeer(EenhedenEenheid(id="e324b", ruimten=[berging]))
    assert resultaat.punten > 0
