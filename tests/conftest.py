import pathlib

import pytest

from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)

BASE_DIR = pathlib.Path(__file__).parent.parent


@pytest.fixture(params=[str(p) for p in (BASE_DIR / "input_modellen").glob("*.json")])
def eenheid_inputmodel(request):
    file_path = request.param
    with open(file_path, "r+") as f:
        eenheid = EenhedenEenheid.model_validate_json(f.read())
    return eenheid


@pytest.fixture()
def woningwaardering_resultaat():
    return WoningwaarderingResultatenWoningwaarderingResultaat()
