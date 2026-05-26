"""Merge a scanned version's facts into a doc's frontmatter."""

from __future__ import annotations

from .model import (
    PRODUCTS,
    PRIMARY_PRODUCT,
    cell_key,
    latest_version,
    version_rank,
)


class VersionAlreadyRecorded(Exception):
    """Raised by append when the version is already present in the doc."""


def _reconstruct_cells(fm: dict) -> dict[tuple[str, str], dict]:
    """Rebuild {(product, version): {"attrs": {...}, "can_code": int}} from the
    primary attributes/can_code plus per-cell overrides. `can_code` may appear
    inside an override entry (it can differ by version)."""
    cells: dict[tuple[str, str], dict] = {}
    primary_attrs = fm.get("attributes") or {}
    top_can = fm.get("can_code")
    availability = fm.get("availability", {})
    overrides = fm.get("overrides", {})
    for product in PRODUCTS:
        for version in availability.get(product, []):
            ov = dict(overrides.get(cell_key(product, version), {}))
            can_code = ov.pop("can_code", top_can)
            attrs = dict(primary_attrs)
            attrs.update(ov)
            cells[(product, version)] = {"attrs": attrs, "can_code": can_code}
    return cells


def _recorded_versions(fm: dict) -> set[str]:
    versions: set[str] = set()
    for vs in fm.get("availability", {}).values():
        versions.update(vs)
    return versions


def merge_version(fm: dict, scan_cells: dict, version: str, mode: str) -> dict:
    """Return a new frontmatter dict with `version`'s facts merged in.

    `scan_cells` maps product -> {"can_code", "attributes"} or None if absent.
    `mode` is "append" (errors if version already present) or "overwrite".
    """
    fm = dict(fm or {})
    if mode == "append" and version in _recorded_versions(fm):
        raise VersionAlreadyRecorded(version)

    cells = _reconstruct_cells(fm)

    # Drop any prior cells for this version, then apply the scan.
    for product in PRODUCTS:
        cells.pop((product, version), None)
        cell = scan_cells.get(product)
        if cell is not None:
            cells[(product, version)] = {
                "attrs": cell["attributes"],
                "can_code": cell["can_code"],
            }

    # removed_in: a version we scanned but where the keyword is now absent,
    # while older cells still exist.
    removed_in = set(fm.get("removed_in", []))
    removed_in.discard(version)
    scanned_absent = all(scan_cells.get(p) is None for p in PRODUCTS)
    if scanned_absent and cells:
        removed_in.add(version)

    availability = {
        product: sorted(
            [v for (p, v) in cells if p == product], key=version_rank
        )
        for product in PRODUCTS
    }

    primary_cell = _pick_primary(cells)
    result = dict(fm)
    result["availability"] = availability
    if primary_cell is not None:
        primary = cells[primary_cell]
        result["can_code"] = primary["can_code"]
        result["attributes"] = primary["attrs"]
        result["overrides"] = _compute_overrides(cells, primary_cell)
    if removed_in:
        result["removed_in"] = sorted(removed_in, key=version_rank)
    else:
        result.pop("removed_in", None)
    return result


def _pick_primary(cells: dict[tuple[str, str], dict]) -> tuple[str, str] | None:
    for product in [PRIMARY_PRODUCT] + [p for p in PRODUCTS if p != PRIMARY_PRODUCT]:
        versions = [v for (p, v) in cells if p == product]
        latest = latest_version(versions)
        if latest is not None:
            return (product, latest)
    return None


def _compute_overrides(cells, primary_cell) -> dict:
    """Per-cell deltas from the primary cell, covering both attributes and
    can_code (which can differ by version)."""
    primary = cells[primary_cell]
    overrides: dict[str, dict] = {}
    for (product, version), cell in cells.items():
        if (product, version) == primary_cell:
            continue
        diff = {
            k: v for k, v in cell["attrs"].items()
            if v != primary["attrs"].get(k)
        }
        if cell["can_code"] != primary["can_code"]:
            diff["can_code"] = cell["can_code"]
        if diff:
            overrides[cell_key(product, version)] = diff
    return overrides
