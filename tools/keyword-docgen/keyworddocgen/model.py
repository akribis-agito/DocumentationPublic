"""Shared constants and helpers for products, versions, and data types."""

from __future__ import annotations

VERSION_ORDER = ["v4", "v5"]
PRODUCTS = ["standalone", "central-i"]
PRIMARY_PRODUCT = "standalone"


def version_rank(version: str) -> int:
    return VERSION_ORDER.index(version)


def latest_version(versions: list[str]) -> str | None:
    if not versions:
        return None
    return max(versions, key=version_rank)


def cell_key(product: str, version: str) -> str:
    return f"{product}.{version}"


def infer_data_type(record: dict) -> str:
    """Numeric type of a keyword.

    The LTS source encodes every keyword as 32-bit long, so we return int32.
    This is the single extension point for develop-branch float32/int64/float64
    encoding once it is confirmed (see spec risks).
    """
    return "int32"
