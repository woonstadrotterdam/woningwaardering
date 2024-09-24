from datetime import date
from pathlib import Path

import pytest

from tests.test_utils import (
    assert_output_model,
    krijg_warning_tuple_op_datum,
    laad_specifiek_input_en_output_model,
)
from woningwaardering.stelsels.utils import normaliseer_ruimte_namen
from woningwaardering.stelsels.zelfstandige_woonruimten.keuken import (
    Keuken,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
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


def test_Keuken(
    zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat, peildatum
):
    keuken = Keuken(peildatum=peildatum)
    resultaat = keuken.bereken(
        zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat
    )
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep)


def test_Keuken_output(zelfstandige_woonruimten_input_en_outputmodel, peildatum):
    eenheid_input, eenheid_output = zelfstandige_woonruimten_input_en_outputmodel

    normaliseer_ruimte_namen(eenheid_input)

    keuken = Keuken(peildatum=peildatum)

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [keuken.bereken(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.keuken,
    )


# In deze test data zit expres missende data
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_Keuken_specifiek_output(specifieke_input_en_output_model, peildatum):
    eenheid_input, eenheid_output = specifieke_input_en_output_model
    keuken = Keuken(peildatum=peildatum)
    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [keuken.bereken(eenheid_input)]
    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.keuken,
    )


# mapping eenheid_id naar peildatum-warning
specifiek_warning_mapping = {
    # let op: dit is de eenheid_id in de input json
    "aanrecht_zonder_lengte": [
        (
            date(2024, 7, 1),
            (
                UserWarning,
                "geen aanrecht",
            ),
        )
    ],
    # let op: dit is de eenheid_id in de input json
    "keuken_zonder_aanrecht": [
        (
            date(2024, 7, 1),
            (
                UserWarning,
                "geen aanrecht",
            ),
        )
    ],
}


# In deze test data zit expres missende data
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_Keuken_specifiek_warnings(specifieke_input_en_output_model, peildatum):
    eenheid_input, _ = specifieke_input_en_output_model
    keuken = Keuken(peildatum=peildatum)
    warning_tuple = krijg_warning_tuple_op_datum(
        eenheid_input.id, peildatum, specifiek_warning_mapping
    )
    if warning_tuple is not None:
        with pytest.warns(warning_tuple[0], match=warning_tuple[1]):
            keuken.bereken(eenheid_input)
