"""Tests voor verbonden kasten in de energieprestatie-oppervlakte."""

from datetime import date

import pytest

from woningwaardering.stelsels.onzelfstandige_woonruimten import Energieprestatie
from woningwaardering.vera.bvg.generated import EenhedenEenheid, EenhedenRuimte
from woningwaardering.vera.referentiedata import Ruimtedetailsoort, Ruimtesoort

PEILDATUM = date(2026, 7, 1)


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_vaste_kast_telt_mee_in_energie_m2_grondslag():
    kast = EenhedenRuimte(
        id="kast",
        soort=Ruimtesoort.overige_ruimten,
        detail_soort=Ruimtedetailsoort.kast,
        naam="Kast",
        oppervlakte=2.0,
    )
    slaapkamer = EenhedenRuimte(
        id="slaapkamer",
        soort=Ruimtesoort.vertrek,
        detail_soort=Ruimtedetailsoort.slaapkamer,
        naam="Slaapkamer",
        oppervlakte=20.0,
        verbonden_ruimten=[kast],
    )
    eenheid = EenhedenEenheid(
        id="energieprestatie_kasten",
        bouwjaar=1970,
        monumenten=[],
        ruimten=[slaapkamer],
    )

    groep = Energieprestatie(peildatum=PEILDATUM).waardeer(eenheid)
    m2 = next(
        w.aantal
        for w in groep.woningwaarderingen or []
        if w.aantal is not None and w.punten is not None
    )
    assert m2 == 22.0
    assert groep.punten < -3.0  # strenger dan 20 m² × -0,15 = -3,0
