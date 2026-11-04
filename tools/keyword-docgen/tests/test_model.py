from keyworddocgen.model import (
    PRIMARY_PRODUCT_TYPE,
    PRODUCT_TYPES,
)


def test_constants():
    assert PRODUCT_TYPES == ["controller", "ci-master"]
    assert PRIMARY_PRODUCT_TYPE == "controller"
