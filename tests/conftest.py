from pathlib import Path

import pytest

from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)

BASE_DIR = Path(__file__).parent.parent
INPUT_DIR = BASE_DIR / "data_modellen/input"  # Define the input directory
OUTPUT_DIR = BASE_DIR / "data_modellen/output"  # Define the output directory


@pytest.fixture(params=[str(p) for p in (INPUT_DIR).glob("*.json")])
def eenheid_inputmodel(request):
    file_path = request.param
    with open(file_path, "r+") as f:
        eenheid = EenhedenEenheid.model_validate_json(f.read())
    return eenheid


@pytest.fixture(params=[str(p) for p in (OUTPUT_DIR).glob("*.json")])
def eenheid_input_en_output(request):
    output_file_path = request.param
    file_name = Path(output_file_path).name
    input_file_path = INPUT_DIR / file_name

    # get input model
    with open(input_file_path, "r+") as f:
        eenheid_input = EenhedenEenheid.model_validate_json(f.read())

    # get output model
    with open(output_file_path, "r+") as f:
        eenheid_output = (
            WoningwaarderingResultatenWoningwaarderingResultaat.model_validate_json(
                f.read()
            )
        )

    return eenheid_input, eenheid_output


@pytest.fixture()
def woningwaardering_resultaat():
    return WoningwaarderingResultatenWoningwaarderingResultaat()
