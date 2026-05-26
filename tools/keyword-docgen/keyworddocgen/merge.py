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
    """Rebuild {(product, version): attributes} from primary + overrides."""
    cells: dict[tuple[str, str], dict] = {}
    primary = fm.get("attributes")
    availability = fm.get("availability", {})
    overrides = fm.get("overrides", {})
    for product in PRODUCTS:
        for version in availability.get(product, []):
            attrs = dict(primary) if primary else {}
            attrs.update(overrides.get(cell_key(product, version), {}))
            cells[(product, version)] = attrs
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
    can_codes = {k: fm.get("can_code") for k in cells}

    # Drop any prior cells for this version, then apply the scan.
    for product in PRODUCTS:
        cells.pop((product, version), None)
        cell = scan_cells.get(product)
        if cell is not None:
            cells[(product, version)] = cell["attributes"]
            can_codes[(product, version)] = cell["can_code"]

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
        primary_attrs = cells[primary_cell]
        result["can_code"] = can_codes.get(primary_cell, fm.get("can_code"))
        result["attributes"] = primary_attrs
        result["overrides"] = _compute_overrides(cells, primary_cell, primary_attrs)
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


def _compute_overrides(cells, primary_cell, primary_attrs) -> dict:
    overrides: dict[str, dict] = {}
    for (product, version), attrs in cells.items():
        if (product, version) == primary_cell:
            continue
        diff = {k: v for k, v in attrs.items() if v != primary_attrs.get(k)}
        if diff:
            overrides[cell_key(product, version)] = diff
    return overrides
