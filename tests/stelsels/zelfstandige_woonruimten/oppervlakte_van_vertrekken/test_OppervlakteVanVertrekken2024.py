from woningwaardering.stelsels.zelfstandige_woonruimten.oppervlakte_van_vertrekken import (
    OppervlakteVanVertrekken2024,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingGroep,
)


def test_OppervlakteVanVertrekken2024(eenheid_inputmodel, woningwaardering_resultaat):
    resultaat = OppervlakteVanVertrekken2024.bereken(
        eenheid_inputmodel, woningwaardering_resultaat
    )
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep)
