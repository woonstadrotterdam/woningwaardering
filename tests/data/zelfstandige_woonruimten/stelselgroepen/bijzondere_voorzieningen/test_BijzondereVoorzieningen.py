from pathlib import Path

from tests.utils import (
    assert_stelselgroep_output,
    assert_stelselgroep_specifiek_output,
    maak_specifieke_input_en_output_model_fixture,
)
from woningwaardering.stelsels.builders import WaarderingsgroepBuilder
from woningwaardering.stelsels.zelfstandige_woonruimten.bijzondere_voorzieningen import (
    BijzondereVoorzieningen,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.bijzondere_voorzieningen.bijzondere_voorzieningen import (
    UITGESLOTEN_ZORGWONING_GRONDSLAG_CRITERIUM_IDS,
)
from woningwaardering.stelsels.zelfstandige_woonruimten.punten_voor_de_woz_waarde.punten_voor_de_woz_waarde import (
    NIEUWBOUW_MINIMUM_PUNTEN_CRITERIUM_ID,
    NIEUWBOUW_MINIMUM_PUNTEN_ID,
)
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Doelgroep,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)


def test_BijzondereVoorzieningen_output(
    zelfstandige_woonruimten_input_en_outputmodel, peildatum
):
    assert_stelselgroep_output(
        zelfstandige_woonruimten_input_en_outputmodel,
        peildatum,
        BijzondereVoorzieningen,
    )


specifieke_input_en_output_model = maak_specifieke_input_en_output_model_fixture(
    Path(__file__).parent
)


def test_BijzondereVoorzieningen_specifiek_output(
    specifieke_input_en_output_model, peildatum
):
    assert_stelselgroep_specifiek_output(
        specifieke_input_en_output_model,
        peildatum,
        BijzondereVoorzieningen,
    )


def test_BijzondereVoorzieningen_zorgwoninggrondslag_sluit_nieuwbouwminimum_uit(
    peildatum,
):
    eenheid = EenhedenEenheid(
        id="zorgwoning",
        doelgroep=Doelgroep.zorg,
        woningwaarderingstelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
    )

    oppervlakte_builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        Woningwaarderingstelselgroep.oppervlakte_van_vertrekken,
    )
    oppervlakte_builder.met_onderliggend(
        id="vertrekken", naam="Vertrekken", punten=120.0
    )

    woz_builder = WaarderingsgroepBuilder(
        Woningwaarderingstelsel.zelfstandige_woonruimten,
        Woningwaarderingstelselgroep.punten_voor_de_woz_waarde,
    )
    woz_builder.met_onderliggend(id="woz_basis", naam="WOZ basis", punten=20.0)
    woz_builder.met_onderliggend(
        id=NIEUWBOUW_MINIMUM_PUNTEN_ID,
        naam="Nieuwbouw: min. 30 punten",
        punten=10.0,
    )

    woningwaardering_resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
        groepen=[oppervlakte_builder.build(), woz_builder.build()]
    )

    groep = BijzondereVoorzieningen(peildatum=peildatum).waardeer(
        eenheid, woningwaardering_resultaat
    )

    assert UITGESLOTEN_ZORGWONING_GRONDSLAG_CRITERIUM_IDS == [
        NIEUWBOUW_MINIMUM_PUNTEN_CRITERIUM_ID
    ]
    assert groep.punten == 49.0
    assert groep.woningwaarderingen is not None
    assert len(groep.woningwaarderingen) == 1
    assert groep.woningwaarderingen[0].criterium is not None
    assert (
        groep.woningwaarderingen[0].criterium.id
        == "bijzondere_voorzieningen__zorgwoning_puntenverhoging"
    )
    assert groep.woningwaarderingen[0].punten == 49.0
