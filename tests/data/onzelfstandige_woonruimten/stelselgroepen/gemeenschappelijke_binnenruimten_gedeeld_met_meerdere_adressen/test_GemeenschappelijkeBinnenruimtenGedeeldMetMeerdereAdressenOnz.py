from pathlib import Path

import pytest

from tests.utils import (
    assert_stelselgroep_output,
    assert_stelselgroep_specifiek_output,
    maak_specifieke_input_en_output_model_fixture,
)
from woningwaardering.stelsels.onzelfstandige_woonruimten.gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen import (
    GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen,
)


def test_GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen_output(
    onzelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        onzelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen,
    )


specifieke_input_en_output_model = maak_specifieke_input_en_output_model_fixture(
    Path(__file__).parent
)


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen_specifiek_output(
    specifieke_input_en_output_model, peildatum
):
    assert_stelselgroep_specifiek_output(
        specifieke_input_en_output_model,
        peildatum,
        GemeenschappelijkeBinnenruimtenGedeeldMetMeerdereAdressen,
    )
