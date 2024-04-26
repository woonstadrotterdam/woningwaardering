import difflib
import re
from datetime import date, datetime
from pathlib import Path
from typing import Iterator

from pytest import fail

from woningwaardering.stelsels.utils import naar_tabel
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

    difflines = [
        *difflib.unified_diff(
            fromfile="verwacht",
            tofile="testresultaat",
            a=naar_tabel(verwachte_resultaat).get_string().split("\n"),
            b=naar_tabel(resultaat).get_string().split("\n"),
            lineterm="",
            n=3,
        )
    ]

    colored_diff = "\n".join(kleur_diff(difflines, use_loguru_colors=True))

    if colored_diff != "":
        fail(reason=f"Output komt niet overeen\n{colored_diff}", pytrace=False)


def laad_specifiek_input_en_output_model(
    module_path: Path,
    output_json_path: Path,
) -> tuple[EenhedenEenheid, WoningwaarderingResultatenWoningwaarderingResultaat, date]:
    file_name = output_json_path.name
    input_path = module_path / f"data/input/{file_name}"
    peildatum_match = re.search(r"\d{4}-\d{2}-\d{2}", str(output_json_path))
    if peildatum_match is None:
        raise ValueError(f"geen datum gevonden in bestandsnaam {file_name}")
    peildatum = datetime.strptime(peildatum_match.group(0), "%Y-%m-%d").date()
    with open(input_path, "r+") as f:
        eenheid_input = EenhedenEenheid.model_validate_json(f.read())

    with open(output_json_path, "r+") as f:
        eenheid_output = (
            WoningwaarderingResultatenWoningwaarderingResultaat.model_validate_json(
                f.read()
            )
        )

    return eenheid_input, eenheid_output, peildatum


def kleur_diff(diffresult: list[str], use_loguru_colors: bool = True) -> Iterator[str]:
    green = "\x1b[92m"
    red = "\x1b[91m"
    reset = "\x1b[0m"

    return (
        (green + diff + reset)
        if diff.startswith("+")
        else (red + diff + reset)
        if diff.startswith("-")
        else diff
        for diff in diffresult
    )
