from pathlib import Path

import pytest
from tests.test_utils import assert_output_model, laad_specifiek_input_en_output_model

from woningwaardering.stelsels.zelfstandige_woonruimten.oppervlakte_van_vertrekken import (
    OppervlakteVanVertrekken,
)

from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingGroep,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep


def test_OppervlakteVanVertrekken(
    zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat
):
    oppervlakte_van_vertrekken = OppervlakteVanVertrekken()
    resultaat = oppervlakte_van_vertrekken.bereken(
        zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat
    )
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep)


def test_OppervlakteVanVertrekken_output(
    zelfstandige_woonruimten_input_en_outputmodel,
):
    eenheid_input, eenheid_output, peildatum = (
        zelfstandige_woonruimten_input_en_outputmodel
    )
    oppervlakte_van_vertrekken = OppervlakteVanVertrekken(peildatum=peildatum)
    resultaat = oppervlakte_van_vertrekken.bereken(eenheid_input)

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.oppervlakte_van_vertrekken,
    )


# Get the absolute path to the current file
current_file_path = Path(__file__).absolute().parent


@pytest.fixture(params=[str(p) for p in (current_file_path / "output").rglob("*.json")])
def specifieke_input_en_output_model(request):
    output_file_path = request.param
    return laad_specifiek_input_en_output_model(
        current_file_path, Path(output_file_path)
    )


def test_OppervlakteVanVertrekken_specifiek_output(
    specifieke_input_en_output_model,
):
    eenheid_input, eenheid_output, peildatum = specifieke_input_en_output_model
    oppervlakte_van_vertrekken = OppervlakteVanVertrekken(peildatum=peildatum)
    resultaat = oppervlakte_van_vertrekken.bereken(eenheid_input)

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.oppervlakte_van_vertrekken,
    )
