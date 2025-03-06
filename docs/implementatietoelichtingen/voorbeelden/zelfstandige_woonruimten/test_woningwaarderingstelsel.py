import warnings
import pytest

@pytest.fixture
def zelfstandige_woonruimte_pydantic():
    # include-start
    from woningwaardering.vera.bvg.generated import EenhedenEenheid
    from woningwaardering.vera.referentiedata import Woningwaarderingstelsel

    eenheid = EenhedenEenheid()
    eenheid.woningwaarderingstelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
    # include-end

    return eenheid

@pytest.fixture
def zelfstandige_woonruimte_json():
    from woningwaardering.vera.bvg.generated import EenhedenEenheid

    with open("tests/docs/zelfstandige_woonruimten/woningwaarderingstelsel.json", "r") as f:
        json_data = f.read()
        # Then parse as regular EenhedenEenheid
        return EenhedenEenheid.model_validate_json(json_data)

def test_zelfstandige_woonruimten_pydantic(zelfstandige_woonruimte_pydantic):
    with warnings.catch_warnings(record=True) as warning_list:
        assert len(warning_list) == 0, f"{[str(w.message) for w in warning_list]}"

def test_zelfstandige_woonruimten_json(zelfstandige_woonruimte_json):
    with warnings.catch_warnings(record=True) as warning_list:
        assert len(warning_list) == 0, f"{[str(w.message) for w in warning_list]}"

def test_zelfstandige_woonruimten_pydantic_equals_json(zelfstandige_woonruimte_pydantic, zelfstandige_woonruimte_json):
    assert zelfstandige_woonruimte_pydantic == zelfstandige_woonruimte_json
