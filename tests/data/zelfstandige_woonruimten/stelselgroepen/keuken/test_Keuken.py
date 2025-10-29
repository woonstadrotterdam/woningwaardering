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
from woningwaardering.stelsels.zelfstandige_woonruimten.keuken import (
    Keuken,
)


def test_Keuken_output(zelfstandige_woonruimten_input_en_outputmodel, peildatum):
    assert_stelselgroep_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        Keuken,
    )


current_file_path = Path(__file__).absolute().parent
specifieke_input_en_output_model = maak_specifieke_input_en_output_model_fixture(
    current_file_path
)


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_Keuken_specifiek_output(specifieke_input_en_output_model, peildatum):
    assert_stelselgroep_specifiek_output(
        specifieke_input_en_output_model,
        peildatum,
        Keuken,
    )


warning_configs = [
    WarningConfig(
        file=f"{current_file_path}/input/aanrecht_zonder_lengte.json",
        peildatum=date(2025, 1, 1),
        warnings={
            UserWarning: "geen aanrecht",
        },
    ),
    WarningConfig(
        file=f"{current_file_path}/input/keuken_zonder_aanrecht.json",
        peildatum=date(2025, 1, 1),
        warnings={
            UserWarning: "geen aanrecht",
        },
    ),
    WarningConfig(
        file=f"{current_file_path}/input/2_aanrechten_waarvan_1_geen_lengte.json",
        peildatum=date(2025, 1, 1),
        warnings={
            UserWarning: "geen lengte",
        },
    ),
    WarningConfig(
        file=f"{current_file_path}/input/2_aanrechten_waarvan_1_geen_detailsoort.json",
        peildatum=date(2025, 1, 1),
        warnings={
            UserWarning: "geen detailsoort",
        },
    ),
]


@pytest.mark.filterwarnings("ignore::UserWarning")
@pytest.mark.parametrize("warning_config", warning_configs)
def test_Keuken_specifiek_warnings(warning_config, peildatum):
    assert_stelselgroep_warnings(warning_config, peildatum, Keuken)
