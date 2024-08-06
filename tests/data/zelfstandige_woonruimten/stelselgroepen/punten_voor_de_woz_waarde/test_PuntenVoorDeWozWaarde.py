from datetime import date
from pathlib import Path

import pytest
from tests.test_utils import (
    assert_output_model,
    krijg_warning_tuple_op_datum,
    laad_specifiek_input_en_output_model,
)

from woningwaardering.stelsels.zelfstandige_woonruimten import (
    PuntenVoorDeWozWaarde,
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


def test_PuntenVoorDeWozWaarde(
    zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat
):
    punten_voor_de_woz_waarde = PuntenVoorDeWozWaarde()
    resultaat = punten_voor_de_woz_waarde.bereken(
        zelfstandige_woonruimten_inputmodel, woningwaardering_resultaat
    )
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep)


def test_PuntenVoorDeWozWaarde_output(
    zelfstandige_woonruimten_input_en_outputmodel,
):
    eenheid_input, eenheid_output, peildatum = (
        zelfstandige_woonruimten_input_en_outputmodel
    )
    punten_voor_de_woz_waarde = PuntenVoorDeWozWaarde(peildatum=peildatum)
    resultaat = punten_voor_de_woz_waarde.bereken(eenheid_input)

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.punten_voor_de_woz_waarde,
    )


# In deze test data zit expres missende data
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_PuntenVoorDeWozWaarde_specifiek_output(specifieke_input_en_output_model):
    eenheid_input, eenheid_output, peildatum = specifieke_input_en_output_model
    punten_voor_de_woz_waarde = PuntenVoorDeWozWaarde(peildatum=peildatum)
    resultaat = punten_voor_de_woz_waarde.bereken(eenheid_input)

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.punten_voor_de_woz_waarde,
    )


# mapping eenheid_id naar peildatum-warning
specifiek_warning_mapping = {
    "geen_woz": [
        (
            date(2024, 1, 1),
            (
                UserWarning,
                "geen WOZ-waarde",
            ),
        )
    ],
}


def test_PuntenVoorDeWozWaarde_specifiek_warnings(specifieke_input_en_output_model):
    eenheid_input, _, peildatum = specifieke_input_en_output_model
    woz = PuntenVoorDeWozWaarde(peildatum=peildatum)
    warning_tuple = krijg_warning_tuple_op_datum(
        eenheid_input.id, peildatum, specifiek_warning_mapping
    )
    if warning_tuple is not None:
        with pytest.warns(warning_tuple[0], match=warning_tuple[1]):
            woz.bereken(eenheid_input)
