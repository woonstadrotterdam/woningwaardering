from datetime import date
from pathlib import Path

import pytest

from tests.utils import (
    WarningConfig,
    assert_stelselgroep_output,
    assert_stelselgroep_specifiek_output,
    assert_stelselgroep_warnings,
    maak_specifieke_input_en_output_model_fixture,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.prijsopslag_monumenten_en_nieuwbouw import (
    PrijsopslagMonumentenEnNieuwbouw,
)


def test_PrijsopslagMonumentenEnNieuwbouw_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        PrijsopslagMonumentenEnNieuwbouw,
    )


current_file_path = Path(__file__).absolute().parent
specifieke_input_en_output_model = maak_specifieke_input_en_output_model_fixture(
    current_file_path
)


@pytest.mark.filterwarnings("ignore::UserWarning")
def test_PrijsopslagMonumentenEnNieuwbouw_specifiek_output(
    specifieke_input_en_output_model, peildatum
):
    assert_stelselgroep_specifiek_output(
        specifieke_input_en_output_model,
        peildatum,
        PrijsopslagMonumentenEnNieuwbouw,
    )


warning_configs = [
    WarningConfig(
        file=f"{current_file_path}/input/beschermd_stadsgezicht_zonder_bouwjaar.json",
        peildatum=date(2025, 1, 1),
        warnings={
            UserWarning: "geen bouwjaar",
        },
    ),
    WarningConfig(
        file=f"{current_file_path}/input/monumenten_none.json",
        peildatum=date(2025, 1, 1),
        warnings={
            UserWarning: "'monumenten' is niet gespecificeerd. Indien de eenheid geen monumentstatus heeft, geef dit dan expliciet aan door een lege lijst toe te wijzen aan het 'monumenten'-attribuut.",
        },
    ),
    WarningConfig(
        file=f"{current_file_path}/input/rijksmonument_zonder_datum_afsluiting_huurovereenkomst.json",
        peildatum=date(2025, 1, 1),
        warnings={
            UserWarning: "'datum_afsluiten_huurovereenkomst' is niet gespecificeerd voor dit rijksmonument.",
        },
    ),
]


@pytest.mark.filterwarnings("ignore::UserWarning")
@pytest.mark.parametrize("warning_config", warning_configs)
def test_PrijsopslagMonumentenEnNieuwbouw_specifiek_warnings(warning_config, peildatum):
    assert_stelselgroep_warnings(
        warning_config, peildatum, PrijsopslagMonumentenEnNieuwbouw
    )
