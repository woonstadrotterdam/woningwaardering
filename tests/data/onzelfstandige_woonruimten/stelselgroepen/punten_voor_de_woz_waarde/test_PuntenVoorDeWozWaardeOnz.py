from datetime import date
from pathlib import Path

import pytest

from tests.utils import (
    WarningConfig,
    assert_output_model,
    laad_specifiek_input_en_output_model,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten import PuntenVoorDeWozWaarde
from woningwaardering.stelsels.utils import normaliseer_ruimte_namen
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
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


def test_PuntenVoorDeWozWaarde_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    eenheid_input, eenheid_output = onzelfstandige_woonruimten_input_en_outputmodel

    normaliseer_ruimte_namen(eenheid_input)

    stelselgroep = PuntenVoorDeWozWaarde(peildatum=peildatum)

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [stelselgroep.waardeer(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.punten_voor_de_woz_waarde,
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
        file=f"{current_file_path}/input/geen_geldige_woz_waarde.json",
        peildatum=date(2024, 1, 1),
        warnings={
            UserWarning: "geen WOZ-waarde",
        },
    ),
]


@pytest.mark.filterwarnings("ignore::UserWarning")
@pytest.mark.parametrize("warning_config", warning_configs)
def test_PuntenVoorDeWozWaarde_specifiek_warnings(warning_config, peildatum):
    if peildatum < warning_config.peildatum:
        pytest.skip(f"Warning is niet van toepassing op peildatum: {peildatum}")

    with open(warning_config.file, "r+") as f:
        eenheid_input = EenhedenEenheid.model_validate_json(f.read())

    with pytest.warns() as records:
        woz = PuntenVoorDeWozWaarde(peildatum=peildatum)
        woz.waardeer(eenheid_input)

        warning_message = [(r.category, str(r.message)) for r in records]
        for warning_type, warning_message in warning_config.warnings.items():
            assert any(
                [
                    warning_type == r.category and warning_message in str(r.message)
                    for r in records
                ]
            ), f"Geen {warning_type} met message '{warning_message}' geraised"
