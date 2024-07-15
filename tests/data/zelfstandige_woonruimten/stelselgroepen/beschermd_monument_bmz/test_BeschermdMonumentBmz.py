from pathlib import Path

import pytest

from tests.test_utils import assert_output_model, laad_specifiek_input_en_output_model
from woningwaardering.stelsels.zelfstandige_woonruimten.beschermd_monument_bmz import (
    BeschermdMonumentBmz,
)

from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep


# def test_BeschermdMonumentBmz(
#     zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat
# ):
#     beschermd_monument_bmz = BeschermdMonumentBmz()
#     resultaat = beschermd_monument_bmz.bereken(
#         zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat
#     )
#     assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep)


# def test_BeschermdMonumentBmz_output(
#     zelfstandige_woonruimten_input_en_outputmodel,
# ):
#     eenheid_input, eenheid_output, peildatum = (
#         zelfstandige_woonruimten_input_en_outputmodel
#     )
#     beschermd_monument_bmz = BeschermdMonumentBmz(peildatum=peildatum)
#     resultaat = beschermd_monument_bmz.bereken(eenheid_input)

#     assert_output_model(
#         resultaat,
#         eenheid_output,
#         Woningwaarderingstelselgroep.beschermd_monument_bmz,
#     )


# Get the absolute path to the current file
current_file_path = Path(__file__).absolute().parent


@pytest.fixture(params=[str(p) for p in (current_file_path / "output").rglob("*.json")])
def specifieke_input_en_output_model(request):
    output_file_path = request.param
    return laad_specifiek_input_en_output_model(
        current_file_path, Path(output_file_path)
    )


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_BeschermdMonumentBmz_specifiek_output(
    specifieke_input_en_output_model,
):
    eenheid_input, eenheid_output, peildatum = specifieke_input_en_output_model
    beschermd_monument_bmz = BeschermdMonumentBmz(peildatum=peildatum)
    resultaat = beschermd_monument_bmz.bereken(eenheid_input)

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.beschermd_monument_bmz,
    )


specifiek_warning_mapping = {
    "missend_rijksmonument": (
        UserWarning,
        "Monumenten is None",
    )
}


def test_BeschermdMonumentBmz_specifiek_warnings(specifieke_input_en_output_model):
    eenheid_input, _, peildatum = specifieke_input_en_output_model
    woz = BeschermdMonumentBmz(peildatum=peildatum)
    warning_tuple = specifiek_warning_mapping.get(eenheid_input.id)
    if warning_tuple is not None:
        with pytest.warns(warning_tuple[0], match=warning_tuple[1]):
            woz.bereken(eenheid_input)
