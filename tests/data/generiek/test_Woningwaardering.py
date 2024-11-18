from datetime import date

from tests.test_utils import assert_output_model
from woningwaardering import Woningwaardering
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelsel


def test_WoningwaarderingGeneriekOnzelfstandigeWoonruimte(
    onzelfstandige_woonruimten_inputmodel,
):
    woningwaardering = Woningwaardering(peildatum=date(2024, 7, 1))
    resultaat = woningwaardering.bereken(onzelfstandige_woonruimten_inputmodel)

    assert isinstance(
        resultaat, WoningwaarderingResultatenWoningwaarderingResultaat
    ), f"Resultaat is geen instance van WoningwaarderingResultatenWoningwaarderingResultaat, {type(resultaat) = }"
    assert resultaat.punten is not None
    assert all(
        groepresultaat.criterium_groep.stelsel.code
        == Woningwaarderingstelsel.onzelfstandige_woonruimten.code
        for groepresultaat in resultaat.groepen
    )


def test_WoningwaarderingGeneriekOnzelfstandigeWoonruimte_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    eenheid_input, verwachte_output = onzelfstandige_woonruimten_input_en_outputmodel
    woningwaardering = Woningwaardering(peildatum=peildatum)
    resultaat = woningwaardering.bereken(eenheid_input)
    assert_output_model(resultaat, verwachte_output)


def test_WoningwaarderingGeneriekZelfstandigeWoonruimte(
    zelfstandige_woonruimten_inputmodel,
):
    woningwaardering = Woningwaardering(peildatum=date(2024, 7, 1))
    resultaat = woningwaardering.bereken(zelfstandige_woonruimten_inputmodel)

    assert isinstance(
        resultaat, WoningwaarderingResultatenWoningwaarderingResultaat
    ), f"Resultaat is geen instance van WoningwaarderingResultatenWoningwaarderingResultaat, {type(resultaat) = }"
    assert resultaat.punten is not None
    assert all(
        groepresultaat.criterium_groep.stelsel.code
        == Woningwaarderingstelsel.zelfstandige_woonruimten.code
        for groepresultaat in resultaat.groepen
    )


def test_WoningwaarderingGeneriekZelfstandigeWoonruimte_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    eenheid_input, verwachte_output = zelfstandige_woonruimten_input_en_outputmodel
    woningwaardering = Woningwaardering(peildatum=peildatum)
    resultaat = woningwaardering.bereken(eenheid_input)
    assert_output_model(resultaat, verwachte_output)
