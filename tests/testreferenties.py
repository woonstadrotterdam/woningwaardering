"""Testreferenties: het rapport en de output-JSON waarmee een test vergelijkt.

Een waarderingstest vergelijkt de uitkomst van één stelselgroep, een test van een
model op stelselniveau die van het hele stelsel. Een testreferentie staat in
`testreferenties/<testnaam>.md` naast de testmodule. Zie
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
    WoningwaarderingResultatenWoningwaarderingResultaat,
)

Uitkomst = (
    WoningwaarderingResultatenWoningwaarderingGroep
    | WoningwaarderingResultatenWoningwaarderingResultaat
)

# Alleen `task genereer-test-output` geeft deze optie mee aan pytest. Zonder de
# optie vergelijkt pytest en schrijft het nooit.
BIJWERKOPTIE = "--update-testreferenties"
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


def _rapport_blok(uitkomst: Uitkomst, eenheid: EenhedenEenheid) -> list[str]:
    if isinstance(uitkomst, WoningwaarderingResultatenWoningwaarderingResultaat):
        rapport = naar_rapport(uitkomst, eenheid_id=eenheid.id).get_string()
        return ["```text", rapport, "```"]
    rapport = naar_rapport(uitkomst).get_string()
    if not rapport:
        stelselgroep = (
            uitkomst.criterium_groep and uitkomst.criterium_groep.stelselgroep
        )
        naam = stelselgroep.naam if stelselgroep else "deze stelselgroep"
        return [f"Geen waarderingen voor {naam}."]
    return ["```text", rapport, "```"]


def maak_testreferentie(
    node: pytest.Function,
    eenheid: EenhedenEenheid,
    uitkomst: Uitkomst,
    waarschuwingen: Iterable[WarningMessage],
    beschrijving: str | None = None,
) -> str:
    """Stel de tekst van een testreferentie samen.

    De beschrijving van een model op stelselniveau komt na de docstring van de test.
    """
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
            *([beschrijving, ""] if beschrijving else []),
            *([f"Dit geval: {toelichting.args[0]}", ""] if toelichting else []),
            "## Rapport",
            "",
            *_rapport_blok(uitkomst, eenheid),
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
            *_json_blok(uitkomst),
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


def _gevallen_per_testfunctie(testmodule: Path) -> dict[str, set[str] | None]:
    """Geef per testfunctie de id's van de gevallen uit `pytest.param(..., id=...)`.

    Staat een id niet letterlijk in de code, zoals bij de modellen op stelselniveau,
    dan zijn de gevallen hier niet te kennen: de functie krijgt dan None.
    """
    testfuncties = [
        node
        for node in ast.parse(testmodule.read_text()).body
        if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")
    ]
    gevallen: dict[str, set[str] | None] = {}
    for testfunctie in testfuncties:
        ids = [
            keyword.value
            for decorator in testfunctie.decorator_list
            for call in ast.walk(decorator)
            if isinstance(call, ast.Call)
            for keyword in call.keywords
            if keyword.arg == "id"
        ]
        letterlijk = all(
            isinstance(id_, ast.Constant) and isinstance(id_.value, str) for id_ in ids
        )
        gevallen[testfunctie.name] = (
            {id_.value for id_ in ids if isinstance(id_, ast.Constant)}
            if letterlijk
            else None
        )
    return gevallen


def verweesde_testreferenties(tests_map: Path) -> list[Path]:
    """Geef de testreferenties waar geen test meer bij hoort."""
    verweesd = []
    for testreferenties_map in sorted(tests_map.rglob(MAP)):
        gevallen: dict[str, set[str] | None] = {}
        for testmodule in testreferenties_map.parent.glob("test_*.py"):
            gevallen.update(_gevallen_per_testfunctie(testmodule))

        for pad in sorted(testreferenties_map.iterdir()):
            naam = _GELDIGE_TESTNAAM.match(pad.stem)
            functie = naam.group("functie") if naam else None
            geval = naam.group("geval") if naam else None
            if pad.suffix != ".md" or functie not in gevallen:
                verweesd.append(pad)
                continue
            bekend = gevallen[functie]
            if bekend is not None and (
                (geval is None) != (not bekend)
                or (geval is not None and geval not in bekend)
            ):
                verweesd.append(pad)
    return verweesd
