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


def product_supported(product: str, version: str) -> bool:
    """Whether a (product, version) combination is a supported/shipped product.

    v5 moved the controller to 64-bit calculations and dropped the standalone
    product; v5 is central-i only. The develop branch still *compiles* a
    standalone (CONTROLLER) keyword table, but it is not a supported product, so
    the generator must not record standalone availability on a v5 scan.
    """
    if version == "v5" and product == "standalone":
        return False
    return True


def infer_data_type(record: dict) -> str:
    """Numeric type of a keyword.

    The LTS source encodes every keyword as 32-bit long, so we return int32.
    This is the single extension point for develop-branch float32/int64/float64
    encoding once it is confirmed (see spec risks).
    """
    return "int32"
