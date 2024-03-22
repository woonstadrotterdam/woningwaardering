from woningwaardering.bereken import Woningwaardering
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


def test_Woningwaardering(eenheid_inputmodel, woningwaardering_resultaat):
    wws = Woningwaardering()
    resultaat = wws.bereken(eenheid_inputmodel, woningwaardering_resultaat)
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingResultaat)
