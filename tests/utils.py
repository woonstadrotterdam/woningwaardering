import difflib
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterator

import pytest
from pytest import fail

from woningwaardering.stelsels import utils
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.stelsels.utils import naar_tabel, normaliseer_ruimte_namen
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
        if groep.criterium_groep.stelselgroep == stelselgroep
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

    difflines_json = list(
        difflib.unified_diff(
            fromfile="verwacht",
            tofile="testresultaat",
            a=verwacht_resultaat.model_dump_json(indent=2, exclude_none=True).split(
                "\n"
            ),
            b=resultaat.model_dump_json(indent=2, exclude_none=True).split("\n"),
            lineterm="",
            n=3,
        )
    )

    colored_diff_json = "\n".join(kleur_diff(difflines_json, use_loguru_colors=True))

    if colored_diff_json != "":
        fail(
            reason=f"Json output komt niet overeen\n{colored_diff_json}", pytrace=False
        )

    assert_som_bovenliggend_criterium(resultaat)
    assert_punten_afgerond_op_kwarten(resultaat)


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


def assert_stelselgroep_warnings(
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


def assert_stelselgroep_output(
    input_en_output_model: tuple[
        EenhedenEenheid, WoningwaarderingResultatenWoningwaarderingResultaat
    ],
    peildatum: date,
    stelselgroep_class: Stelselgroep,
):
    eenheid_input, eenheid_output = input_en_output_model
    normaliseer_ruimte_namen(eenheid_input)

    stelselgroep = stelselgroep_class(peildatum=peildatum)

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    assert isinstance(
        resultaat, WoningwaarderingResultatenWoningwaarderingResultaat
    ), "Resultaat is geen WoningwaarderingResultatenWoningwaarderingResultaat"
    resultaat.groepen = [stelselgroep.waardeer(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        stelselgroep.stelselgroep,
    )

    assert_som_bovenliggend_criterium(resultaat)


def assert_stelselgroep_specifiek_output(
    specifieke_input_en_output_model: tuple[
        EenhedenEenheid, WoningwaarderingResultatenWoningwaarderingResultaat
    ],
    peildatum: date,
    stelselgroep_class: Stelselgroep,
):
    """
    Generieke functie om specifieke output voor stelselgroepen te testen

    Args:
        specifieke_input_en_output_model (tuple[EenhedenEenheid, WoningwaarderingResultatenWoningwaarderingResultaat]): Tuple van input en verwachte output
        peildatum (date): peildatum
        stelselgroep_class (Stelselgroep): Class van de stelselgroep om te testen
    """
    eenheid_input, eenheid_output = specifieke_input_en_output_model
    stelselgroep = stelselgroep_class(peildatum=peildatum)

    resultaat = WoningwaarderingResultatenWoningwaarderingResultaat()
    resultaat.groepen = [stelselgroep.waardeer(eenheid_input)]

    assert_output_model(
        resultaat,
        eenheid_output,
        stelselgroep.stelselgroep,
    )

    assert_som_bovenliggend_criterium(resultaat)


def maak_specifieke_input_en_output_model_fixture(base_path: Path) -> pytest.fixture:
    """
    Factory functie die een pytest fixture maakt voor het laden van specifieke test cases.

    Args:
        base_path (Path): Pad naar de directory waarin de test file zich bevindt

    Returns:
        pytest.fixture: Een pytest fixture die een tuple van input en output model retourneert
    """

    @pytest.fixture(params=[str(p) for p in (base_path / "output").rglob("*.json")])
    def specifieke_input_en_output_model(request):
        current_file_path = Path(request.fspath).parent
        output_file_path = request.param
        return laad_specifiek_input_en_output_model(
            current_file_path, Path(output_file_path)
        )

    return specifieke_input_en_output_model


def assert_geen_dubbele_aantal_in_hierarchie(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
) -> None:
    """Geen structurele ouder met aantal wanneer onderliggende waarderingen ook aantal hebben."""
    for groep in resultaat.groepen or []:
        waarderingen = groep.woningwaarderingen or []
        parent_ids = utils.parent_ids_met_onderliggende_aantal(waarderingen)
        for waardering in waarderingen:
            if (
                waardering.aantal is None
                or waardering.criterium is None
                or waardering.criterium.id is None
            ):
                continue
            if waardering.criterium.id not in parent_ids:
                continue
            if waardering.punten is not None:
                continue
            assert False, (
                f"Waardering {waardering.criterium.id} heeft aantal terwijl onderliggende "
                f"waarderingen ook aantal hebben "
                f"(groep "
                f"{groep.criterium_groep and groep.criterium_groep.stelselgroep and groep.criterium_groep.stelselgroep.naam})"
            )


def assert_geen_dubbele_punten_in_hierarchie(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
) -> None:
    """Geen ouder met punten wanneer een onderliggende waardering ook punten heeft."""
    for groep in resultaat.groepen or []:
        waarderingen = groep.woningwaarderingen or []
        parent_ids = utils.parent_ids_met_onderliggende_punten(waarderingen)
        for waardering in waarderingen:
            if (
                waardering.punten is None
                or waardering.criterium is None
                or waardering.criterium.id is None
            ):
                continue
            assert waardering.criterium.id not in parent_ids, (
                f"Waardering {waardering.criterium.id} heeft punten terwijl onderliggende "
                f"waarderingen ook punten hebben "
                f"(groep "
                f"{groep.criterium_groep and groep.criterium_groep.stelselgroep and groep.criterium_groep.stelselgroep.naam})"
            )


def assert_groep_punten_is_som_van_waarderingen(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
) -> None:
    """groep.punten is de som van punten op waarderingen (indien die punten hebben)."""
    for groep in resultaat.groepen or []:
        waarderingen = groep.woningwaarderingen or []
        if groep.punten is None:
            continue
        if not any(w.punten is not None for w in waarderingen):
            continue
        # Oppervlakte-stelselgroepen: groep.punten uit som aantal×factor + aparte puntenregels
        if any(w.aantal is not None and w.punten is None for w in waarderingen):
            continue
        verwacht = utils.som_punten_waarderingen(waarderingen)
        assert groep.punten == verwacht, (
            f"groep.punten ({groep.punten}) != som waarderingen ({verwacht}) "
            f"in groep "
            f"{groep.criterium_groep and groep.criterium_groep.stelselgroep and groep.criterium_groep.stelselgroep.naam}"
        )


def assert_som_bovenliggend_criterium(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
) -> None:
    assert_geen_dubbele_punten_in_hierarchie(resultaat)
    assert_geen_dubbele_aantal_in_hierarchie(resultaat)
    assert_groep_punten_is_som_van_waarderingen(resultaat)


def assert_punten_afgerond_op_kwarten(
    resultaat: WoningwaarderingResultatenWoningwaarderingResultaat,
):
    """
    Controleert of alle punten in het resultaat zijn afgerond op kwarten (0.25).
    """
    for groep in resultaat.groepen or []:
        # Check groepstotaal
        if groep.punten is not None:
            remainder = round((groep.punten % 0.25) * 100) / 100
            assert (
                remainder == 0.0
            ), f"Groep '{groep.criterium_groep.naam}' heeft punten {groep.punten} die niet zijn afgerond op kwarten"
