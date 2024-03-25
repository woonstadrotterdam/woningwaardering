from datetime import datetime
from zoneinfo import ZoneInfo
from woningwaardering.stelsels.zelfstandig import (
    OppervlakteVanVertrekken,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingGroep,
)


def test_OppervlakteVanVertrekken(eenheid_inputmodel, woningwaardering_resultaat):
    ovv = OppervlakteVanVertrekken(
        peildatum=datetime(2025, 1, 1, tzinfo=ZoneInfo("Europe/Amsterdam")).date()
    )
    resultaat = ovv.bereken(eenheid_inputmodel, woningwaardering_resultaat)
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep)
