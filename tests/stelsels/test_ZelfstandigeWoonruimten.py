from deepdiff import DeepDiff
from loguru import logger

from woningwaardering.stelsels.zelfstandige_woonruimten.zelfstandige_woonruimten import (
    ZelfstandigeWoonruimten,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


def detailed_model_comparison(model_a, model_b):
    for field in model_a.__fields__:
        val_a, val_b = getattr(model_a, field), getattr(model_b, field)
        assert val_a == val_b, f"Field '{field}' differs: {val_a = } != {val_b = }"


def test_ZelfstandigeWoonruimten(eenheid_inputmodel):
    zelfstandige_woonruimten = ZelfstandigeWoonruimten()
    resultaat = zelfstandige_woonruimten.bereken(eenheid_inputmodel)
    assert isinstance(
        resultaat, WoningwaarderingResultatenWoningwaarderingResultaat
    ), f"Resultaat is geen instance van WoningwaarderingResultatenWoningwaarderingResultaat, {type(resultaat) = }"
    assert resultaat.punten is not None


def test_ZelfstandigeWoonruimtes_output(eenheid_input_en_output):
    eenheid_input, eenheid_output = eenheid_input_en_output
    zelfstandige_woonruimten = ZelfstandigeWoonruimten()
    resultaat = zelfstandige_woonruimten.bereken(eenheid_input)
    diffresult = DeepDiff(resultaat.model_dump(), eenheid_output.model_dump())
    if diffresult:
        logger.error(diffresult.to_json(indent=2))
        raise ValueError(f"Models are not equal: {diffresult}")
