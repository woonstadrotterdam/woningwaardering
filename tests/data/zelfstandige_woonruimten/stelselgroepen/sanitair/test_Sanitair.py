from datetime import date
from pathlib import Path

import pytest

from tests.utils import (
    WarningConfig,
    assert_output_model,
    laad_specifiek_input_en_output_model,
)
from woningwaardering.stelsels.utils import normaliseer_ruimte_namen
from woningwaardering.stelsels.zelfstandige_woonruimten import (
    Sanitair,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep

# Get the absolute path to the current file
current_file_path = Path(__file__).absolute().parent


@pytest.fixture(params=[str(p) for p in (current_file_path / "output").rglob("*.json")])
def specifieke_input_en_output_model(request):
    output_file_path = request.param
    return laad_specifiek_input_en_output_model(
        current_file_path, Path(output_file_path)
    )


def test_Sanitair(
    zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat, peildatum
):
    sanitair = Sanitair(peildatum=peildatum)
    resultaat = sanitair.waardeer(
        zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat
    )
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep)


def test_Sanitair_output(zelfstandige_woonruimten_input_en_outputmodel, peildatum):
    eenheid_input, eenheid_output = zelfstandige_woonruimten_input_en_outputmodel

    normaliseer_ruimte_namen(eenheid_input)

    sanitair = Sanitair(peildatum=peildatum)

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [sanitair.waardeer(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.sanitair,
    )


def test_Sanitair_specifiek_output(specifieke_input_en_output_model, peildatum):
    eenheid_input, eenheid_output = specifieke_input_en_output_model
    sanitair = Sanitair(peildatum=peildatum)

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [sanitair.waardeer(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.sanitair,
    )


warning_configs = [
    WarningConfig(
        file=f"{current_file_path}/input/ingebouwd_kastje_met_wastafel_zonder_wastafel.json",
        peildatum=date(2024, 7, 1),
        warnings={
            UserWarning: "wastafel",
        },
    ),
]


@pytest.mark.filterwarnings("ignore::UserWarning")
@pytest.mark.parametrize("warning_config", warning_configs)
def test_Sanitair_specifiek_warnings(warning_config, peildatum):
    if peildatum < warning_config.peildatum:
        pytest.skip(f"Warning is niet van toepassing op peildatum: {peildatum}")

    with open(warning_config.file, "r+") as f:
        eenheid_input = EenhedenEenheid.model_validate_json(f.read())

    with pytest.warns() as records:
        sanitair = Sanitair(peildatum=peildatum)
        sanitair.waardeer(eenheid_input)

        warning_message = [(r.category, str(r.message)) for r in records]
        for warning_type, warning_message in warning_config.warnings.items():
            assert any(
                [
                    warning_type == r.category and warning_message in str(r.message)
                    for r in records
                ]
            ), f"Geen {warning_type} met message '{warning_message}' geraised"
