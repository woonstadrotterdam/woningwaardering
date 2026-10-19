from woningwaardering import Woningwaardering
from woningwaardering.vera.bvg.generated import (
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
