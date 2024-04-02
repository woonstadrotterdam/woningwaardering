from datetime import date

from woningwaardering.stelsels.zelfstandige_woonruimten import (
    OppervlakteVanVertrekken,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingGroep,
)


def test_OppervlakteVanVertrekken(eenheid_inputmodel, woningwaardering_resultaat):
    ovv = OppervlakteVanVertrekken(peildatum=date(2025, 1, 1))
    resultaat = ovv.bereken(eenheid_inputmodel, woningwaardering_resultaat)
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep)
