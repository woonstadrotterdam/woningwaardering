from datetime import date
from pathlib import Path

import pytest

from tests.utils import (
    WarningConfig,
    assert_output_model,
    assert_stelselgroep_output_in_eenheid_output,
    assert_stelselgroep_warnings,
    laad_specifiek_input_en_output_model,
)
from woningwaardering.stelsels.zelfstandige_woonruimten import PuntenVoorDeWozWaarde
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep


def test_PuntenVoorDeWozWaarde_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output_in_eenheid_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        PuntenVoorDeWozWaarde,
    )


# Get the absolute path to the current file
current_file_path = Path(__file__).absolute().parent


@pytest.fixture(params=[str(p) for p in (current_file_path / "output").rglob("*.json")])
def specifieke_input_en_output_model(request):
    output_file_path = request.param
    return laad_specifiek_input_en_output_model(
        current_file_path, Path(output_file_path)
    )


# In deze test data zit expres missende data
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_PuntenVoorDeWozWaarde_specifiek_output(
    specifieke_input_en_output_model, peildatum
):
    eenheid_input, eenheid_output = specifieke_input_en_output_model
    stelselgroep = PuntenVoorDeWozWaarde(peildatum=peildatum)

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [stelselgroep.waardeer(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.punten_voor_de_woz_waarde,
    )


warning_configs = [
    WarningConfig(
        file=f"{current_file_path}/input/geen_woz.json",
        peildatum=date(2024, 1, 1),
        warnings={
            UserWarning: "geen WOZ-waarde",
        },
    ),
]


@pytest.mark.filterwarnings("ignore::UserWarning")
@pytest.mark.parametrize("warning_config", warning_configs)
def test_PuntenVoorDeWozWaarde_specifiek_warnings(warning_config, peildatum):
    assert_stelselgroep_warnings(warning_config, peildatum, PuntenVoorDeWozWaarde)
