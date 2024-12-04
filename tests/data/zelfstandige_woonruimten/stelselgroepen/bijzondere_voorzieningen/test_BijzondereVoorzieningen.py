from pathlib import Path

import pytest

from tests.utils import (
    assert_output_model,
    assert_stelselgroep_output_in_eenheid_output,
    laad_specifiek_input_en_output_model,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.bijzondere_voorzieningen import (
    BijzondereVoorzieningen,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep


def test_BijzondereVoorzieningen_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output_in_eenheid_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        BijzondereVoorzieningen,
    )


current_file_path = Path(__file__).absolute().parent


@pytest.fixture(params=[str(p) for p in (current_file_path / "output").rglob("*.json")])
def specifieke_input_en_output_model(request):
    output_file_path = request.param
    return laad_specifiek_input_en_output_model(
        current_file_path, Path(output_file_path)
    )


def test_BijzondereVoorzieningen_specifiek_output(
    specifieke_input_en_output_model, peildatum
):
    eenheid_input, eenheid_output = specifieke_input_en_output_model
    bijzondere_voorzieningen = BijzondereVoorzieningen(peildatum=peildatum)

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [bijzondere_voorzieningen.waardeer(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.bijzondere_voorzieningen,
    )
