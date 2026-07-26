#!/usr/bin/env python3
"""Valideer Beleidsboek-quotes in input_context.md (zelfde regels als pytest)."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType

REPO = Path(__file__).resolve().parent.parent


def _load_test_module() -> ModuleType:
    path = REPO / "tests" / "test_test_context.py"
    spec = importlib.util.spec_from_file_location("test_test_context", path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Kan {path} niet laden")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_ctx = _load_test_module()


def check_case(rel: str) -> list[str]:
    case_dir = _ctx.STELSELS_DIR / rel
    context_path = case_dir / "input_context.md"
    errors: list[str] = []
    if not context_path.exists():
        return [f"missing {context_path}"]
    content = context_path.read_text()
    if _ctx.MAXIMALE_HUUR.search(content):
        errors.append("maximale huur genoemd")
    eenheidtest = _ctx._is_eenheidtest(case_dir)
    blocks = _ctx._parse_quote_blocks(content)
    if eenheidtest and not blocks:
        return errors
    if not blocks:
        errors.append("geen quote-blok")
    if any(not b for b in blocks):
        errors.append("leeg quote-blok")
    primary = _ctx._primary_implementatietoelichting(content, context_path)
    if not primary or not primary[1]:
        errors.append("geen implementatietoelichting-link met anker")
        return errors
    target, anchor = primary
    section = _ctx._section_text_for_anchor(target, anchor)
    if section is None:
        errors.append(f"sectie {anchor} niet gevonden")
        return errors
    norm = _ctx._normalize_beleids_text(section)
    for block in blocks:
        search_from = 0
        for segment in block:
            ns = _ctx._normalize_quote_segment(segment)
            pos = norm.find(ns, search_from)
            if pos == -1:
                errors.append(f"segment niet gevonden (volgorde): {segment!r}")
                break
            search_from = pos + len(ns)
    return errors


def main() -> int:
    rels = sys.argv[1:]
    if not rels:
        print("usage: check_input_context_quotes.py <rel_case>...", file=sys.stderr)
        return 2
    failed = 0
    for rel in rels:
        errs = check_case(rel)
        if errs:
            failed += 1
            print(f"FAIL {rel}")
            for e in errs:
                print(f"  {e}")
        else:
            print(f"OK   {rel}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
