from collections.abc import Callable, Iterable
from pathlib import Path
from warnings import WarningMessage

import pytest

from tests.peildatum import REFERENTIE_PEILDATUM
from tests.testreferenties import (
    BIJWERKOPTIE,
    assert_geen_onverwachte_waarschuwingen,
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
    """Geef de functie waarmee een waarderingstest afsluit.

    De functie doet drie dingen, in deze volgorde:

    1. Ze faalt bij een `UserWarning` die de test niet heeft meegegeven.
    2. Ze controleert de invarianten die voor elke gewaardeerde stelselgroep
       gelden, zie `assert_invarianten_van_groep`.
    3. Ze vergelijkt de waardering met de testreferentie van de test. Wijkt de
       waardering af of ontbreekt de testreferentie, dan faalt de test.
       Bijwerken kan alleen met `task genereer-test-output`.

    Het is een fixture omdat de testreferentie de naam, de docstring en de
    waarschuwingen van de test nodig heeft; die geeft pytest via `request` en
    `recwarn`.
    """
    aangeroepen = False

    def _vergelijk(
        eenheid: EenhedenEenheid,
        groep: WoningwaarderingResultatenWoningwaarderingGroep,
        waarschuwingen: Iterable[WarningMessage] = (),
    ) -> None:
        # Een test heeft één testreferentie; een tweede aanroep zou de eerste
        # overschrijven.
        nonlocal aangeroepen
        assert (
            not aangeroepen
        ), "Roep vergelijk_met_testreferentie één keer per test aan."
        aangeroepen = True
        waarschuwingen = list(waarschuwingen)

        assert_geen_onverwachte_waarschuwingen(recwarn, waarschuwingen)
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
