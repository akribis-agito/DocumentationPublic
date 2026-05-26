"""Render a manifest of keywords present in the scan but missing a doc."""

from __future__ import annotations

from .model import PRODUCTS


def render_manifest(
    scanned: dict[str, set[str]], documented: set[str], version: str
) -> str:
    """Return a markdown manifest listing undocumented keywords.

    `scanned` maps product -> set of mnemonics found in that product's table.
    `documented` is the set of mnemonics that already have a doc file.
    """
    all_scanned: set[str] = set()
    for names in scanned.values():
        all_scanned |= names
    undocumented = sorted(all_scanned - documented)

    lines = [
        "# Undocumented keywords",
        "",
        f"Generated from the {version} scan. Each keyword below exists in "
        "`Params.c` but has no doc file yet.",
        "",
        "| Keyword | Products | First seen |",
        "| --- | --- | --- |",
    ]
    for name in undocumented:
        products = ", ".join(p for p in PRODUCTS if name in scanned.get(p, set()))
        lines.append(f"| {name} | {products} | {version} |")
    return "\n".join(lines) + "\n"
