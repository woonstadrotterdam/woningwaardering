"""Testreferenties: het rapport en de output-JSON waarmee een waarderingstest vergelijkt.

Een testreferentie staat in `testreferenties/<testnaam>.md` naast de testmodule. Zie
docs/voor-ontwikkelaars/testing.md voor de afspraken.
"""

import ast
import difflib
import inspect
import re
from collections.abc import Iterable
from pathlib import Path
from warnings import WarningMessage

import pytest
from pydantic import BaseModel

from tests.utils import kleur_diff
from woningwaardering.rapport import naar_rapport
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    WoningwaarderingResultatenWoningwaarderingGroep,
)

# Alleen `task genereer-test-output` geeft deze optie mee aan pytest. Zonder de
# optie vergelijkt pytest en schrijft het nooit.
BIJWERKOPTIE = "--werk-testreferenties-bij"
BIJWERKOPDRACHT = "task genereer-test-output"

# De map met testreferenties, naast de testmodule.
MAP = "testreferenties"

# De naam van een test is `test_functie` of, bij een geparametriseerde test,
# `test_functie[geval]`. Hij wordt de bestandsnaam van de testreferentie; het
# geval mag daarom alleen letters, cijfers, `_` en `-` bevatten.
_GELDIGE_TESTNAAM = re.compile(r"^(?P<functie>\w+)(\[(?P<geval>[\w\-]+)\])?$")


def pad_van_testreferentie(node: pytest.Item) -> Path:
    """Geef het pad van de testreferentie van een test."""
    if not _GELDIGE_TESTNAAM.match(node.name):
        pytest.fail(
            f"De id van een geval mag alleen letters, cijfers, _ en - bevatten, "
            f"omdat hij de bestandsnaam van de testreferentie wordt: {node.name}",
            pytrace=False,
        )
    return node.path.parent / MAP / f"{node.name}.md"


def _json_blok(model: BaseModel, *, alleen_ingevuld: bool = False) -> list[str]:
    return [
        "```json",
        model.model_dump_json(
            by_alias=True,
            exclude_none=True,
            exclude_unset=alleen_ingevuld,
            indent=2,
        ),
        "```",
    ]


def _rapport_blok(groep: WoningwaarderingResultatenWoningwaarderingGroep) -> list[str]:
    rapport = naar_rapport(groep).get_string()
    if not rapport:
        stelselgroep = groep.criterium_groep and groep.criterium_groep.stelselgroep
        naam = stelselgroep.naam if stelselgroep else "deze stelselgroep"
        return [f"Geen waarderingen voor {naam}."]
    return ["```text", rapport, "```"]


def maak_testreferentie(
    node: pytest.Function,
    eenheid: EenhedenEenheid,
    groep: WoningwaarderingResultatenWoningwaarderingGroep,
    waarschuwingen: Iterable[WarningMessage],
) -> str:
    """Stel de tekst van een testreferentie samen."""
    docstring = inspect.getdoc(node.function)
    if not docstring:
        pytest.fail(
            f"{node.name} heeft geen docstring. Een waarderingstest beschrijft de "
            "beleidsregel en de bron in zijn docstring.",
            pytrace=False,
        )
    toelichting = node.get_closest_marker("toelichting")
    return "\n".join(
        [
            f"# {node.name}",
            "",
            docstring,
            "",
            *([f"Dit geval: {toelichting.args[0]}", ""] if toelichting else []),
            "## Rapport",
            "",
            *_rapport_blok(groep),
            "",
            "## Waarschuwingen",
            "",
            *(
                [f"- {w.category.__name__}: {w.message}" for w in waarschuwingen]
                or ["Geen."]
            ),
            "",
            "## Input",
            "",
            # Alleen wat de test invult: een standaardwaarde van het model,
            # zoals `aantal` op een ruimte, is geen input van de test.
            *_json_blok(eenheid, alleen_ingevuld=True),
            "",
            "## Output",
            "",
            *_json_blok(groep),
            "",
        ]
    )


def vergelijk_of_werk_bij(pad: Path, testreferentie: str, *, bijwerken: bool) -> None:
    """Vergelijk de testreferentie met het bestand, of schrijf het bij het bijwerken."""
    if bijwerken:
        pad.parent.mkdir(parents=True, exist_ok=True)
        pad.write_text(testreferentie)
        return

    if not pad.exists():
        pytest.fail(
            f"Geen testreferentie: {pad.name}\n"
            f"Draai `{BIJWERKOPDRACHT}` en beoordeel het nieuwe bestand.",
            pytrace=False,
        )

    diff = list(
        difflib.unified_diff(
            pad.read_text().split("\n"),
            testreferentie.split("\n"),
            fromfile="testreferentie",
            tofile="testresultaat",
            lineterm="",
            n=3,
        )
    )
    if diff:
        pytest.fail(
            f"De waardering wijkt af van de testreferentie {pad.name}\n"
            + "\n".join(kleur_diff(diff))
            + "\n\nVoorzag de taak deze wijziging in de output? Draai dan "
            f"`{BIJWERKOPDRACHT}` en beoordeel de diff. Zo niet: herstel de code "
            "en laat de testreferentie staan.",
            pytrace=False,
        )


def assert_geen_onverwachte_waarschuwingen(
    opgevangen: Iterable[WarningMessage], meegegeven: Iterable[WarningMessage]
) -> None:
    """Faal bij een `UserWarning` die de test niet aan de testreferentie meegeeft."""
    teksten = {str(waarschuwing.message) for waarschuwing in meegegeven}
    onverwacht = [
        str(waarschuwing.message)
        for waarschuwing in opgevangen
        if issubclass(waarschuwing.category, UserWarning)
        and str(waarschuwing.message) not in teksten
    ]
    assert not onverwacht, (
        "Onverwachte waarschuwing. Vang een verwachte waarschuwing op met "
        f"pytest.warns en geef hem mee aan vergelijk_met_testreferentie: {onverwacht}"
    )


def _gevallen_per_testfunctie(testmodule: Path) -> dict[str, set[str]]:
    """Geef per testfunctie de id's van de gevallen uit `pytest.param(..., id=...)`."""
    testfuncties = [
        node
        for node in ast.parse(testmodule.read_text()).body
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")
    ]
    return {
        testfunctie.name: {
            keyword.value.value
            for decorator in testfunctie.decorator_list
            for call in ast.walk(decorator)
            if isinstance(call, ast.Call)
            for keyword in call.keywords
            if keyword.arg == "id"
            and isinstance(keyword.value, ast.Constant)
            and isinstance(keyword.value.value, str)
        }
        for testfunctie in testfuncties
    }


def verweesde_testreferenties(tests_map: Path) -> list[Path]:
    """Geef de testreferenties waar geen test meer bij hoort."""
    verweesd = []
    for testreferenties_map in sorted(tests_map.rglob(MAP)):
        gevallen: dict[str, set[str]] = {}
        for testmodule in testreferenties_map.parent.glob("test_*.py"):
            gevallen.update(_gevallen_per_testfunctie(testmodule))

        for pad in sorted(testreferenties_map.iterdir()):
            naam = _GELDIGE_TESTNAAM.match(pad.stem)
            functie = naam.group("functie") if naam else None
            geval = naam.group("geval") if naam else None
            if (
                pad.suffix != ".md"
                or functie not in gevallen
                or (geval is None) != (not gevallen[functie])
                or (geval is not None and geval not in gevallen[functie])
            ):
                verweesd.append(pad)
    return verweesd
