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
from woningwaardering.stelsels.onzelfstandige_woonruimten import PuntenVoorDeWozWaarde


def test_PuntenVoorDeWozWaarde_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        onzelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        PuntenVoorDeWozWaarde,
    )


current_file_path = Path(__file__).absolute().parent
specifieke_input_en_output_model = maak_specifieke_input_en_output_model_fixture(
    current_file_path
)


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_PuntenVoorDeWozWaarde_specifiek_output(
    specifieke_input_en_output_model, peildatum
):
    assert_stelselgroep_specifiek_output(
        specifieke_input_en_output_model,
        peildatum,
        PuntenVoorDeWozWaarde,
    )


warning_configs = [
    WarningConfig(
        file=f"{current_file_path}/input/geen_geldige_woz_waarde.json",
        peildatum=date(2025, 1, 1),
        warnings={
            UserWarning: "geen WOZ-waarde",
        },
    ),
    WarningConfig(
        file=f"{current_file_path}/input/inconsistent_adres.json",
        peildatum=date(2025, 1, 1),
        warnings={
            UserWarning: "woonplaats",
        },
    ),
]


@pytest.mark.filterwarnings("ignore::UserWarning")
@pytest.mark.parametrize("warning_config", warning_configs)
def test_PuntenVoorDeWozWaarde_specifiek_warnings(warning_config, peildatum):
    assert_stelselgroep_warnings(warning_config, peildatum, PuntenVoorDeWozWaarde)
