from pathlib import Path

import pytest

from tests.utils import (
    assert_output_model,
    assert_stelselgroep_output_in_eenheid_output,
    laad_specifiek_input_en_output_model,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten.gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen import (
    GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata.woningwaarderingstelselgroep import (
    Woningwaarderingstelselgroep,
)


def test_GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output_in_eenheid_output(
        onzelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen,
    )


# Get the absolute path to the current file
current_file_path = Path(__file__).absolute().parent


@pytest.fixture(params=[str(p) for p in (current_file_path / "output").rglob("*.json")])
def specifieke_input_en_output_model(request):
    output_file_path = request.param
    return laad_specifiek_input_en_output_model(
        current_file_path, Path(output_file_path)
    )


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen_specifiek_output(
    specifieke_input_en_output_model, peildatum
):
    eenheid_input, eenheid_output = specifieke_input_en_output_model
    gemeenschappelijke_binnenruimten = (
        GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen(peildatum=peildatum)
    )
    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [gemeenschappelijke_binnenruimten.waardeer(eenheid_input)]
    assert_output_model(
        resultaat,
        eenheid_output,
        Woningwaarderingstelselgroep.gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen,
    )
