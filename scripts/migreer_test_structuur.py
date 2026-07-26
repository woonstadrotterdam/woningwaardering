"""Eenmalige migratie: tests/data/ -> tests/stelsels/ met per-eenheid mappen."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OLD_DATA = ROOT / "tests/data"
NEW_STELSELS = ROOT / "tests/stelsels"

STELSELS = ("zelfstandige_woonruimten", "onzelfstandige_woonruimten")

STUB_CONTEXT = """# {naam}

## Doel
TODO: beschrijf wat deze testcase test.

## Beleidsbron
- Implementatietoelichting: TODO
- Beleidsboek (quote): TODO

## Handmatige berekening
(optioneel)

## Opmerkingen
(optioneel)
"""


def _case_dir_for_stelsel_input(stelsel: str, case_name: str) -> Path:
    return NEW_STELSELS / stelsel / "eenheden" / case_name


def _case_dir_for_stelselgroep_input(
    stelsel: str, stelselgroep: str, case_name: str
) -> Path:
    return NEW_STELSELS / stelsel / stelselgroep / case_name


def _migrate_case_files(
    case_dir: Path,
    case_name: str,
    input_path: Path,
    output_dir: Path | None,
    input_dir: Path | None,
) -> None:
    case_dir.mkdir(parents=True, exist_ok=True)

    shutil.copy2(input_path, case_dir / "input.json")

    if output_dir and (output_dir / f"{case_name}.json").exists():
        shutil.copy2(output_dir / f"{case_name}.json", case_dir / "output.json")
    if output_dir and (output_dir / f"{case_name}.log").exists():
        shutil.copy2(output_dir / f"{case_name}.log", case_dir / "output.log")
    if output_dir and (output_dir / f"{case_name}.txt").exists():
        shutil.copy2(output_dir / f"{case_name}.txt", case_dir / "output.txt")

    context_dest = case_dir / "input_context.md"
    if context_dest.exists():
        return

    md_sources: list[Path] = []
    if input_dir and (input_dir / f"{case_name}.md").exists():
        md_sources.append(input_dir / f"{case_name}.md")
    if output_dir and (output_dir / f"{case_name}.md").exists():
        md_sources.append(output_dir / f"{case_name}.md")

    if md_sources:
        content = md_sources[0].read_text()
        if not content.lstrip().startswith("# "):
            content = f"# {case_name}\n\n{content}"
        context_dest.write_text(content)
    else:
        context_dest.write_text(STUB_CONTEXT.format(naam=case_name))


def _migrate_stelsel_eenheden(stelsel: str, stats: dict[str, int]) -> None:
    input_dir = OLD_DATA / stelsel / "input"
    output_dir = OLD_DATA / stelsel / "output"
    if not input_dir.exists():
        return

    for input_path in sorted(input_dir.glob("*.json")):
        case_name = input_path.stem
        case_dir = _case_dir_for_stelsel_input(stelsel, case_name)
        _migrate_case_files(case_dir, case_name, input_path, output_dir, input_dir)
        stats["eenheden"] += 1


def _migrate_stelselgroep_cases(stelsel: str, stats: dict[str, int]) -> None:
    stelselgroepen_dir = OLD_DATA / stelsel / "stelselgroepen"
    if not stelselgroepen_dir.exists():
        return

    for stelselgroep_dir in sorted(stelselgroepen_dir.iterdir()):
        if not stelselgroep_dir.is_dir():
            continue

        stelselgroep = stelselgroep_dir.name
        input_dir = stelselgroep_dir / "input"
        output_dir = stelselgroep_dir / "output"
        if not input_dir.exists():
            continue

        dest_stelselgroep = NEW_STELSELS / stelsel / stelselgroep
        dest_stelselgroep.mkdir(parents=True, exist_ok=True)

        test_file = (
            stelselgroep_dir / f"test_{_test_module_name(stelselgroep, stelsel)}.py"
        )
        if not test_file.exists():
            for candidate in stelselgroep_dir.glob("test_*.py"):
                test_file = candidate
                break

        if test_file.exists():
            shutil.copy2(test_file, dest_stelselgroep / test_file.name)
            stats["test_files"] += 1

        for input_path in sorted(input_dir.glob("*.json")):
            case_name = input_path.stem
            case_dir = _case_dir_for_stelselgroep_input(
                stelsel, stelselgroep, case_name
            )
            _migrate_case_files(case_dir, case_name, input_path, output_dir, input_dir)
            stats["stelselgroep_cases"] += 1


def _test_module_name(stelselgroep: str, stelsel: str) -> str:
    """Fallback; echte bestandsnaam wordt via glob opgepikt."""
    words = stelselgroep.replace("_", " ").title().replace(" ", "")
    if stelsel == "onzelfstandige_woonruimten" and not words.endswith("Onz"):
        return f"{words}Onz"
    return words


def _migrate_generiek(stats: dict[str, int]) -> None:
    generiek_input = OLD_DATA / "generiek" / "input" / "37101000032.json"
    if not generiek_input.exists():
        return

    case_dir = _case_dir_for_stelsel_input("zelfstandige_woonruimten", "37101000032")
    if not (case_dir / "input.json").exists():
        case_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(generiek_input, case_dir / "input.json")
        stats["generiek"] += 1

    context = case_dir / "input_context.md"
    if not context.exists():
        context.write_text(
            """# 37101000032

## Doel
Canonieke demo-eenheid voor documentatie, doc-tests en `context.waardeer`-voorbeelden.

## Beleidsbron
- Implementatietoelichting: TODO
- Beleidsboek (quote): n.v.t. (integratievoorbeeld)

## Opmerkingen
Samengevoegd uit `tests/data/generiek/` en `tests/data/zelfstandige_woonruimten/input/`.
"""
        )

    smoke_test = OLD_DATA / "generiek" / "test_Woningwaardering.py"
    if smoke_test.exists():
        shutil.copy2(smoke_test, ROOT / "tests" / "test_Woningwaardering.py")
        stats["smoke_test"] += 1


def _update_warning_paths_in_test_files() -> int:
    updated = 0
    for test_file in NEW_STELSELS.rglob("test_*.py"):
        content = test_file.read_text()
        new_content = re.sub(
            r'file=f"\{current_file_path\}/input/([^"]+)\.json"',
            r'file=f"{current_file_path}/\1/input.json"',
            content,
        )
        if new_content != content:
            test_file.write_text(new_content)
            updated += 1
    return updated


def main() -> int:
    stats: dict[str, int] = {
        "eenheden": 0,
        "stelselgroep_cases": 0,
        "generiek": 0,
        "test_files": 0,
        "smoke_test": 0,
        "warning_paths": 0,
    }

    NEW_STELSELS.mkdir(parents=True, exist_ok=True)

    for stelsel in STELSELS:
        _migrate_stelsel_eenheden(stelsel, stats)
        _migrate_stelselgroep_cases(stelsel, stats)

    _migrate_generiek(stats)
    stats["warning_paths"] = _update_warning_paths_in_test_files()

    print("Migratie voltooid:")
    for key, value in stats.items():
        print(f"  {key}: {value}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
