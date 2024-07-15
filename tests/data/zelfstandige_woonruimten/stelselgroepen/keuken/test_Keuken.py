from pathlib import Path

import pytest
from tests.test_utils import assert_output_model, laad_specifiek_input_en_output_model

from woningwaardering.stelsels.zelfstandige_woonruimten.keuken import (
    Keuken,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingGroep,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep

# Get the absolute path to the current file
current_file_path = Path(__file__).absolute().parent


@pytest.fixture(params=[str(p) for p in (current_file_path / "output").rglob("*.json")])
def specifieke_input_en_output_model(request):
    output_file_path = request.param
    return laad_specifiek_input_en_output_model(
        current_file_path, Path(output_file_path)
    )


def test_Keuken(zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat):
    keuken = Keuken()
    resultaat = keuken.bereken(
        zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat
    )
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep)


def test_Keuken_output(
    zelfstandige_woonruimten_input_en_outputmodel,
):
    eenheid_input, eenheid_output, peildatum = (
        zelfstandige_woonruimten_input_en_outputmodel
    )
    keuken = Keuken(peildatum=peildatum)
    resultaat = keuken.bereken(eenheid_input)

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.keuken,
    )


# In deze test data zit expres missende data
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_Keuken_specifiek_output(specifieke_input_en_output_model):
    eenheid_input, eenheid_output, peildatum = specifieke_input_en_output_model
    keuken = Keuken(peildatum=peildatum)
    resultaat = keuken.bereken(eenheid_input)
    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.keuken,
    )


specifiek_warning_mapping = {
    "aanrecht_zonder_lengte": (
        UserWarning,
        "Aanrecht aanrecht_1 in ruimte keuken heeft geen lengte",
    ),
    "keuken_zonder_aanrecht": (UserWarning, "keuken zonder aanrecht"),
}


def test_Keuken_specifiek_warnings(specifieke_input_en_output_model):
    eenheid_input, _, peildatum = specifieke_input_en_output_model
    keuken = Keuken(peildatum=peildatum)
    warning_tuple = specifiek_warning_mapping.get(eenheid_input.id)
    # keuken.bereken(eenheid_input)
    if warning_tuple is not None:
        with pytest.warns(warning_tuple[0], match=warning_tuple[1]):
            keuken.bereken(eenheid_input)
