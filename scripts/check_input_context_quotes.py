#!/usr/bin/env python3
"""Valideer Beleidsboek-quotes in input_context.md (zelfde regels als pytest)."""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tests"))
from test_test_context import (  # noqa: E402
    STELSELS_DIR,
    _normalize_beleids_text,
    _normalize_quote_segment,
    _parse_quote_blocks,
    _primary_implementatietoelichting,
    _section_text_for_anchor,
)


def check_case(rel: str) -> list[str]:
    case_dir = STELSELS_DIR / rel
    context_path = case_dir / "input_context.md"
    errors: list[str] = []
    if not context_path.exists():
        return [f"missing {context_path}"]
    content = context_path.read_text()
    blocks = _parse_quote_blocks(content)
    if not blocks:
        errors.append("geen quote-blok")
    if any(not b for b in blocks):
        errors.append("leeg quote-blok")
    primary = _primary_implementatietoelichting(content, context_path)
    if not primary or not primary[1]:
        errors.append("geen implementatietoelichting-link met anker")
        return errors
    target, anchor = primary
    section = _section_text_for_anchor(target, anchor)
    if section is None:
        errors.append(f"sectie {anchor} niet gevonden")
        return errors
    norm = _normalize_beleids_text(section)
    for block in blocks:
        search_from = 0
        for segment in block:
            ns = _normalize_quote_segment(segment)
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
