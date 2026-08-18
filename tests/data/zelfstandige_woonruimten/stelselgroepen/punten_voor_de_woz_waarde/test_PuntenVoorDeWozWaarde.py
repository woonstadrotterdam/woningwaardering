from pathlib import Path

import pytest

from tests.utils import (
    WarningConfig,
    assert_stelselgroep_output,
    assert_stelselgroep_specifiek_output,
    assert_stelselgroep_warnings,
    maak_specifieke_input_en_output_model_fixture,
)
from woningwaardering.stelsels.builders import WaarderingsgroepBuilder
from woningwaardering.stelsels.zelfstandige_woonruimten import PuntenVoorDeWozWaarde
from woningwaardering.stelsels.zelfstandige_woonruimten.punten_voor_de_woz_waarde.punten_voor_de_woz_waarde import (
    NIEUWBOUW_MINIMUM_PUNTEN_CRITERIUM_ID,
    NIEUWBOUW_MINIMUM_PUNTEN_ID,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


def test_PuntenVoorDeWozWaarde_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        zelfstandige_woonruimten_input_en_outputmodel,
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
        file=f"{current_file_path}/input/geen_woz.json",
        warnings={
            UserWarning: "geen WOZ-waarde",
        },
    ),
]


@pytest.mark.filterwarnings("ignore::UserWarning")
@pytest.mark.parametrize("warning_config", warning_configs)
def test_PuntenVoorDeWozWaarde_specifiek_warnings(warning_config, peildatum):
    assert_stelselgroep_warnings(warning_config, peildatum, PuntenVoorDeWozWaarde)


def test_nieuwbouw_minimum_criterium_id_komt_overeen_met_builder_pad():
    builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        Woningwaarderingstelselgroep.punten_voor_de_woz_waarde,
    )
    waardering = builder.met_onderliggend(
        id=NIEUWBOUW_MINIMUM_PUNTEN_ID,
        naam="Nieuwbouwminimum",
        punten=1,
    )
    assert (
        NIEUWBOUW_MINIMUM_PUNTEN_CRITERIUM_ID
        == "punten_voor_de_woz_waarde__nieuwbouw_minimum_punten"
    )
    assert waardering.criterium_id == NIEUWBOUW_MINIMUM_PUNTEN_CRITERIUM_ID
