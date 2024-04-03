# from deepdiff import DeepDiff
# from loguru import logger
from test_utils import assert_output_model

from woningwaardering.stelsels.zelfstandige_woonruimten import (
    OppervlakteVanVertrekken,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingGroep,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep


def test_OppervlakteVanVertrekken(eenheid_inputmodel, woningwaardering_resultaat):
    ovz = OppervlakteVanVertrekken()
    resultaat = ovz.bereken(eenheid_inputmodel, woningwaardering_resultaat)
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep)


def test_OppervlakteVanVertrekken_output(eenheid_input_en_output):
    eenheid_input, eenheid_output, peildatum = eenheid_input_en_output
    ovz = OppervlakteVanVertrekken(peildatum=peildatum)
    resultaat = ovz.bereken(eenheid_input)

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.oppervlakte_van_vertrekken,
    )
