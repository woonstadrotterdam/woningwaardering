from woningwaardering.stelsels.zelfstandig.zelfstandig import Zelfstandig
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


def test_Zelfstandig(eenheid_inputmodel, woningwaardering_resultaat):
    zelfstandig = Zelfstandig()
    resultaat = zelfstandig.bereken(eenheid_inputmodel, woningwaardering_resultaat)
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingResultaat)
    assert resultaat.punten is not None
