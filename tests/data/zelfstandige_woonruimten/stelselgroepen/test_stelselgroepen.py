from datetime import date
from pathlib import Path
from typing import Iterator

import pytest

from tests.test_utils import (
    assert_output_model,
    krijg_warning_tuple_op_datum,
    laad_specifiek_input_en_output_model,
)
from woningwaardering.stelsels.utils import normaliseer_ruimte_namen
from woningwaardering.stelsels.zelfstandige_woonruimten import (
    BijzondereVoorzieningen,
    Buitenruimten,
    Energieprestatie,
    GemeenschappelijkeParkeerruimten,
    GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen,
    Keuken,
    OppervlakteVanOverigeRuimten,
    OppervlakteVanVertrekken,
    PrijsopslagMonumentenEnNieuwbouw,
    PuntenVoorDeWozWaarde,
    Sanitair,
    VerkoelingEnVerwarming,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "tests/data"

# Define a list of tuples containing the stelselgroep class, name, and corresponding enum
STELSELGROEPEN = [
    (
        OppervlakteVanVertrekken,
        "oppervlakte_van_vertrekken",
        Woningwaarderingstelselgroep.oppervlakte_van_vertrekken,
    ),
    (
        OppervlakteVanOverigeRuimten,
        "oppervlakte_van_overige_ruimten",
        Woningwaarderingstelselgroep.oppervlakte_van_overige_ruimten,
    ),
    (
        VerkoelingEnVerwarming,
        "verkoeling_en_verwarming",
        Woningwaarderingstelselgroep.verkoeling_en_verwarming,
    ),
    (
        Buitenruimten,
        "buitenruimten",
        Woningwaarderingstelselgroep.buitenruimten,
    ),
    (
        Energieprestatie,
        "energieprestatie",
        Woningwaarderingstelselgroep.energieprestatie,
    ),
    (
        Keuken,
        "keuken",
        Woningwaarderingstelselgroep.keuken,
    ),
    (
        Sanitair,
        "sanitair",
        Woningwaarderingstelselgroep.sanitair,
    ),
    (
        GemeenschappelijkeParkeerruimten,
        "gemeenschappelijke_parkeerruimten",
        Woningwaarderingstelselgroep.gemeenschappelijke_parkeerruimten,
    ),
    (
        GemeenschappelijkeVertrekkenOverigeRuimtenEnVoorzieningen,
        "gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen",
        Woningwaarderingstelselgroep.gemeenschappelijke_vertrekken_overige_ruimten_en_voorzieningen,
    ),
    (
        PuntenVoorDeWozWaarde,
        "punten_voor_de_woz_waarde",
        Woningwaarderingstelselgroep.punten_voor_de_woz_waarde,
    ),
    (
        BijzondereVoorzieningen,
        "bijzondere_voorzieningen",
        Woningwaarderingstelselgroep.bijzondere_voorzieningen,
    ),
    (
        PrijsopslagMonumentenEnNieuwbouw,
        "prijsopslag_monumenten_en_nieuwbouw",
        Woningwaarderingstelselgroep.prijsopslag_monumenten_en_nieuwbouw,
    ),
]


def get_specific_input_output_paths(stelselgroep_name):
    current_file_path = Path(__file__).absolute().parent
    stelselgroep_path = current_file_path / stelselgroep_name
    return [str(p) for p in (stelselgroep_path / "output").rglob("*.json")]


def load_specific_model(stelselgroep_name, output_file_path):
    current_file_path = Path(__file__).absolute().parent / stelselgroep_name
    return laad_specifiek_input_en_output_model(
        current_file_path, Path(output_file_path)
    )


@pytest.mark.filterwarnings("ignore::UserWarning")
@pytest.mark.parametrize(
    "stelselgroep_info, output_file_path",
    [
        (stelselgroep_info, output_file_path)
        for stelselgroep_info in STELSELGROEPEN
        for output_file_path in get_specific_input_output_paths(stelselgroep_info[1])
    ],
)
def test_stelselgroep_specifiek_output(
    stelselgroep_info,
    output_file_path,
    peildatum,
):
    StelselgroepClass, _, stelselgroep_enum = stelselgroep_info
    eenheid_input, eenheid_output = load_specific_model(
        stelselgroep_info[1], output_file_path
    )
    stelselgroep = StelselgroepClass(peildatum=peildatum)
    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [stelselgroep.bereken(eenheid_input)]
    assert_output_model(
        resultaat,
        eenheid_output,
        stelselgroep_enum,
    )


# Add specific warning tests if needed
specifiek_warning_mapping = {
    "keuken": {
        "aanrecht_zonder_lengte": [
            (
                date(2024, 7, 1),
                (
                    UserWarning,
                    "geen aanrecht",
                ),
            )
        ],
        "keuken_zonder_aanrecht": [
            (
                date(2024, 7, 1),
                (
                    UserWarning,
                    "geen aanrecht",
                ),
            )
        ],
    },
    "gemeenschappelijke_parkeerruimten": {
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
    },
    "prijsopslag_monumenten_en_nieuwbouw": {
        "beschermd_stadsgezicht_zonder_bouwjaar": [
            (
                date(2024, 7, 1),
                (
                    UserWarning,
                    "Eenheid beschermd_stadsgezicht_zonder_bouwjaar: 'bouwjaar' is niet gespecificeerd.",
                ),
            )
        ],
        "monumenten_none": [
            (
                date(2024, 7, 1),
                (
                    UserWarning,
                    "Eenheid monumenten_none: 'monumenten' is niet gespecificeerd. Indien de eenheid geen monumentstatus heeft, geef dit dan expliciet aan door een lege lijst toe te wijzen aan het 'monumenten'-attribuut.",
                ),
            )
        ],
        "rijksmonument_zonder_datum_afsluiten_huurovereenkomst": [
            (
                date(2024, 7, 1),
                (
                    UserWarning,
                    "Eenheid rijksmonument_zonder_datum_afsluiten_huurovereenkomst: 'datum_afsluiten_huurovereenkomst' is niet gespecificeerd voor dit rijksmonument.",
                ),
            )
        ],
    },
}


def zelfstandige_woonruimten_input_en_outputmodel() -> (
    Iterator[
        tuple[EenhedenEenheid, WoningwaarderingResultatenWoningwaarderingResultaat]
    ]
):
    for output_file_path in [
        str(p)
        for p in (DATA_DIR / "zelfstandige_woonruimten/output").rglob("*.json")
        if ".unverified" not in str(p)
    ]:
        file_name = Path(output_file_path).name
        input_file_path = DATA_DIR / "zelfstandige_woonruimten/input" / file_name

        # get input model
        with open(input_file_path, "r+") as f:
            eenheid_input = EenhedenEenheid.model_validate_json(f.read())

        # get output model
        with open(output_file_path, "r+") as f:
            eenheid_output = (
                WoningwaarderingResultatenWoningwaarderingResultaat.model_validate_json(
                    f.read()
                )
            )
        yield eenheid_input, eenheid_output


@pytest.mark.parametrize(
    "stelselgroep_info, zelfstandige_woonruimten_input_en_outputmodel",
    [
        (stelselgroep_info, (eenheid_input, eenheid_output))
        for stelselgroep_info in STELSELGROEPEN
        for eenheid_input, eenheid_output in zelfstandige_woonruimten_input_en_outputmodel()
    ],
)
def test_stelselgroepen(
    stelselgroep_info, zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    eenheid_input, _ = zelfstandige_woonruimten_input_en_outputmodel
    StelselgroepClass, _, _ = stelselgroep_info
    stelselgroep = StelselgroepClass(peildatum=peildatum)
    resultaat = stelselgroep.bereken(eenheid_input)
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep)


@pytest.mark.parametrize(
    "stelselgroep_info, zelfstandige_woonruimten_input_en_outputmodel",
    [
        (stelselgroep_info, (eenheid_input, eenheid_output))
        for stelselgroep_info in STELSELGROEPEN
        for eenheid_input, eenheid_output in zelfstandige_woonruimten_input_en_outputmodel()
    ],
)
def test_stelselgroepen_output(
    peildatum, stelselgroep_info, zelfstandige_woonruimten_input_en_outputmodel
):
    eenheid_input, eenheid_output = zelfstandige_woonruimten_input_en_outputmodel

    normaliseer_ruimte_namen(eenheid_input)

    StelselgroepClass, _, stelselgroep_enum = stelselgroep_info
    stelselgroep = StelselgroepClass(peildatum=peildatum)

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [stelselgroep.bereken(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        stelselgroep_enum,
    )


@pytest.mark.filterwarnings("ignore::UserWarning")
@pytest.mark.parametrize(
    "stelselgroep_info, output_file_path",
    [
        (stelselgroep_info, output_file_path)
        for stelselgroep_info in STELSELGROEPEN
        for output_file_path in get_specific_input_output_paths(stelselgroep_info[1])
    ],
)
def test_stelselgroep_specifiek_warnings(
    stelselgroep_info,
    output_file_path,
    peildatum,
):
    StelselgroepClass, stelselgroep_name, _ = stelselgroep_info
    eenheid_input, _ = load_specific_model(stelselgroep_name, output_file_path)
    stelselgroep = StelselgroepClass(peildatum=peildatum)

    if stelselgroep_name in specifiek_warning_mapping:
        warning_tuple = krijg_warning_tuple_op_datum(
            eenheid_input.id, peildatum, specifiek_warning_mapping[stelselgroep_name]
        )
        if warning_tuple is not None:
            with pytest.warns(warning_tuple[0], match=warning_tuple[1]):
                stelselgroep.bereken(eenheid_input)
    else:
        stelselgroep.bereken(eenheid_input)
