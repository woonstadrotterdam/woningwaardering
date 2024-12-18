from datetime import date
from pathlib import Path

import pytest

from tests.utils import (
    WarningConfig,
    assert_stelselgroep_output,
    assert_stelselgroep_specifiek_output,
    assert_stelselgroep_warnings,
    maak_specifieke_input_en_output_model_fixture,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.gemeenschappelijke_parkeerruimten import (
    GemeenschappelijkeParkeerruimten,
)


def test_GemeenschappelijkeParkeerruimten_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        GemeenschappelijkeParkeerruimten,
    )


current_file_path = Path(__file__).absolute().parent
specifieke_input_en_output_model = maak_specifieke_input_en_output_model_fixture(
    current_file_path
)


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_GemeenschappelijkeParkeerruimten_specifiek_output(
    specifieke_input_en_output_model, peildatum
):
    assert_stelselgroep_specifiek_output(
        specifieke_input_en_output_model,
        peildatum,
        GemeenschappelijkeParkeerruimten,
    )


warning_configs = [
    WarningConfig(
        file=f"{current_file_path}/input/warning_geen_oppervlakte.json",
        peildatum=date(2025, 1, 1),
        warnings={
            UserWarning: "oppervlakte",
        },
    ),
    WarningConfig(
        file=f"{current_file_path}/input/warning_gedeeld_met_aantal_eenheden.json",
        peildatum=date(2025, 1, 1),
        warnings={
            UserWarning: "gedeeld_met_aantal_eenheden",
        },
    ),
]


@pytest.mark.filterwarnings("ignore::UserWarning")
@pytest.mark.parametrize("warning_config", warning_configs)
def test_GemeenschappelijkeParkeerruimten_specifiek_warnings(warning_config, peildatum):
    assert_stelselgroep_warnings(
        warning_config, peildatum, GemeenschappelijkeParkeerruimten
    )
