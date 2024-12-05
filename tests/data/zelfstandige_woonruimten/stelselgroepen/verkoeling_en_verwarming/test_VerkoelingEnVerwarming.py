from pathlib import Path

from tests.utils import (
    assert_stelselgroep_output,
    assert_stelselgroep_specifiek_output,
    maak_specifieke_input_en_output_model_fixture,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.verkoeling_en_verwarming import (
    VerkoelingEnVerwarming,
)


def test_VerkoelingEnVerwarming_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        VerkoelingEnVerwarming,
    )


specifieke_input_en_output_model = maak_specifieke_input_en_output_model_fixture(
    Path(__file__).absolute().parent
)


def test_VerkoelingEnVerwarming_specifiek_output(
    specifieke_input_en_output_model, peildatum
):
    assert_stelselgroep_specifiek_output(
        specifieke_input_en_output_model,
        peildatum,
        VerkoelingEnVerwarming,
    )
