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
from woningwaardering.stelsels.zelfstandige_woonruimten.gemeenschappelijke_parkeerruimten import (
    GemeenschappelijkeParkeerruimten,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata.woningwaarderingstelselgroep import (
    Woningwaarderingstelselgroep,
)


def test_GemeenschappelijkeParkeerruimten_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output_in_eenheid_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        GemeenschappelijkeParkeerruimten,
    )


current_file_path = Path(__file__).absolute().parent


@pytest.fixture(params=[str(p) for p in (current_file_path / "output").rglob("*.json")])
def specifieke_input_en_output_model(request):
    output_file_path = request.param
    return laad_specifiek_input_en_output_model(
        current_file_path, Path(output_file_path)
    )


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_GemeenschappelijkeParkeerruimten_specifiek_output(
    specifieke_input_en_output_model, peildatum
):
    eenheid_input, eenheid_output = specifieke_input_en_output_model
    gemeenschappelijke_parkeerruimten = GemeenschappelijkeParkeerruimten(
        peildatum=peildatum
    )
    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [gemeenschappelijke_parkeerruimten.waardeer(eenheid_input)]
    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten,
    )


warning_configs = [
    WarningConfig(
        file=f"{current_file_path}/input/warning_geen_oppervlakte.json",
        peildatum=date(2024, 7, 1),
        warnings={
            UserWarning: "oppervlakte",
        },
    ),
    WarningConfig(
        file=f"{current_file_path}/input/warning_gedeeld_met_aantal_eenheden.json",
        peildatum=date(2024, 7, 1),
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
