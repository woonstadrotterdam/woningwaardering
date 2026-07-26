"""Verificatietests voor GitHub issue #323."""

from datetime import date

import pytest

from woningwaardering.stelsels.onzelfstandige_woonruimten import Buitenruimten
from woningwaardering.stelsels.onzelfstandige_woonruimten.gemeenschappelijke_parkeerruimten import (
    GemeenschappelijkeParkeerruimten,
)
from woningwaardering.vera.bvg.generated import EenhedenEenheid, EenhedenRuimte
from woningwaardering.vera.referentiedata import Ruimtedetailsoort, Ruimtesoort

PEILDATUM = date(2026, 7, 1)


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_issue_323_prive_carport_niet_in_buitenruimten_en_wel_in_gpa():
    """§2.8.3 / §2.10.2 [ONZ]: carport alleen in rubriek 10, niet ook rubriek 8."""
    carport = EenhedenRuimte(
        id="carport",
        soort=Ruimtesoort.buitenruimte,
        detail_soort=Ruimtedetailsoort.carport,
        naam="Carport",
        oppervlakte=12.0,
        lengte=4.0,
        breedte=3.0,
        gedeeld_met_aantal_adressen=1,
        gedeeld_met_aantal_onzelfstandige_woonruimten=2,
        aantal=1,
    )
    eenheid = EenhedenEenheid(id="e323", ruimten=[carport])

    buitenruimten = Buitenruimten(peildatum=PEILDATUM).waardeer(eenheid)
    parkeerruimten = GemeenschappelijkeParkeerruimten(peildatum=PEILDATUM).waardeer(
        eenheid
    )

    assert buitenruimten.punten == 0
    assert parkeerruimten.punten == pytest.approx(3.0)
