from datetime import date
from pathlib import Path

import pytest

from tests.utils import (
    WarningConfig,
    assert_output_model,
    laad_specifiek_input_en_output_model,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten.gemeenschappelijke_parkeerruimten import (
    GemeenschappelijkeParkeerruimten,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata.woningwaarderingstelselgroep import (
    Woningwaarderingstelselgroep,
)

# Get the absolute path to the current file
current_file_path = Path(__file__).absolute().parent


@pytest.fixture(params=[str(p) for p in (current_file_path / "output").rglob("*.json")])
def specifieke_input_en_output_model(request):
    output_file_path = request.param
    return laad_specifiek_input_en_output_model(
        current_file_path, Path(output_file_path)
    )


def test_GemeenschappelijkeParkeerruimten(
    onzelfstandige_woonruimten_inputmodel, woningwaardering_resultaat, peildatum
):
    gemeenschappelijke_parkeerruimten = GemeenschappelijkeParkeerruimten(
        peildatum=peildatum
    )
    resultaat = gemeenschappelijke_parkeerruimten.waardeer(
        onzelfstandige_woonruimten_inputmodel, woningwaardering_resultaat
    )
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep)


def test_GemeenschappelijkeParkeerruimten_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    eenheid_input, eenheid_output = onzelfstandige_woonruimten_input_en_outputmodel
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
    if peildatum < warning_config.peildatum:
        pytest.skip(f"Warning is niet van toepassing op peildatum: {peildatum}")

    with open(warning_config.file, "r+") as f:
        eenheid_input = EenhedenEenheid.model_validate_json(f.read())

    with pytest.warns() as records:
        gemeenschappelijke_parkeerruimten = GemeenschappelijkeParkeerruimten(
            peildatum=peildatum
        )
        gemeenschappelijke_parkeerruimten.waardeer(eenheid_input)

        warning_message = [(r.category, str(r.message)) for r in records]
        for warning_type, warning_message in warning_config.warnings.items():
            assert any(
                [
                    warning_type == r.category and warning_message in str(r.message)
                    for r in records
                ]
            ), f"Geen {warning_type} met message '{warning_message}' geraised"
