from keyworddocgen.model import (
    PRIMARY_PRODUCT_TYPE,
    PRODUCT_TYPES,
    normalise_data_type,
)


def test_constants():
    assert PRODUCT_TYPES == ["controller", "ci-master"]
    assert PRIMARY_PRODUCT_TYPE == "controller"


def test_normalise_data_type():
    assert normalise_data_type("float") == "float32"
    assert normalise_data_type("double") == "float64"
    assert normalise_data_type("int64") == "int64"
