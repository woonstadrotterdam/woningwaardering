from pathlib import Path

from tests.utils import (
    assert_stelselgroep_output,
    assert_stelselgroep_specifiek_output,
    maak_specifieke_input_en_output_model_fixture,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten import (
    OppervlakteVanVertrekken,
)


def test_OppervlakteVanVertrekken_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        onzelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        OppervlakteVanVertrekken,
    )


specifieke_input_en_output_model = maak_specifieke_input_en_output_model_fixture(
    Path(__file__).parent
)


def test_OppervlakteVanVertrekken_specifiek_output(
    specifieke_input_en_output_model, peildatum
):
    assert_stelselgroep_specifiek_output(
        specifieke_input_en_output_model,
        peildatum,
        OppervlakteVanVertrekken,
    )
