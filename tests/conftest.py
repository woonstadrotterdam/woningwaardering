import re
from datetime import date, datetime
from pathlib import Path
import warnings

import pytest

from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "tests/data"


@pytest.fixture(
    params=[
        str(p) for p in (DATA_DIR / "zelfstandige_woonruimten/input").glob("*.json")
    ]
)
def zelfstandige_woonruimten_inputmodel(request):
    file_path = request.param
    with open(file_path, "r+") as f:
        eenheid = EenhedenEenheid.model_validate_json(f.read())
    return eenheid


@pytest.fixture(
    params=[
        str(p)
        for p in (DATA_DIR / "zelfstandige_woonruimten/output").rglob("*.json")
        if ".unverified" not in str(p)
    ]
)
def zelfstandige_woonruimten_input_en_outputmodel(
    request,
) -> tuple[EenhedenEenheid, WoningwaarderingResultatenWoningwaarderingResultaat, date]:
    output_file_path = request.param
    file_name = Path(output_file_path).name
    input_file_path = DATA_DIR / "zelfstandige_woonruimten/input" / file_name
    # Extract date from string
    peildatum_match = re.search(r"\d{4}-\d{2}-\d{2}", str(output_file_path))
    if peildatum_match is None:
        raise ValueError(f"geen datum gevonden in bestandsnaam {output_file_path}")
    peildatum = datetime.strptime(peildatum_match.group(0), "%Y-%m-%d").date()

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


# Zorg dat de warnings geen error worden
def pytest_runtest_setup(item):
    warnings.simplefilter("default", UserWarning)


def pytest_runtest_teardown(item, nextitem):
    warnings.resetwarnings()
