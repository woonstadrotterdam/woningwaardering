from pathlib import Path

import pytest

from woningwaardering import Woningwaardering
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelsel

MODELLEN = Path(__file__).parent / "stelsels/modellen"


@pytest.mark.parametrize(
    ("pad", "stelsel"),
    [
        pytest.param(
            pad, getattr(Woningwaarderingstelsel, stelselmap.name), id=pad.stem
        )
        for stelselmap in sorted(MODELLEN.iterdir())
        for pad in sorted(stelselmap.glob("*.json"))
    ],
)
def test_woningwaardering_waardeert_met_het_stelsel_van_de_eenheid(
    pad, stelsel, peildatum
):
    """Woningwaardering waardeert een eenheid met het stelsel dat de eenheid opgeeft."""
    eenheid = EenhedenEenheid.model_validate_json(pad.read_text())

    resultaat = Woningwaardering(peildatum=peildatum).waardeer(eenheid)

    assert {groep.criterium_groep.stelsel for groep in resultaat.groepen or []} == {
        stelsel
    }


def test_eenheid_zonder_woningwaarderingstelsel_geeft_een_fout(peildatum):
    """Zonder woningwaarderingstelsel kan Woningwaardering geen stelsel kiezen."""
    with pytest.raises(ValueError, match="woningwaarderingstelsel-attribuut ontbreekt"):
        Woningwaardering(peildatum=peildatum).waardeer(EenhedenEenheid(id="eenheid"))


def test_eenheid_met_een_ongeldig_woningwaarderingstelsel_geeft_een_fout(peildatum):
    """Een ander woningwaarderingstelsel dan zelfstandig of onzelfstandig geeft een fout."""
    eenheid = EenhedenEenheid(
        id="eenheid",
        woningwaarderingstelsel=Woningwaarderingstelsel.zelfstandige_woonruimten.model_copy(
            update={"code": "ONB", "naam": "Onbekend"}
        ),
    )

    with pytest.raises(ValueError, match="ongeldig woningwaarderingsstelsel-attribuut"):
        Woningwaardering(peildatum=peildatum).waardeer(eenheid)
