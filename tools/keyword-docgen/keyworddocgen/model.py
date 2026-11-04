"""Shared constants for product types and data types."""

from __future__ import annotations

# Firmware product types (#18): CONTROLLER -> controller, CI_MASTER -> ci-master.
PRODUCT_TYPES = ["controller", "ci-master"]
PRIMARY_PRODUCT_TYPE = "controller"

_DATA_TYPE_ALIASES = {"float": "float32", "double": "float64"}


def normalise_data_type(value):
    """Map the stray `float` / `double` spellings onto the schema enum."""
    return _DATA_TYPE_ALIASES.get(value, value)
