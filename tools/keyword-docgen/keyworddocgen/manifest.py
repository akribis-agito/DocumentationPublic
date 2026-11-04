"""Render a manifest of keywords present in the scan but missing a doc."""

from __future__ import annotations

from .model import PRODUCT_TYPES


def render_manifest(scanned: dict[str, set[str]], documented: set[str]) -> str:
    """Return a markdown manifest listing undocumented keywords.

    `scanned` maps product type -> set of mnemonics found in that type's table.
    `documented` is the set of mnemonics that already have a doc file.
    """
    all_scanned: set[str] = set()
    for names in scanned.values():
        all_scanned |= names
    undocumented = sorted(all_scanned - documented)

    lines = [
        "# Undocumented keywords",
        "",
        "Generated from the v5 scan. Each keyword below exists in "
        "`Params.c` but has no doc file yet.",
        "",
        "| Keyword | Product types |",
        "| --- | --- |",
    ]
    for name in undocumented:
        types = ", ".join(t for t in PRODUCT_TYPES if name in scanned.get(t, set()))
        lines.append(f"| {name} | {types} |")
    return "\n".join(lines) + "\n"
