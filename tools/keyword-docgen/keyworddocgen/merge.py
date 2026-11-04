"""Merge a v5 scan's per-product-type facts into a doc's frontmatter (schema v2)."""

from __future__ import annotations

from .model import PRIMARY_PRODUCT_TYPE, PRODUCT_TYPES


class FactsAlreadyRecorded(Exception):
    """Raised by append when the doc already carries generated facts."""


_FLOAT_TYPE_LIMIT = 1.0e38
# Generated keys of the v1 schema (version axis, standalone/central-i cells).
_V1_ONLY_KEYS = ("removed_in",)


def _is_finite(value) -> bool:
    """True for a real numeric range/default we should not lose — excludes None
    and the float-type-limit sentinels (+/-3.4e38, +/-1e38 on C2000), which mean 'unbounded'."""
    if value is None:
        return False
    nums = value if isinstance(value, list) else [value]
    return all(
        isinstance(n, (int, float)) and abs(n) < _FLOAT_TYPE_LIMIT for n in nums
    )


def _reconstruct_cells(fm: dict) -> dict[str, dict]:
    """Rebuild {product type: attrs} from schema-v2 primary attributes plus
    overrides. A v1 page (availability keyed by product, values are versions)
    yields nothing: its v4 facts are never carried into a v5 cell."""
    availability = fm.get("availability")
    if not isinstance(availability, list):
        return {}
    primary_attrs = fm.get("attributes") or {}
    overrides = fm.get("overrides") or {}
    cells: dict[str, dict] = {}
    for ptype in availability:
        attrs = dict(primary_attrs)
        attrs.update({k: v for k, v in (overrides.get(ptype) or {}).items() if k != "can_code"})
        cells[ptype] = attrs
    return cells


def merge_scan(fm: dict, scan_cells: dict, mode: str) -> dict:
    """Return a new frontmatter dict carrying the scan's facts.

    `scan_cells` maps product type -> {"can_code", "attributes", "products",
    "product_overrides"} or None when the keyword is absent from that type. `mode` is "append" (errors
    if the doc already carries generated facts) or "overwrite".
    """
    fm = dict(fm or {})
    if mode == "append" and "availability" in fm:
        raise FactsAlreadyRecorded()
    prior = _reconstruct_cells(fm)

    cells: dict[str, dict] = {}
    for ptype in PRODUCT_TYPES:
        cell = scan_cells.get(ptype)
        if cell is None:
            continue
        attrs = dict(cell["attributes"])
        # No-regression guard: a re-scan that can no longer resolve a numeric
        # range/default (e.g. a constant moved from #define to enum) must not
        # downgrade a previously-known value of the same product type to null.
        for field in ("range", "default"):
            if attrs.get(field) is None and _is_finite(prior.get(ptype, {}).get(field)):
                attrs[field] = prior[ptype][field]
        cells[ptype] = {"attrs": attrs, "can_code": cell["can_code"],
                        "products": list(cell.get("products") or []),
                        "product_overrides": dict(cell.get("product_overrides") or {})}
    if not cells:
        raise ValueError(f"{fm.get('keyword')}: absent from every product type")

    primary_type = PRIMARY_PRODUCT_TYPE if PRIMARY_PRODUCT_TYPE in cells else next(iter(cells))
    primary = cells[primary_type]
    generated = {
        "can_code": primary["can_code"],
        "availability": list(cells),
        "attributes": primary["attrs"],
        "overrides": _compute_overrides(cells, primary_type),
    }
    products = sorted({pid for cell in cells.values() for pid in cell["products"]})
    result: dict = {}
    for key, value in fm.items():
        if key in _V1_ONLY_KEYS or key == "products":
            continue
        result[key] = generated.pop(key, value)
        if key == "availability" and products:
            result["products"] = products
    for key, value in generated.items():
        result[key] = value
        if key == "availability" and products:
            result["products"] = products
    return result


def _compute_overrides(cells: dict[str, dict], primary_type: str) -> dict:
    """Deltas from the primary cell per product type, then deltas from its type's
    cell per product (keyed by catalog ID), covering both attributes and can_code."""
    primary = cells[primary_type]
    overrides: dict[str, dict] = {}
    for ptype, cell in cells.items():
        if ptype == primary_type:
            continue
        diff = {k: v for k, v in cell["attrs"].items() if v != primary["attrs"].get(k)}
        if cell["can_code"] != primary["can_code"]:
            diff["can_code"] = cell["can_code"]
        if diff:
            overrides[ptype] = diff
    for cell in cells.values():
        overrides.update(cell["product_overrides"])
    return overrides
