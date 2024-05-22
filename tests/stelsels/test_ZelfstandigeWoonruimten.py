from test_utils import assert_output_model

from woningwaardering.stelsels.zelfstandige_woonruimten import (
    ZelfstandigeWoonruimten,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


def test_ZelfstandigeWoonruimten(zelfstandige_woonruimten_inputmodel):
    zelfstandige_woonruimten = ZelfstandigeWoonruimten()
    resultaat = zelfstandige_woonruimten.bereken(zelfstandige_woonruimten_inputmodel)
    assert isinstance(
        resultaat, WoningwaarderingResultatenWoningwaarderingResultaat
    ), f"Resultaat is geen instance van WoningwaarderingResultatenWoningwaarderingResultaat, {type(resultaat) = }"
    assert resultaat.punten is not None


def test_ZelfstandigeWoonruimtes_output(zelfstandige_woonruimten_input_en_outputmodel):
    eenheid_input, verwachte_output, peildatum = (
        zelfstandige_woonruimten_input_en_outputmodel
    )
    zelfstandige_woonruimten = ZelfstandigeWoonruimten(peildatum=peildatum)
    resultaat = zelfstandige_woonruimten.bereken(eenheid_input)
    assert_output_model(resultaat, verwachte_output)
