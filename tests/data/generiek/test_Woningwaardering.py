import pytest

from woningwaardering import Woningwaardering
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelsel


def test_WoningwaarderingGeneriekOnzelfstandigeWoonruimte(
    onzelfstandige_woonruimten_inputmodel, peildatum
):
    woningwaardering = Woningwaardering(peildatum=peildatum)
    resultaat = woningwaardering.waardeer(onzelfstandige_woonruimten_inputmodel)

    assert isinstance(
        resultaat, WoningwaarderingResultatenWoningwaarderingResultaat
    ), f"Resultaat is geen instance van WoningwaarderingResultatenWoningwaarderingResultaat, {type(resultaat) = }"
    assert resultaat.punten is not None
    assert all(
        groepresultaat.criterium_groep.stelsel
        == Woningwaarderingstelsel.onzelfstandige_woonruimten
        for groepresultaat in resultaat.groepen
    )


def test_WoningwaarderingGeneriekZelfstandigeWoonruimte(
    zelfstandige_woonruimten_inputmodel, peildatum
):
    woningwaardering = Woningwaardering(peildatum=peildatum)
    resultaat = woningwaardering.waardeer(zelfstandige_woonruimten_inputmodel)

    assert isinstance(
        resultaat, WoningwaarderingResultatenWoningwaarderingResultaat
    ), f"Resultaat is geen instance van WoningwaarderingResultatenWoningwaarderingResultaat, {type(resultaat) = }"
    assert resultaat.punten is not None
    assert all(
        groepresultaat.criterium_groep.stelsel
        == Woningwaarderingstelsel.zelfstandige_woonruimten
        for groepresultaat in resultaat.groepen
    )


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
