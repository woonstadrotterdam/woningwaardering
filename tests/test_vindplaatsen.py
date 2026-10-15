"""De vindplaatsen in de docstrings van waarderingstests bestaan.

De vormen van een vindplaats staan in `docs/voor-ontwikkelaars/testing.md`
onder "Docstring".
"""

import ast
import re
import xml.etree.ElementTree as ET
from functools import cache
from pathlib import Path

import pytest

TESTS_MAP = Path(__file__).parent
REPO = TESTS_MAP.parent
TOELICHTINGEN = REPO / "docs/implementatietoelichtingen"
WETTEKST = REPO / "wettelijke-documenten/BWBR0003237_2026-01-01_0.xml"

RANGTELWOORDEN = ["eerste", "tweede", "derde", "vierde", "vijfde", "zesde", "zevende"]

TOELICHTING = re.compile(
    r"implementatietoelichting (zelfstandige|onzelfstandige) woonruimten, "
    r"(\d+(?:\.\d+)*)"
)
TOELICHTING_DATAMODEL = re.compile(
    r'implementatietoelichting datamodel-uitbreidingen, "([^"]+)"'
)
ONTWIKKELAARSDOCS = re.compile(r'docs/voor-ontwikkelaars/([\w-]+), "([^"]+)"')
ONDERDEEL = re.compile(r"wettekst, Bijlage I onder ([AB]), onderdeel (\d+(?:\.\d+)?)")
RUBRIEK = re.compile(
    r"wettekst, Bijlage I onder ([AB]), toelichting rubriek (\d+(?:\.\d+)?)"
    r"( \(via Bijlage I onder B, toelichting, inleiding\))?"
)
INLEIDING = re.compile(r"wettekst, Bijlage I onder ([AB]), toelichting, inleiding")
ARTIKEL = re.compile(r"wettekst, artikel (\w+), (\w+) lid")


def _waarderingstests() -> list[tuple[str, str | None]]:
    """Geef per waarderingstest de plek en de docstring.

    Een waarderingstest is een test die `vergelijk_met_testreferentie` gebruikt.
    """
    tests = []
    for module in sorted((TESTS_MAP / "stelsels").rglob("test_*.py")):
        for node in ast.walk(ast.parse(module.read_text())):
            if not isinstance(node, ast.FunctionDef):
                continue
            argumenten = [argument.arg for argument in node.args.args]
            if "vergelijk_met_testreferentie" in argumenten:
                plek = f"{module.relative_to(REPO)}::{node.name}"
                tests.append((plek, ast.get_docstring(node)))
    return tests


def _vindplaatsen(docstring: str) -> list[list[str]]:
    """Geef per alinea die met "Bron:" begint de vindplaatsen."""
    bronnen = []
    for alinea in docstring.split("\n\n"):
        if alinea.startswith("Bron: "):
            tekst = " ".join(alinea.removeprefix("Bron: ").split())
            bronnen.append(tekst.removesuffix(".").split("; "))
    return bronnen


@cache
def _koppen(bestand: Path) -> list[str]:
    return [
        regel.lstrip("#").strip()
        for regel in bestand.read_text().splitlines()
        if regel.startswith("#")
    ]


def _tekst(element: ET.Element) -> str:
    return " ".join("".join(element.itertext()).split())


@cache
def _wettekst() -> dict[str, set[str]]:
    """Geef de onderdelen en de rubrieken van de toelichting van bijlage I, onder A en B."""
    wettekst = ET.parse(WETTEKST)
    bijlage = next(
        element
        for element in wettekst.iter("bijlage")
        if element.get("label") == "Bijlage I"
    )
    nummers: dict[str, set[str]] = {}
    for onder, divisie in zip("AB", bijlage.findall("divisie")):
        nummers[f"{onder} onderdeel"] = {
            match.group(1)
            for tabel in divisie.findall("table")
            for entry in tabel.iter("entry")
            if (match := re.match(r"(\d+(?:\.\d+)?)\.? +[A-Z]", _tekst(entry)))
        }
        nummers[f"{onder} rubriek"] = {
            _tekst(nummer)
            for kop in divisie.iter("kop")
            if (nummer := kop.find("nr")) is not None
        }
    for artikel in wettekst.iter("artikel"):
        nummers[f"artikel {artikel.get('label', '').removeprefix('Artikel ')}"] = {
            _tekst(nummer) for nummer in artikel.iter("lidnr")
        }
    return nummers


def _fout_in(vindplaats: str) -> str | None:
    """Geef wat er niet klopt aan een vindplaats, of None als ze bestaat."""
    if match := TOELICHTING.fullmatch(vindplaats):
        stelsel, nummer = match.groups()
        koppen = _koppen(TOELICHTINGEN / f"{stelsel}-woonruimten.md")
        if not any(re.match(rf"{re.escape(nummer)}( |$)", kop) for kop in koppen):
            return "paragraaf bestaat niet"
    elif match := TOELICHTING_DATAMODEL.fullmatch(vindplaats):
        if match.group(1) not in _koppen(TOELICHTINGEN / "datamodel-uitbreidingen.md"):
            return "kop bestaat niet"
    elif match := ONTWIKKELAARSDOCS.fullmatch(vindplaats):
        bestand, kop = match.groups()
        pad = REPO / "docs/voor-ontwikkelaars" / f"{bestand}.md"
        if not pad.exists() or kop not in _koppen(pad):
            return "kop bestaat niet"
    elif match := ONDERDEEL.fullmatch(vindplaats):
        onder, nummer = match.groups()
        if nummer not in _wettekst()[f"{onder} onderdeel"]:
            return "onderdeel bestaat niet"
    elif match := RUBRIEK.fullmatch(vindplaats):
        onder, nummer, via = match.groups()
        if nummer not in _wettekst()[f"{onder} rubriek"]:
            return "rubriek bestaat niet in de toelichting"
        if via and onder != "A":
            return "alleen de toelichting onder A geldt via de inleiding onder B"
    elif INLEIDING.fullmatch(vindplaats):
        pass
    elif match := ARTIKEL.fullmatch(vindplaats):
        artikel, lid = match.groups()
        leden = _wettekst().get(f"artikel {artikel}")
        if leden is None:
            return "artikel bestaat niet"
        if lid not in RANGTELWOORDEN or str(RANGTELWOORDEN.index(lid) + 1) not in leden:
            return "lid bestaat niet"
    else:
        return "onbekende vorm"
    return None


def test_vindplaatsen_van_waarderingstests_bestaan():
    """Elke vindplaats in de docstring van een waarderingstest bestaat.

    Een alinea die met "Bron:" begint, noemt eerst de paragraaf van de
    implementatietoelichting en daarna eventueel de wettekst.
    """
    fouten = []
    for plek, docstring in _waarderingstests():
        for vindplaatsen in _vindplaatsen(docstring or ""):
            if not vindplaatsen[0].startswith("implementatietoelichting"):
                fouten.append(f"{plek}: begint niet met de implementatietoelichting")
            for vindplaats in vindplaatsen:
                if fout := _fout_in(vindplaats):
                    fouten.append(f"{plek}: {fout}: {vindplaats}")
    assert fouten == []


@pytest.mark.parametrize(
    ("vindplaats", "fout"),
    [
        ("implementatietoelichting zelfstandige woonruimten, 2.6.2", None),
        (
            "implementatietoelichting zelfstandige woonruimten, 2.6.9",
            "paragraaf bestaat niet",
        ),
        (
            'implementatietoelichting datamodel-uitbreidingen, "Parkeergelegenheden"',
            None,
        ),
        ("wettekst, Bijlage I onder A, onderdeel 6.2", None),
        ("wettekst, Bijlage I onder B, onderdeel 11.3", "onderdeel bestaat niet"),
        ("wettekst, Bijlage I onder B, toelichting rubriek 13", None),
        (
            "wettekst, Bijlage I onder A, toelichting rubriek 13",
            "rubriek bestaat niet in de toelichting",
        ),
        (
            "wettekst, Bijlage I onder B, toelichting rubriek 9 "
            "(via Bijlage I onder B, toelichting, inleiding)",
            "alleen de toelichting onder A geldt via de inleiding onder B",
        ),
        (
            "wettekst, Bijlage I onder A, toelichting rubriek 8 "
            "(via Bijlage I onder B, toelichting, inleiding)",
            None,
        ),
        (
            "wettekst, Bijlage I onder B, toelichting rubriek 8 "
            "(via Bijlage I onder A, toelichting, inleiding)",
            "onbekende vorm",
        ),
        ("wettekst, Bijlage I onder A, toelichting, inleiding", None),
        ("wettekst, artikel 8a, tweede lid", None),
        ("wettekst, artikel 8a, achtste lid", "lid bestaat niet"),
        ('wettekst, Bijlage I onder A, onderdeel 6.2: "Bad"', "onbekende vorm"),
    ],
)
def test_fout_in_vindplaats(vindplaats, fout):
    assert _fout_in(vindplaats) == fout
