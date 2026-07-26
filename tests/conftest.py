from pathlib import Path

import pytest

from tests.peildatum import REFERENTIE_PEILDATUM
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)

BASE_DIR = Path(__file__).parent.parent
STELSELS_DIR = BASE_DIR / "tests/stelsels"

STELSELS = ("zelfstandige_woonruimten", "onzelfstandige_woonruimten")


def _eenheid_case_dirs(stelsel: str) -> list[Path]:
    eenheden_dir = STELSELS_DIR / stelsel / "eenheden"
    if not eenheden_dir.exists():
        return []
    return sorted(p.parent for p in eenheden_dir.glob("*/input.json"))


def _laad_eenheid(case_dir: Path) -> EenhedenEenheid:
    with open(case_dir / "input.json", "r+") as f:
        return EenhedenEenheid.model_validate_json(f.read())


def _laad_eenheid_en_output(
    case_dir: Path,
) -> tuple[EenhedenEenheid, WoningwaarderingResultatenWoningwaarderingResultaat]:
    with open(case_dir / "input.json", "r+") as f:
        eenheid_input = EenhedenEenheid.model_validate_json(f.read())

    with open(case_dir / "output.json", "r+") as f:
        eenheid_output = (
            WoningwaarderingResultatenWoningwaarderingResultaat.model_validate_json(
                f.read()
            )
        )

    return eenheid_input, eenheid_output


@pytest.fixture()
def peildatum():
    return REFERENTIE_PEILDATUM


@pytest.fixture(params=[str(p) for p in _eenheid_case_dirs("zelfstandige_woonruimten")])
def zelfstandige_woonruimten_inputmodel(request):
    return _laad_eenheid(Path(request.param))


@pytest.fixture(
    params=[
        str(p)
        for p in _eenheid_case_dirs("zelfstandige_woonruimten")
        if (p / "output.json").exists() and ".unverified" not in str(p)
    ]
)
def zelfstandige_woonruimten_input_en_outputmodel(
    request,
) -> tuple[EenhedenEenheid, WoningwaarderingResultatenWoningwaarderingResultaat]:
    return _laad_eenheid_en_output(Path(request.param))


@pytest.fixture(
    params=[str(p) for p in _eenheid_case_dirs("onzelfstandige_woonruimten")]
)
def onzelfstandige_woonruimten_inputmodel(request):
    return _laad_eenheid(Path(request.param))


@pytest.fixture(
    params=[
        str(p)
        for p in _eenheid_case_dirs("onzelfstandige_woonruimten")
        if (p / "output.json").exists() and ".unverified" not in str(p)
    ]
)
def onzelfstandige_woonruimten_input_en_outputmodel(
    request,
) -> tuple[EenhedenEenheid, WoningwaarderingResultatenWoningwaarderingResultaat]:
    return _laad_eenheid_en_output(Path(request.param))


@pytest.fixture()
def woningwaardering_resultaat():
    return WoningwaarderingResultatenWoningwaarderingResultaat()


def pytest_runtest_makereport(item: pytest.Item, call: pytest.CallInfo):
    # Controleer of de test een exception heeft gegeven
    if call.excinfo is not None:
        # Controleer of de exception een NotImplementedError is
        if call.excinfo is NotImplementedError:
            # Maak een aangepast rapport om de test over te slaan
            rep = pytest.TestReport.from_item_and_call(item, call)
            rep.outcome = "skipped"
            rep.longrepr = call.excinfo
            return rep
