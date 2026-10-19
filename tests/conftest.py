from collections.abc import Callable, Iterable
from warnings import WarningMessage

import pytest

from tests.peildatum import REFERENTIE_PEILDATUM
from tests.testreferenties import (
    BIJWERKOPTIE,
    Uitkomst,
    assert_geen_onverwachte_waarschuwingen,
    maak_testreferentie,
    pad_van_testreferentie,
    vergelijk_of_werk_bij,
)
from tests.utils import assert_invarianten_van_groep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)


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
    """Geef de functie waarmee een waarderingstest of een modeltest afsluit.

    De uitkomst is een stelselgroep (waarderingstest) of het hele stelsel (model op
    stelselniveau, met de beschrijving van het model). De functie doet drie dingen,
    in deze volgorde:

    1. Ze faalt bij een `UserWarning` die de test niet heeft meegegeven.
    2. Ze controleert de invarianten die voor elke gewaardeerde stelselgroep
       gelden, zie `assert_invarianten_van_groep`.
    3. Ze vergelijkt de uitkomst met de testreferentie van de test. Wijkt de
       uitkomst af of ontbreekt de testreferentie, dan faalt de test.
       Bijwerken kan alleen met `task genereer-test-output`.

    Het is een fixture omdat de testreferentie de naam, de docstring en de
    waarschuwingen van de test nodig heeft; die geeft pytest via `request` en
    `recwarn`.
    """
    aangeroepen = False

    def _vergelijk(
        eenheid: EenhedenEenheid,
        uitkomst: Uitkomst,
        waarschuwingen: Iterable[WarningMessage] = (),
        beschrijving: str | None = None,
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
        groepen = (
            uitkomst.groepen or []
            if isinstance(uitkomst, WoningwaarderingResultatenWoningwaarderingResultaat)
            else [uitkomst]
        )
        for groep in groepen:
            assert_invarianten_van_groep(groep)
        vergelijk_of_werk_bij(
            pad_van_testreferentie(request.node),
            maak_testreferentie(
                request.node, eenheid, uitkomst, waarschuwingen, beschrijving
            ),
            bijwerken=request.config.getoption(BIJWERKOPTIE),
        )

    return _vergelijk


@pytest.fixture()
def woningwaardering_resultaat():
    return WoningwaarderingResultatenWoningwaarderingResultaat()
