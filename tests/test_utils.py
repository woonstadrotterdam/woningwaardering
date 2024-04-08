import re
from datetime import date, datetime
from pathlib import Path

from deepdiff import DeepDiff
from loguru import logger

from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelselgroep,
)


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


def laad_specifiek_input_en_output_model(
    module_path: Path,
    output_json_path: Path,
) -> tuple[EenhedenEenheid, WoningwaarderingResultatenWoningwaarderingResultaat, date]:
    file_name = output_json_path.name
    input_path = module_path / f"data/input/{file_name}"
    peildatum = re.search(r"\d{4}-\d{2}-\d{2}", str(output_json_path)).group(0)
    peildatum = datetime.strptime(peildatum, "%Y-%m-%d").date()
    with open(input_path, "r+") as f:
        eenheid_input = EenhedenEenheid.model_validate_json(f.read())

    with open(output_json_path, "r+") as f:
        eenheid_output = (
            WoningwaarderingResultatenWoningwaarderingResultaat.model_validate_json(
                f.read()
            )
        )

    return eenheid_input, eenheid_output, peildatum
