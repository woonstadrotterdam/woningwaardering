from woningwaardering.stelsels.zelfstandige_woonruimten.zelfstandige_woonruimten import (
    ZelfstandigeWoonruimten,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


def test_ZelfstandigeWoonruimten(eenheid_inputmodel):
    zelfstandige_woonruimten = ZelfstandigeWoonruimten()
    resultaat = zelfstandige_woonruimten.bereken(eenheid_inputmodel)
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingResultaat)
    assert resultaat.punten is not None
