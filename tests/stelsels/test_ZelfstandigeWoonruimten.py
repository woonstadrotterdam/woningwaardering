from test_utils import assert_output_model

from woningwaardering.stelsels.zelfstandige_woonruimten.zelfstandige_woonruimten import (
    ZelfstandigeWoonruimten,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


def test_ZelfstandigeWoonruimten(eenheid_inputmodel):
    zelfstandige_woonruimten = ZelfstandigeWoonruimten()
    resultaat = zelfstandige_woonruimten.bereken(eenheid_inputmodel)
    assert isinstance(
        resultaat, WoningwaarderingResultatenWoningwaarderingResultaat
    ), f"Resultaat is geen instance van WoningwaarderingResultatenWoningwaarderingResultaat, {type(resultaat) = }"
    assert resultaat.punten is not None


def test_ZelfstandigeWoonruimtes_output(eenheid_input_en_output):
    eenheid_input, verwachte_output, peildatum = eenheid_input_en_output
    zelfstandige_woonruimten = ZelfstandigeWoonruimten(peildatum=peildatum)
    resultaat = zelfstandige_woonruimten.bereken(eenheid_input)
    assert_output_model(resultaat, verwachte_output)
