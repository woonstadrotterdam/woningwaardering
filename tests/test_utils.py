import difflib
from datetime import date
from decimal import Decimal
from pathlib import Path
from typing import Iterator

import pytest
from pytest import fail

from woningwaardering.stelsels.utils import naar_tabel, rond_af_op_kwart
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
    verwachte_resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
    stelselgroep: Woningwaarderingstelselgroep | None = None,
):
    if stelselgroep:
        verwachte_groepen = get_stelselgroep_resultaten(
            verwachte_resultaat, stelselgroep
        )
        verwachte_resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(
            groepen=verwachte_groepen
        )

        groepen = get_stelselgroep_resultaten(resultaat, stelselgroep)
        resultaat = WoningwaarderingResultatenWoningwaarderingResultaat(groepen=groepen)

    difflines = list(
        difflib.unified_diff(
            fromfile="verwacht",
            tofile="testresultaat",
            a=naar_tabel(verwachte_resultaat).get_string().split("\n"),
            b=naar_tabel(resultaat).get_string().split("\n"),
            lineterm="",
            n=3,
        )
    )

    colored_diff = "\n".join(kleur_diff(difflines, use_loguru_colors=True))

    if colored_diff != "":
        fail(reason=f"Output komt niet overeen\n{colored_diff}", pytrace=False)


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


def krijg_warning_tuple_op_datum(
    id: str, peildatum: date, eenheid_warning_mapping: dict
) -> tuple[Warning, str]:
    """
    Geeft de warning tuple terug die hoort bij een eenheid_id.

    Args:
        id (str): eenheid_id
        peildatum (date): peildatum
        eenheid_warning_mapping (dict): mapping van eenheid_id naar peildatum-warning

    Returns:
        tuple[Warning, str]: warning tuple
    """

    if id not in eenheid_warning_mapping:
        return None

    datum_lijst = eenheid_warning_mapping[id]

    result = None

    for datum_warning_tuple in datum_lijst:
        if peildatum >= datum_warning_tuple[0]:
            result = datum_warning_tuple[1]

    return result


def test_rond_af_op_kwart():
    # floats
    assert rond_af_op_kwart(0.125) == Decimal("0.25")
    assert rond_af_op_kwart(0.3) == Decimal("0.25")
    assert rond_af_op_kwart(0.55) == Decimal("0.5")
    assert rond_af_op_kwart(0.6) == Decimal("0.5")
    assert rond_af_op_kwart(0.625) == Decimal("0.75")
    assert rond_af_op_kwart(1.2) == Decimal("1.25")
    assert rond_af_op_kwart(1.875) == Decimal("2.0")

    # Decimals
    assert rond_af_op_kwart(Decimal("0.125")) == Decimal("0.25")
    assert rond_af_op_kwart(Decimal("0.55")) == Decimal("0.5")
    assert rond_af_op_kwart(Decimal("0.625")) == Decimal("0.75")

    # ints
    assert rond_af_op_kwart(1) == Decimal("1.0")
    assert rond_af_op_kwart(2) == Decimal("2.0")

    # Test value error
    with pytest.raises(ValueError):
        rond_af_op_kwart(None)
