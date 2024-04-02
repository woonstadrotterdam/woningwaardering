from datetime import date

from deepdiff import DeepDiff
from loguru import logger

from woningwaardering.stelsels.zelfstandige_woonruimten import (
    OppervlakteVanVertrekken,
)
from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingGroep,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep


def test_OppervlakteVanVertrekken(eenheid_inputmodel, woningwaardering_resultaat):
    ovz = OppervlakteVanVertrekken(peildatum=date(2024, 1, 1))
    resultaat = ovz.bereken(eenheid_inputmodel, woningwaardering_resultaat)
    assert isinstance(resultaat, WoningwaarderingResultatenWoningwaarderingGroep)


def test_OppervlakteVanVertrekken_output(eenheid_input_en_output):
    eenheid_input, eenheid_output = eenheid_input_en_output
    ovz = OppervlakteVanVertrekken(peildatum=date(2024, 1, 1))
    resultaat = ovz.bereken(eenheid_input)
    eenheid_output_ovz = [
        groep
        for groep in eenheid_output.groepen
        if groep.criterium_groep.stelselgroep.code
        == Woningwaarderingstelselgroep.oppervlakte_van_vertrekken.code
    ]
    assert (
        len(eenheid_output_ovz) < 2
    ), f"Meer dan 1 groep gevonden: {eenheid_output_ovz}"
    assert len(eenheid_output_ovz) == 1, "Geen groep gevonden!"

    diffresult = DeepDiff(resultaat.model_dump(), eenheid_output_ovz[0].model_dump())
    if diffresult:
        logger.error(diffresult.to_json(indent=2))
        raise ValueError(f"Models are not equal: {diffresult}")
