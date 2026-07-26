from pathlib import Path

import pytest

from tests.utils import (
    WarningConfig,
    assert_stelselgroep_output,
    assert_stelselgroep_specifiek_output,
    assert_stelselgroep_warnings,
    maak_specifieke_input_en_output_model_fixture,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten import (
    Energieprestatie,
)


def test_Energieprestatie_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        onzelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        Energieprestatie,
    )


current_file_path = Path(__file__).absolute().parent
specifieke_input_en_output_model = maak_specifieke_input_en_output_model_fixture(
    current_file_path
)


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_Energieprestatie_specifiek_output(specifieke_input_en_output_model, peildatum):
    assert_stelselgroep_specifiek_output(
        specifieke_input_en_output_model,
        peildatum,
        Energieprestatie,
    )


warning_configs = [
    WarningConfig(
        file=f"{current_file_path}/warning_geen_ruimten/input.json",
        warnings={
            UserWarning: "geen ruimten gevonden",
        },
    ),
    WarningConfig(
        file=f"{current_file_path}/warning_ruimte_zonder_oppervlakte/input.json",
        warnings={
            UserWarning: "heeft geen oppervlakte",
        },
    ),
]


@pytest.mark.filterwarnings("ignore::UserWarning")
@pytest.mark.parametrize("warning_config", warning_configs)
def test_Energieprestatie_specifiek_warnings(warning_config, peildatum):
    assert_stelselgroep_warnings(warning_config, peildatum, Energieprestatie)
