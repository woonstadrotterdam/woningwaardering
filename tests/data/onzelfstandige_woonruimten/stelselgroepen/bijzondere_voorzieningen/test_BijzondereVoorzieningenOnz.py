from pathlib import Path

import pytest

from tests.utils import assert_output_model, laad_specifiek_input_en_output_model
from woningwaardering.stelsels.onzelfstandige_woonruimten import (
    BijzondereVoorzieningen,
)
from woningwaardering.stelsels.utils import normaliseer_ruimte_namen
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep


def test_BijzondereVoorzieningenZorgwoning(
    onzelfstandige_woonruimten_inputmodel, woningwaardering_resultaat, peildatum
):
    bijzondere_voorzieningen = BijzondereVoorzieningen(peildatum=peildatum)
    resultaat = bijzondere_voorzieningen.bereken(
        onzelfstandige_woonruimten_inputmodel, woningwaardering_resultaat
    )
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep)


def test_BijzondereVoorzieningenZorgwoning_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    eenheid_input, eenheid_output = onzelfstandige_woonruimten_input_en_outputmodel

    normaliseer_ruimte_namen(eenheid_input)

    bijzondere_voorzieningen = BijzondereVoorzieningen(peildatum=peildatum)

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [bijzondere_voorzieningen.bereken(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.bijzondere_voorzieningen,
    )


# Get the absolute path to the current file
current_file_path = Path(__file__).absolute().parent


@pytest.fixture(params=[str(p) for p in (current_file_path / "output").rglob("*.json")])
def specifieke_input_en_output_model(request):
    output_file_path = request.param
    return laad_specifiek_input_en_output_model(
        current_file_path, Path(output_file_path)
    )


def test_BijzondereVoorzieningenZorgwoning_specifiek_output(
    specifieke_input_en_output_model, peildatum
):
    eenheid_input, eenheid_output = specifieke_input_en_output_model
    bijzondere_voorzieningen = BijzondereVoorzieningen(peildatum=peildatum)

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [bijzondere_voorzieningen.bereken(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.bijzondere_voorzieningen,
    )
