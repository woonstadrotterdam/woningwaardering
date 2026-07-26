"""Controleer dat elke testcase een input_context.md heeft met verplichte secties."""

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent
STELSELS_DIR = REPO_ROOT / "tests/stelsels"

VERPLICHTE_HEADINGS = ("## Doel", "## Beleidsbron")
IMPLEMENTATIETOELICHTING_LINK = re.compile(
    r"\[([^\]]+)\]\(([^)]*docs/implementatietoelichtingen/[^)#]+\.md)(#[^)]+)?\)"
)


def _resolve_implementatietoelichting(context_path: Path, rel_path: str) -> Path:
    if rel_path.startswith("docs/"):
        return REPO_ROOT / rel_path
    return (context_path.parent / rel_path).resolve()


def _case_dirs() -> list[Path]:
    return sorted(p.parent for p in STELSELS_DIR.rglob("input.json"))


def _heading_anchors(md_path: Path) -> set[str]:
    anchors: set[str] = set()
    for line in md_path.read_text().splitlines():
        match = re.match(r"^#{1,6}\s+(.+)$", line)
        if not match:
            continue
        title = match.group(1).strip()
        anchor = re.sub(r"[^\w\s-]", "", title.lower())
        anchor = re.sub(r"\s+", "-", anchor).strip("-")
        anchors.add(f"#{anchor}")
    return anchors


@pytest.mark.parametrize(
    "case_dir", _case_dirs(), ids=lambda p: str(p.relative_to(STELSELS_DIR))
)
def test_test_context_aanwezig_en_volledig(case_dir: Path) -> None:
    context_path = case_dir / "input_context.md"
    assert context_path.exists(), f"Geen input_context.md in {case_dir}"

    content = context_path.read_text()
    for heading in VERPLICHTE_HEADINGS:
        assert heading in content, f"{heading} ontbreekt in {context_path}"

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
