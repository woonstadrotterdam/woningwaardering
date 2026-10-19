"""Modellen op stelselniveau, zelfstandige woonruimten.

Zie docs/voor-ontwikkelaars/testing.md onder "Model op stelselniveau".
"""

import warnings
from pathlib import Path

import pytest

from tests.testreferenties import MAP
from tests.utils import lees_model
from woningwaardering.stelsels.zelfstandige_woonruimten.zelfstandige_woonruimten import (
    ZelfstandigeWoonruimten,
)

MODELLEN = sorted(
    (Path(__file__).parent / "modellen/zelfstandige_woonruimten").glob("*.json")
)


@pytest.mark.parametrize("pad", [pytest.param(pad, id=pad.stem) for pad in MODELLEN])
def test_model_zelfstandige_woonruimten(pad, peildatum, vergelijk_met_testreferentie):
    """Het stelsel zelfstandige woonruimten waardeert het model zoals de testreferentie het vastlegt."""
    eenheid, beschrijving = lees_model(pad)

    # Alle waarschuwingen van het model komen in de testreferentie.
    with warnings.catch_warnings(record=True) as opgevangen:
        warnings.simplefilter("always", UserWarning)
        # De kopie houdt de input in de testreferentie zoals het model hem geeft.
        resultaat = ZelfstandigeWoonruimten(peildatum=peildatum).waardeer(
            eenheid.model_copy(deep=True)
        )
    waarschuwingen = [w for w in opgevangen if issubclass(w.category, UserWarning)]

    vergelijk_met_testreferentie(
        eenheid, resultaat, waarschuwingen, beschrijving=beschrijving
    )


def test_bij_elke_testreferentie_van_een_model_hoort_een_model():
    """Bij elke testreferentie van een model hoort een model.

    Is een model bewust verwijderd of hernoemd, verwijder dan ook zijn testreferentie.
    """
    verwacht = {
        f"test_model_zelfstandige_woonruimten[{pad.stem}].md" for pad in MODELLEN
    }
    testreferenties = (Path(__file__).parent / MAP).glob(
        "test_model_zelfstandige_woonruimten[[]*].md"
    )
    assert sorted(pad.name for pad in testreferenties if pad.name not in verwacht) == []
