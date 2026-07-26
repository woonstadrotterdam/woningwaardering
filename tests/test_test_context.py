"""Controleer dat elke testcase een input_context.md heeft met verplichte secties."""

import re
import unicodedata
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent
STELSELS_DIR = REPO_ROOT / "tests/stelsels"

VERPLICHTE_HEADINGS_STELSELGROEP = ("## Doel", "## Beleidsbron")
VERPLICHTE_HEADINGS_EENHEID = ("## Opmerkingen",)
IMPLEMENTATIETOELICHTING_LINK = re.compile(
    r"\[([^\]]+)\]\(([^)]*docs/implementatietoelichtingen/[^)#]+\.md)(#[^)]+)?\)"
)
QUOTE_BLOCK_START = re.compile(
    r"^-\s*Beleidsboek\s*\(quote\)\s*:\s*(.*)$", re.IGNORECASE
)
QUOTED_SEGMENT = re.compile(r'"([^"]*)"')
ELLIPSIS_ONLY = re.compile(r"^\s*\(\.\.\.\)\s*$")
HEADING_LINE = re.compile(r"^(#{1,6})\s+(.+)$")
MAXIMALE_HUUR = re.compile(r"maximale\s+huur(?!prijs)", re.IGNORECASE)


def _resolve_implementatietoelichting(context_path: Path, rel_path: str) -> Path:
    if rel_path.startswith("docs/"):
        return REPO_ROOT / rel_path
    return (context_path.parent / rel_path).resolve()


def _case_dirs() -> list[Path]:
    return sorted(p.parent for p in STELSELS_DIR.rglob("input.json"))


def _is_eenheidtest(case_dir: Path) -> bool:
    """True voor tests/stelsels/{stelsel}/eenheden/{id}/."""
    parts = case_dir.relative_to(STELSELS_DIR).parts
    return len(parts) >= 2 and parts[1] == "eenheden"


def _heading_anchor(title: str) -> str:
    anchor = re.sub(r"[^\w\s-]", "", title.lower())
    anchor = re.sub(r"\s+", "-", anchor).strip("-")
    return f"#{anchor}"


def _heading_anchors(md_path: Path) -> set[str]:
    anchors: set[str] = set()
    for line in md_path.read_text().splitlines():
        match = HEADING_LINE.match(line)
        if not match:
            continue
        anchors.add(_heading_anchor(match.group(2).strip()))
    return anchors


def _normalize_beleids_text(text: str) -> str:
    """Normaliseer sectietekst voor substring-vergelijking met quote-segmenten."""
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("~~", "").replace("{==", "").replace("==}", "")
    text = re.sub(r"\s+", " ", text).strip().lower()
    return text


def _normalize_quote_segment(segment: str) -> str:
    text = unicodedata.normalize("NFKC", segment)
    text = re.sub(r"\s+", " ", text).strip().lower()
    return text


def _parse_quote_blocks(content: str) -> list[list[str]]:
    """Parse Beleidsboek (quote)-blokken; elk blok is een lijst letterlijke segmenten."""
    lines = content.splitlines()
    blocks: list[list[str]] = []
    i = 0
    while i < len(lines):
        match = QUOTE_BLOCK_START.match(lines[i])
        if not match:
            i += 1
            continue

        segments: list[str] = []
        remainder = match.group(1).strip()
        if remainder:
            segments.extend(QUOTED_SEGMENT.findall(remainder))

        i += 1
        while i < len(lines):
            line = lines[i]
            stripped = line.strip()
            if not stripped:
                i += 1
                continue
            if ELLIPSIS_ONLY.match(stripped):
                i += 1
                continue
            if QUOTE_BLOCK_START.match(line) or stripped.startswith(
                ("- ", "## ", "# ")
            ):
                break
            if stripped.startswith('"') or '"' in stripped:
                found = QUOTED_SEGMENT.findall(stripped)
                if found:
                    segments.extend(found)
                    i += 1
                    continue
            break

        blocks.append(segments)
    return blocks


def _section_text_for_anchor(md_path: Path, anchor: str) -> str | None:
    """Tekst van de heading met `anchor` tot de volgende heading van gelijk/hoger niveau."""
    lines = md_path.read_text().splitlines()
    start_idx: int | None = None
    start_level: int | None = None
    for idx, line in enumerate(lines):
        match = HEADING_LINE.match(line)
        if not match:
            continue
        level = len(match.group(1))
        title = match.group(2).strip()
        if _heading_anchor(title) == anchor:
            start_idx = idx
            start_level = level
            break
    if start_idx is None or start_level is None:
        return None

    end_idx = len(lines)
    for idx in range(start_idx + 1, len(lines)):
        match = HEADING_LINE.match(lines[idx])
        if match and len(match.group(1)) <= start_level:
            end_idx = idx
            break
    return "\n".join(lines[start_idx:end_idx])


def _primary_implementatietoelichting(
    content: str, context_path: Path
) -> tuple[Path, str] | None:
    """Eerste niet-TODO implementatietoelichting-link (pad + anchor)."""
    for match in IMPLEMENTATIETOELICHTING_LINK.finditer(content):
        if "TODO" in match.group(1):
            continue
        rel_path = match.group(2)
        anchor = match.group(3) or ""
        target = _resolve_implementatietoelichting(context_path, rel_path)
        return target, anchor
    return None


def _assert_implementatietoelichting_links(content: str, context_path: Path) -> None:
    for match in IMPLEMENTATIETOELICHTING_LINK.finditer(content):
        rel_path = match.group(2)
        anchor = match.group(3) or ""
        if "TODO" in match.group(1):
            continue
        target = _resolve_implementatietoelichting(context_path, rel_path)
        assert target.exists(), f"Implementatietoelichting niet gevonden: {rel_path}"
        if anchor:
            assert anchor in _heading_anchors(
                target
            ), f"Anchor {anchor} niet gevonden in {rel_path}"


def _assert_quotes_tegen_toelichting(content: str, context_path: Path) -> None:
    quote_blocks = _parse_quote_blocks(content)
    assert quote_blocks, f"Geen Beleidsboek (quote)-blok in {context_path}"
    assert all(
        block for block in quote_blocks
    ), f"Leeg Beleidsboek (quote)-blok in {context_path}"

    primary = _primary_implementatietoelichting(content, context_path)
    assert primary is not None, f"Geen implementatietoelichting-link in {context_path}"
    target, anchor = primary
    assert anchor, f"Implementatietoelichting-link zonder anker in {context_path}"

    section = _section_text_for_anchor(target, anchor)
    assert section is not None, f"Sectie {anchor} niet gevonden in {target}"
    normalized_section = _normalize_beleids_text(section)

    for block in quote_blocks:
        search_from = 0
        for segment in block:
            normalized_segment = _normalize_quote_segment(segment)
            assert normalized_segment, f"Leeg quote-segment in {context_path}"
            pos = normalized_section.find(normalized_segment, search_from)
            assert pos != -1, (
                f"Quote-segment niet (in volgorde) gevonden in {anchor} "
                f"van {target.name} ({context_path}): {segment!r}"
            )
            search_from = pos + len(normalized_segment)


@pytest.mark.parametrize(
    "case_dir", _case_dirs(), ids=lambda p: str(p.relative_to(STELSELS_DIR))
)
def test_test_context_aanwezig_en_volledig(case_dir: Path) -> None:
    context_path = case_dir / "input_context.md"
    assert context_path.exists(), f"Geen input_context.md in {case_dir}"

    content = context_path.read_text()
    assert not MAXIMALE_HUUR.search(
        content
    ), f"Geen maximale huur noemen in {context_path}"

    eenheidtest = _is_eenheidtest(case_dir)
    verplichte = (
        VERPLICHTE_HEADINGS_EENHEID if eenheidtest else VERPLICHTE_HEADINGS_STELSELGROEP
    )
    for heading in verplichte:
        assert heading in content, f"{heading} ontbreekt in {context_path}"

    _assert_implementatietoelichting_links(content, context_path)

    quote_blocks = _parse_quote_blocks(content)
    if eenheidtest and not quote_blocks:
        return

    _assert_quotes_tegen_toelichting(content, context_path)
