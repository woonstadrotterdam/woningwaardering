from deepdiff import DeepDiff
from loguru import logger

from woningwaardering.vera.bvg.generated import (
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import Woningwaarderingstelselgroep


def assert_output_model(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    verwachte_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    stelselgroep: Woningwaarderingstelselgroep | None = None,
):
    if stelselgroep:
        stelselgroep_output = [
            groep
            for groep in verwachte_resultaat.groepen
            if groep.criterium_groep.stelselgroep.code == stelselgroep.code
        ]
        assert (
            len(stelselgroep_output) < 2
        ), f"Meer dan 1 stelselgroepresultaat gevonden voor {stelselgroep.naam}: {stelselgroep_output}"
        assert (
            len(stelselgroep_output) == 1
        ), f"Geen stelselgroepresultaat gevonden gevonden voor: {stelselgroep.naam}"
        verwachte_resultaat = stelselgroep_output[0]

    diffresult = DeepDiff(
        resultaat.model_dump(),
        verwachte_resultaat.model_dump(),
    )
    if diffresult:
        logger.error(diffresult.to_json(indent=2))
        raise ValueError(f"Modellen zijn niet gelijk: {diffresult}")
