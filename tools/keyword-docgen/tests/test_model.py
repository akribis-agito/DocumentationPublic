from keyworddocgen.model import (
    PRODUCTS,
    PRIMARY_PRODUCT,
    VERSION_ORDER,
    cell_key,
    latest_version,
    infer_data_type,
)


def test_constants():
    assert VERSION_ORDER == ["v4", "v5"]
    assert PRODUCTS == ["standalone", "central-i"]
    assert PRIMARY_PRODUCT == "standalone"


def test_latest_version_picks_highest_rank():
    assert latest_version(["v4", "v5"]) == "v5"
    assert latest_version(["v4"]) == "v4"


def test_latest_version_empty_is_none():
    assert latest_version([]) is None


def test_cell_key_format():
    assert cell_key("standalone", "v4") == "standalone.v4"


def test_infer_data_type_defaults_int32():
    assert infer_data_type({}) == "int32"
