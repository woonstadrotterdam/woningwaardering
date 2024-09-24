from pathlib import Path

import pytest

from tests.test_utils import assert_output_model, laad_specifiek_input_en_output_model
from woningwaardering.stelsels.utils import normaliseer_ruimte_namen
from woningwaardering.stelsels.zelfstandige_woonruimten.energieprestatie import (
    Energieprestatie,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep


def test_Energieprestatie(
    zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat, peildatum
):
    energieprestatie = Energieprestatie(peildatum=peildatum)
    resultaat = energieprestatie.bereken(
        zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat
    )
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep)


def test_Energieprestatie_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    eenheid_input, eenheid_output = zelfstandige_woonruimten_input_en_outputmodel

    normaliseer_ruimte_namen(eenheid_input)

    energieprestatie = Energieprestatie(peildatum=peildatum)
    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [energieprestatie.bereken(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.energieprestatie,
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
    resultaat.groepen = [energieprestatie.bereken(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.energieprestatie,
    )
