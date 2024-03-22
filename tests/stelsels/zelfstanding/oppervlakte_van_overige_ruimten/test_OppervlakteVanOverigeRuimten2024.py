from woningwaardering.stelsels.zelfstandig.oppervlakte_van_overige_ruimten import (
    OppervlakteVanOverigeRuimten2024,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingGroep,
)


def test_OppervlakteVanOverigeRuimten2024(
    eenheid_inputmodel, woningwaardering_resultaat
):
    resultaat = OppervlakteVanOverigeRuimten2024.bereken(
        eenheid_inputmodel, woningwaardering_resultaat
    )
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep)
