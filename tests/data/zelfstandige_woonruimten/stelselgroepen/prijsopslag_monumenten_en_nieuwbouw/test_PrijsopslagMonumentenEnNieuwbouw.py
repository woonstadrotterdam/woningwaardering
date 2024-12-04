from pathlib import Path

import pytest

from tests.utils import (
    assert_output_model,
    assert_stelselgroep_output_in_eenheid_output,
    laad_specifiek_input_en_output_model,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.prijsopslag_monumenten_en_nieuwbouw import (
    PrijsopslagMonumentenEnNieuwbouw,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep


def test_PrijsopslagMonumentenEnNieuwbouw_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output_in_eenheid_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        PrijsopslagMonumentenEnNieuwbouw,
    )


current_file_path = Path(__file__).absolute().parent


@pytest.fixture(params=[str(p) for p in (current_file_path / "output").rglob("*.json")])
def specifieke_input_en_output_model(request):
    output_file_path = request.param
    return laad_specifiek_input_en_output_model(
        current_file_path, Path(output_file_path)
    )


# In deze test data zit expres missende data
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_PrijsopslagMonumentenEnNieuwbouw_specifiek_output(
    specifieke_input_en_output_model, peildatum
):
    eenheid_input, eenheid_output = specifieke_input_en_output_model
    prijsopslag_monumenten_en_nieuwbouw = PrijsopslagMonumentenEnNieuwbouw(
        peildatum=peildatum
    )
    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [prijsopslag_monumenten_en_nieuwbouw.waardeer(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.prijsopslag_monumenten_en_nieuwbouw,
    )


# mapping eenheid_id naar peildatum-warning
specifiek_warning_mapping = {
    "beschermd_stadsgezicht_zonder_bouwjaar": (
        UserWarning,
        "geen bouwjaar",
    ),
    "monumenten_none": (
        UserWarning,
        "'monumenten' is niet gespecificeerd. Indien de eenheid geen monumentstatus heeft, geef dit dan expliciet aan door een lege lijst toe te wijzen aan het 'monumenten'-attribuut.",
    ),
    "rijksmonument_zonder_datum_afsluiten_huurovereenkomst": (
        UserWarning,
        "'datum_afsluiten_huurovereenkomst' is niet gespecificeerd voor dit rijksmonument.",
    ),
}


# In deze test data zit expres missende data
@pytest.mark.filterwarnings("ignore::UserWarning")
def test_PrijsopslagMonumentenEnNieuwbouw_specifiek_warnings(
    specifieke_input_en_output_model, peildatum
):
    eenheid_input, _ = specifieke_input_en_output_model
    warning_tuple = specifiek_warning_mapping.get(eenheid_input.id)

    if warning_tuple is not None:
        with pytest.warns(warning_tuple[0], match=warning_tuple[1]):
            prijsopslag_monumenten_en_nieuwbouw = PrijsopslagMonumentenEnNieuwbouw(
                peildatum=peildatum
            )
            prijsopslag_monumenten_en_nieuwbouw.waardeer(eenheid_input)
