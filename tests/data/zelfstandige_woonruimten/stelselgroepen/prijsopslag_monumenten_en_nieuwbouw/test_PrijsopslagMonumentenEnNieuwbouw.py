from pathlib import Path

import pytest

from tests.test_utils import assert_output_model, laad_specifiek_input_en_output_model
from woningwaardering.stelsels.zelfstandige_woonruimten.prijsopslag_monumenten_en_nieuwbouw import (
    PrijsopslagMonumentenEnNieuwbouw,
)

from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingGroep,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep


def test_PrijsopslagMonumentenEnNieuwbouw(
    zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat
):
    prijsopslag_monumenten_en_nieuwbouw = PrijsopslagMonumentenEnNieuwbouw()
    resultaat = prijsopslag_monumenten_en_nieuwbouw.bereken(
        zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat
    )
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep)


def test_PrijsopslagMonumentenEnNieuwbouw_output(
    zelfstandige_woonruimten_input_en_outputmodel,
):
    eenheid_input, eenheid_output, peildatum = (
        zelfstandige_woonruimten_input_en_outputmodel
    )
    prijsopslag_monumenten_en_nieuwbouw = PrijsopslagMonumentenEnNieuwbouw(
        peildatum=peildatum
    )
    resultaat = prijsopslag_monumenten_en_nieuwbouw.bereken(eenheid_input)

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.prijsopslag_monumenten_en_nieuwbouw,
    )


# Get the absolute path to the current file
current_file_path = Path(__file__).absolute().parent


@pytest.fixture(params=[str(p) for p in (current_file_path / "output").rglob("*.json")])
def specifieke_input_en_output_model(request):
    output_file_path = request.param
    return laad_specifiek_input_en_output_model(
        current_file_path, Path(output_file_path)
    )


def test_PrijsopslagMonumentenEnNieuwbouw_specifiek_output(
    specifieke_input_en_output_model,
):
    eenheid_input, eenheid_output, peildatum = specifieke_input_en_output_model
    prijsopslag_monumenten_en_nieuwbouw = PrijsopslagMonumentenEnNieuwbouw(
        peildatum=peildatum
    )
    resultaat = prijsopslag_monumenten_en_nieuwbouw.bereken(eenheid_input)

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.prijsopslag_monumenten_en_nieuwbouw,
    )
