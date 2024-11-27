from datetime import date
from pathlib import Path

import pytest

from tests.utils import (
    assert_output_model,
    krijg_warning_tuple_op_datum,
    laad_specifiek_input_en_output_model,
)
from woningwaardering.stelsels.utils import normaliseer_ruimte_namen
from woningwaardering.stelsels.zelfstandige_woonruimten import (
    Sanitair,
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


def test_Sanitair(
    zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat, peildatum
):
    sanitair = Sanitair(peildatum=peildatum)
    resultaat = sanitair.waardeer(
        zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat
    )
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep)


def test_Sanitair_output(zelfstandige_woonruimten_input_en_outputmodel, peildatum):
    eenheid_input, eenheid_output = zelfstandige_woonruimten_input_en_outputmodel

    normaliseer_ruimte_namen(eenheid_input)

    sanitair = Sanitair(peildatum=peildatum)

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [sanitair.waardeer(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.sanitair,
    )


def test_Sanitair_specifiek_output(specifieke_input_en_output_model, peildatum):
    eenheid_input, eenheid_output = specifieke_input_en_output_model
    sanitair = Sanitair(peildatum=peildatum)

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [sanitair.waardeer(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.sanitair,
    )


# mapping eenheid_id naar peildatum-warning
specifiek_warning_mapping = {
    "ingebouwd_kastje_met_wastafel_zonder_wastafel": [
        (
            date(2024, 7, 1),
            (
                UserWarning,
                "wastafel",
            ),
        )
    ],
}


def test_Sanitair_specifiek_warnings(specifieke_input_en_output_model, peildatum):
    eenheid_input, _ = specifieke_input_en_output_model

    warning_tuple = krijg_warning_tuple_op_datum(
        eenheid_input.id, peildatum, specifiek_warning_mapping
    )
    if warning_tuple is not None:
        sanitair = Sanitair(peildatum=peildatum)
        with pytest.warns(warning_tuple[0], match=warning_tuple[1]):
            sanitair.waardeer(eenheid_input)
