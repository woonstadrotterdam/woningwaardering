from datetime import date
from pathlib import Path

import pytest

from tests.test_utils import (
    assert_output_model,
    krijg_warning_tuple_op_datum,
    laad_specifiek_input_en_output_model,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.gemeenschappelijke_parkeerruimten import (
    GemeenschappelijkeParkeerruimten,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata.woningwaarderingstelselgroep import (
    Woningwaarderingstelselgroep,
)

# Get the absolute path to the current file
current_file_path = Path(__file__).absolute().parent


@pytest.fixture(params=[str(p) for p in (current_file_path / "output").rglob("*.json")])
def specifieke_input_en_output_model(request):
    output_file_path = request.param
    return laad_specifiek_input_en_output_model(
        current_file_path, Path(output_file_path)
    )


def test_GemeenschappelijkeParkeerruimten(
    zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat, peildatum
):
    gemeenschappelijke_parkeerruimten = GemeenschappelijkeParkeerruimten(
        peildatum=peildatum
    )
    resultaat = gemeenschappelijke_parkeerruimten.bereken(
        zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat
    )
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep)


def test_GemeenschappelijkeParkeerruimten_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    eenheid_input, eenheid_output = zelfstandige_woonruimten_input_en_outputmodel
    gemeenschappelijke_parkeerruimten = GemeenschappelijkeParkeerruimten(
        peildatum=peildatum
    )

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [gemeenschappelijke_parkeerruimten.bereken(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten,
    )


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_GemeenschappelijkeParkeerruimten_specifiek_output(
    specifieke_input_en_output_model, peildatum
):
    eenheid_input, eenheid_output = specifieke_input_en_output_model
    gemeenschappelijke_parkeerruimten = GemeenschappelijkeParkeerruimten(
        peildatum=peildatum
    )
    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [gemeenschappelijke_parkeerruimten.bereken(eenheid_input)]
    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten,
    )


# mapping eenheid_id naar peildatum-warning
specifiek_warning_mapping = {
    # let op: dit is de eenheid_id in de input json
    "warning_gedeeld_met_aantal_eenheden": [
        (
            date(2024, 7, 1),
            (
                UserWarning,
                "gedeeld_met_aantal_eenheden",
            ),
        )
    ],
    # let op: dit is de eenheid_id in de input json
    "warning_geen_oppervlakte": [
        (
            date(2024, 7, 1),
            (
                UserWarning,
                "oppervlakte",
            ),
        )
    ],
}


# In deze test data zit expres missende data
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_Gemeenschappelijke_parkeerruimte_specifiek_warnings(
    specifieke_input_en_output_model, peildatum
):
    eenheid_input, x = specifieke_input_en_output_model
    gemeenschappelijke_parkeerruimte = GemeenschappelijkeParkeerruimten(
        peildatum=peildatum
    )
    warning_tuple = krijg_warning_tuple_op_datum(
        eenheid_input.id, peildatum, specifiek_warning_mapping
    )
    if warning_tuple is not None:
        with pytest.warns(warning_tuple[0], match=warning_tuple[1]):
            gemeenschappelijke_parkeerruimte.bereken(eenheid_input)
