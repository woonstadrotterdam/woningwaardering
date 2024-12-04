import difflib
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterator

import pytest
from pytest import fail

from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import naar_tabel
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Woningwaarderingstelselgroep,
)


def get_stelselgroep_resultaten(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    stelselgroep: Woningwaarderingstelselgroep,
) -> list[WoningwaarderingResultatenWoningwaarderingGroep]:
    resultaten = [
        groep
        for groep in resultaat.groepen or []
        if groep.criterium_groep.stelselgroep.code == stelselgroep.code
    ]
    assert (
        len(resultaten) < 2
    ), f"Meer dan 1 stelselgroepresultaat gevonden voor {stelselgroep.naam}: {resultaten}"
    assert (
        len(resultaten) == 1
    ), f"Geen stelselgroepresultaat gevonden voor: {stelselgroep.naam}"
    return resultaten


def assert_output_model(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    verwacht_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    stelselgroep: Woningwaarderingstelselgroep | None = None,
):
    if stelselgroep:
        verwachte_groepen = get_stelselgroep_resultaten(
            verwacht_resultaat, stelselgroep
        )
        verwacht_resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
            groepen=verwachte_groepen
        )

        groepen = get_stelselgroep_resultaten(resultaat, stelselgroep)
        resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(groepen=groepen)

    difflines = list(
        difflib.unified_diff(
            fromfile="verwacht",
            tofile="testresultaat",
            a=naar_tabel(verwacht_resultaat).get_string().split("\n"),
            b=naar_tabel(resultaat).get_string().split("\n"),
            lineterm="",
            n=3,
        )
    )

    colored_diff = "\n".join(kleur_diff(difflines, use_loguru_colors=True))

    if colored_diff != "":
        fail(reason=f"Output komt niet overeen\n{colored_diff}", pytrace=False)

    assert (
        verwacht_resultaat == resultaat
    ), "Output-model verschilt van verwacht resultaat"


def laad_specifiek_input_en_output_model(
    module_path: Path,
    output_json_path: Path,
) -> tuple[EenhedenEenheid, WoningwaarderingResultatenWoningwaarderingResultaat]:
    file_name = output_json_path.name
    input_path = module_path / f"input/{file_name}"
    with open(input_path, "r+") as f:
        eenheid_input = EenhedenEenheid.model_validate_json(f.read())

    with open(output_json_path, "r+") as f:
        eenheid_output = (
            WoningwaarderingResultatenWoningwaarderingResultaat.model_validate_json(
                f.read()
            )
        )

    return eenheid_input, eenheid_output


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


@dataclass
class WarningConfig:
    file: str
    peildatum: date
    warnings: dict[type[Warning], str]


def stelselgroep_warnings(
    warning_config: WarningConfig, peildatum: date, stelselgroep_class: Stelselgroep
):
    """
    Generieke functie om warnings voor stelselgroepen te testen

    Args:
        warning_config (WarningConfig): WarningConfig object met waarschuwing test configuratie
        peildatum (date): peildatum
        stelselgroep_class (Stelselgroep): Class van de stelselgroep om te testen
    """
    if peildatum < warning_config.peildatum:
        pytest.skip(f"Warning is niet van toepassing op peildatum: {peildatum}")

    with open(warning_config.file, "r+") as f:
        eenheid_input = EenhedenEenheid.model_validate_json(f.read())

    with pytest.warns() as records:
        stelselgroep = stelselgroep_class(peildatum=peildatum)
        stelselgroep.waardeer(eenheid_input)

        warning_message = [(r.category, str(r.message)) for r in records]
        for warning_type, warning_message in warning_config.warnings.items():
            assert any(
                [
                    warning_type == r.category and warning_message in str(r.message)
                    for r in records
                ]
            ), f"Geen {warning_type} met message '{warning_message}' geraised"
