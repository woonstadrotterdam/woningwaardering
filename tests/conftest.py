from collections.abc import Callable, Iterable
from pathlib import Path
from warnings import WarningMessage

import pytest

from tests.peildatum import REFERENTIE_PEILDATUM
from tests.testreferenties import (
    BIJWERKOPTIE,
    maak_testreferentie,
    pad_van_testreferentie,
    vergelijk_of_werk_bij,
)
from tests.utils import assert_invarianten_van_groep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "tests/data"


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption(
        BIJWERKOPTIE,
        action="store_true",
        help="Schrijf de testreferenties in plaats van ermee te vergelijken. "
        "Gebruik hiervoor `task genereer-test-output`.",
    )


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line(
        "markers",
        "toelichting(tekst): waarom dit geval van een geparametriseerde waarderingstest "
        "bestaat; de tekst komt in de testreferentie",
    )


@pytest.fixture()
def peildatum():
    return REFERENTIE_PEILDATUM


@pytest.fixture()
def vergelijk_met_testreferentie(
    request: pytest.FixtureRequest, recwarn: pytest.WarningsRecorder
) -> Callable[..., None]:
    """Vergelijk een waardering met de testreferentie van deze test.

    De testreferentie bevat de docstring van de test, het rapport, de
    waarschuwingen, de input als VERA-JSON en de output-JSON. Wijkt de
    waardering af of ontbreekt de testreferentie, dan faalt de test. Bijwerken kan
    alleen met `task genereer-test-output`.

    Daarnaast gelden voor elke vergeleken waardering de invarianten uit
    `assert_invarianten_van_groep`, en faalt de test bij een `UserWarning` die
    niet met `pytest.warns` is opgevangen en meegegeven.
    """
    vergeleken = False

    def _vergelijk(
        eenheid: EenhedenEenheid,
        groep: WoningwaarderingResultatenWoningwaarderingGroep,
        waarschuwingen: Iterable[WarningMessage] = (),
    ) -> None:
        nonlocal vergeleken
        assert (
            not vergeleken
        ), "Roep vergelijk_met_testreferentie één keer per test aan."
        vergeleken = True
        waarschuwingen = list(waarschuwingen)
        meegegeven = {str(w.message) for w in waarschuwingen}
        onverwacht = [
            str(w.message)
            for w in recwarn
            if issubclass(w.category, UserWarning) and str(w.message) not in meegegeven
        ]
        assert not onverwacht, (
            "Onverwachte waarschuwing. Vang een verwachte waarschuwing op met "
            f"pytest.warns en geef hem mee aan vergelijk_met_testreferentie: {onverwacht}"
        )
        assert_invarianten_van_groep(groep)
        vergelijk_of_werk_bij(
            pad_van_testreferentie(request.node),
            maak_testreferentie(request.node, eenheid, groep, waarschuwingen),
            bijwerken=request.config.getoption(BIJWERKOPTIE),
        )

    return _vergelijk


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
) -> tuple[EenhedenEenheid, WoningwaarderingResultatenWoningwaarderingResultaat]:
    output_file_path = request.param
    file_name = Path(output_file_path).name
    input_file_path = DATA_DIR / "zelfstandige_woonruimten/input" / file_name

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


@pytest.fixture(
    params=[
        str(p) for p in (DATA_DIR / "onzelfstandige_woonruimten/input").glob("*.json")
    ]
)
def onzelfstandige_woonruimten_inputmodel(request):
    file_path = request.param
    with open(file_path, "r+") as f:
        eenheid = EenhedenEenheid.model_validate_json(f.read())
    return eenheid


@pytest.fixture(
    params=[
        str(p)
        for p in (DATA_DIR / "onzelfstandige_woonruimten/output").rglob("*.json")
        if ".unverified" not in str(p)
    ]
)
def onzelfstandige_woonruimten_input_en_outputmodel(
    request,
) -> tuple[EenhedenEenheid, WoningwaarderingResultatenWoningwaarderingResultaat]:
    output_file_path = request.param
    file_name = Path(output_file_path).name
    input_file_path = DATA_DIR / "onzelfstandige_woonruimten/input" / file_name

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
