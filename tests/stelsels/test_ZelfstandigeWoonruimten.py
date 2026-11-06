"""Modellen op stelselniveau, zelfstandige woonruimten.

Zie docs/voor-ontwikkelaars/testing.md onder "Model op stelselniveau".
"""

import warnings
from pathlib import Path

import pytest

from tests.testreferenties import MAP
from tests.utils import lees_model
from woningwaardering.stelsels.zelfstandige_woonruimten import PuntenVoorDeWozWaarde
from woningwaardering.stelsels.zelfstandige_woonruimten.zelfstandige_woonruimten import (
    ZelfstandigeWoonruimten,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep

MODELLEN_MAP = Path(__file__).parent / "modellen/zelfstandige_woonruimten"
MODELLEN = sorted(MODELLEN_MAP.glob("*.json"))


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


def test_het_nieuwbouwminimum_is_in_het_hele_stelsel_gelijk_aan_dat_van_de_losse_stelselgroep(
    peildatum,
):
    """Het hele stelsel en de losse stelselgroep punten voor de WOZ-waarde kennen dezelfde punten voor de WOZ-waarde toe, ook als de woning de 110 punten voor het nieuwbouwminimum alleen met rubriek 12 haalt.

    Bron:
    - implementatietoelichting zelfstandige woonruimten, 2.11.5
    - wettekst, Bijlage I onder A, onderdeel 11.2
    """
    # Een zorgwoning uit 2017 met 87 punten voor de rubrieken 1 tot en met 10:
    # alleen met de verhoging van rubriek 12 haalt ze 110 punten.
    eenheid, _ = lees_model(
        MODELLEN_MAP / "zorgwoning_2017_haalt_110_punten_met_rubriek_12.json"
    )

    resultaat = ZelfstandigeWoonruimten(peildatum=peildatum).waardeer(
        eenheid.model_copy(deep=True)
    )
    woz_in_stelsel = next(
        groep
        for groep in resultaat.groepen or []
        if groep.criterium_groep
        and groep.criterium_groep.stelselgroep
        == Woningwaarderingstelselgroep.punten_voor_de_woz_waarde
    )
    losse_woz = PuntenVoorDeWozWaarde(peildatum=peildatum).waardeer(
        eenheid.model_copy(deep=True)
    )

    assert woz_in_stelsel.punten == losse_woz.punten == 40.0


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
