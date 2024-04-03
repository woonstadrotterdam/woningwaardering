import re
from datetime import datetime
from pathlib import Path

import pytest

from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)

BASE_DIR = Path(__file__).parent.parent
INPUT_DIR = BASE_DIR / "data_modellen/input"  # Define the input directory
OUTPUT_DIR = BASE_DIR / "data_modellen/output/peildatum"  # Define the output directory


@pytest.fixture(params=[str(p) for p in (INPUT_DIR).glob("*.json")])
def eenheid_inputmodel(request):
    file_path = request.param
    with open(file_path, "r+") as f:
        eenheid = EenhedenEenheid.model_validate_json(f.read())
    return eenheid


@pytest.fixture(params=[str(p) for p in (OUTPUT_DIR).rglob("*.json")])
def eenheid_input_en_output(request):
    output_file_path = request.param
    print(f"output_file_path: {output_file_path}")
    file_name = Path(output_file_path).name
    input_file_path = INPUT_DIR / file_name
    # Extract date from string
    peildatum = re.search(r"\d{4}-\d{2}-\d{2}", output_file_path).group(0)
    peildatum = datetime.strptime(peildatum, "%Y-%m-%d").date()

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

    return eenheid_input, eenheid_output, peildatum


@pytest.fixture()
def woningwaardering_resultaat():
    return WoningwaarderingResultatenWoningwaarderingResultaat()
