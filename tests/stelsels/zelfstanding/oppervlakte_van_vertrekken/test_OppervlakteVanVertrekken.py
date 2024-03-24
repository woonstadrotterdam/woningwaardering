from woningwaardering.stelsels.zelfstandig.oppervlakte_van_vertrekken import (
    OppervlakteVanVertrekken,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingGroep,
)


def test_OppervlakteVanVertrekken(eenheid_inputmodel, woningwaardering_resultaat):
    ovv = OppervlakteVanVertrekken(peildatum="01-01-2025")
    resultaat = ovv.bereken(eenheid_inputmodel, woningwaardering_resultaat)
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep)
