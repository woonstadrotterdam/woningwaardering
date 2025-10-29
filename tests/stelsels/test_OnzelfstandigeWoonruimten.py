from datetime import date

from tests.utils import assert_output_model
from woningwaardering.stelsels.onzelfstandige_woonruimten.onzelfstandige_woonruimten import (
    OnzelfstandigeWoonruimten,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


def test_OnzelfstandigeWoonruimten(onzelfstandige_woonruimten_inputmodel):
    onzelfstandige_woonruimten = OnzelfstandigeWoonruimten(peildatum=date(2025, 1, 1))
    resultaat = onzelfstandige_woonruimten.waardeer(
        onzelfstandige_woonruimten_inputmodel
    )
    assert isinstance(
        resultaat, WoningwaarderingResultatenWoningwaarderingResultaat
    ), f"Resultaat is geen instance van WoningwaarderingResultatenWoningwaarderingResultaat, {type(resultaat) = }"
    assert resultaat.punten is not None


def test_OnzelfstandigeWoonruimtes_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    eenheid_input, verwachte_output = onzelfstandige_woonruimten_input_en_outputmodel
    onzelfstandige_woonruimten = OnzelfstandigeWoonruimten(peildatum=peildatum)
    resultaat = onzelfstandige_woonruimten.waardeer(eenheid_input)
    assert_output_model(resultaat, verwachte_output)
