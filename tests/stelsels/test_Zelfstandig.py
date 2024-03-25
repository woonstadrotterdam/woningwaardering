from woningwaardering.stelsels.zelfstandig.zelfstandig import Zelfstandig
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


def test_Zelfstandig(eenheid_inputmodel):
    zelfstandig = Zelfstandig()
    resultaat = zelfstandig.bereken(eenheid_inputmodel)
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingResultaat)
    assert resultaat.punten is not None
