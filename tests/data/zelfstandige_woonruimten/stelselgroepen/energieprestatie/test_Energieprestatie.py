from pathlib import Path

import pytest

from tests.utils import (
    assert_output_model,
    assert_stelselgroep_output_in_eenheid_output,
    laad_specifiek_input_en_output_model,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.energieprestatie import (
    Energieprestatie,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep


def test_Energieprestatie_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output_in_eenheid_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        Energieprestatie,
    )


# Get the absolute path to the current file
current_file_path = Path(__file__).absolute().parent


@pytest.fixture(params=[str(p) for p in (current_file_path / "output").rglob("*.json")])
def specifieke_input_en_output_model(request):
    output_file_path = request.param
    return laad_specifiek_input_en_output_model(
        current_file_path, Path(output_file_path)
    )


def test_Energieprestatie_specifiek_output(specifieke_input_en_output_model, peildatum):
    eenheid_input, eenheid_output = specifieke_input_en_output_model
    energieprestatie = Energieprestatie(peildatum=peildatum)
    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [energieprestatie.waardeer(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.energieprestatie,
    )
