from pathlib import Path

import pytest

from keyworddocgen.table_parser import (
    TableError,
    catalog_id,
    collapse_by_product_type,
    hardware_build,
    list_v5_products,
    parse_kw_row_table,
)

FW = Path(__file__).parent / "fixtures" / "v5_firmware"


@pytest.fixture(scope="module")
def per_product():
    return parse_kw_row_table(FW)


def test_lists_products_from_product_config():
    assert list_v5_products(FW) == ["PRODUCT_AGD301_ET_2D05", "PRODUCT_AGD155_EC", "PRODUCT_AGM800"]


def test_catalog_id():
    assert catalog_id("PRODUCT_AGD155_EC") == "agd155-ec"


def test_product_type_and_keyword_set_per_product(per_product):
    assert {pid: p["product_type"] for pid, p in per_product.items()} == {
        "agd301-et-2d05": "controller", "agd155-ec": "controller", "agm800": "ci-master"}
    assert {pid: p["build"] for pid, p in per_product.items()} == {
        "agd301-et-2d05": "c2000", "agd155-ec": "c28388", "agm800": "zynq"}
    common = {"Pos", "PosGain", "CurrLim", "DInPort", "GenDataD"}
    assert set(per_product["agd301-et-2d05"]["keywords"]) == common | {"RptCount"}
    # KW_ROW_EC needs the EtherCAT CM and a C28388 or Zynq build.
    assert set(per_product["agd155-ec"]["keywords"]) == common | {"RptCount", "Display7Seg", "ECATSend"}
    assert set(per_product["agm800"]["keywords"]) == common | {"PhaseVoltage"}


def test_hardware_build_per_product():
    assert hardware_build("PRODUCT_AGM800_EC") == "zynq"
    assert hardware_build("PRODUCT_AGD101_EC_17A") == "c28388"
    assert hardware_build("PRODUCT_AGD200_ET_2D01") == "c2000"


def test_sim_build_stubs_the_ethercat_rows():
    sim = parse_kw_row_table(FW, products=["PRODUCT_AGD155_EC"], build="pc")["agd155-ec"]
    assert sim["build"] == "pc"
    assert "ECATSend" not in sim["keywords"] and "Display7Seg" in sim["keywords"]


def test_double_type_limit_is_unbounded_on_every_build(per_product):
    # +/-1e38 on C2000, +/-1e308 elsewhere: both mean "any value".
    assert per_product["agd301-et-2d05"]["keywords"]["GenDataD"]["attributes"]["range"] is None
    assert per_product["agm800"]["keywords"]["GenDataD"]["attributes"]["range"] is None


def test_can_code_is_the_row_position(per_product):
    kws = per_product["agm800"]["keywords"]
    assert kws["Pos"]["can_code"] == 1
    assert kws["PhaseVoltage"]["can_code"] == 5


def test_width_and_scope_macros_follow_the_product(per_product):
    ctl = per_product["agd301-et-2d05"]["keywords"]
    cim = per_product["agm800"]["keywords"]
    assert ctl["Pos"]["attributes"]["data_type"] == "int32"     # CW_TYPETAG_POS = LONG32
    assert cim["Pos"]["attributes"]["data_type"] == "int64"     # CW_TYPETAG_POS = LONG64
    assert ctl["DInPort"]["attributes"]["scope"] == "non-axis"  # AXIS_CIM
    assert cim["DInPort"]["attributes"]["scope"] == "axis"


def test_row_attributes_and_pooled_values(per_product):
    a = per_product["agd301-et-2d05"]["keywords"]["PosGain"]["attributes"]
    assert a == {
        "access": "rw", "scope": "axis", "flash": True, "type": "array", "array_size": 6,
        "data_type": "int32", "ok_in_motion": True, "ok_motor_on": True, "units": "none",
        "range": [0, 4095], "default": 20.0, "scaling": 1.0, "implemented": "final",
    }
    pos = per_product["agd301-et-2d05"]["keywords"]["Pos"]["attributes"]
    assert pos["access"] == "ro" and pos["ok_motor_on"] is False and pos["units"] == "user"
    assert pos["range"] == [-2251799813685247, 2251799813685247]
    assert pos["scaling"] == 1.024
    # FUNC_UNITS expands to 0 like NO_USER_UNITS; the raw row token tells them apart.
    assert per_product["agm800"]["keywords"]["DInPort"]["attributes"]["units"] == "func"
    # Bounds follow each product's own configuration.
    assert per_product["agd155-ec"]["keywords"]["CurrLim"]["attributes"]["range"] == [-8000000, 8000000]


def test_collapse_by_product_type(per_product):
    cells = collapse_by_product_type(per_product)
    assert set(cells) == {"controller", "ci-master"}
    ctl, cim = cells["controller"], cells["ci-master"]
    assert set(ctl) == {"Pos", "PosGain", "CurrLim", "DInPort", "GenDataD", "RptCount", "Display7Seg", "ECATSend"}
    assert set(cim) == {"Pos", "PosGain", "CurrLim", "DInPort", "GenDataD", "PhaseVoltage"}
    assert ctl["Display7Seg"]["products"] == ["agd155-ec"]   # KW_ROW_7SEG
    assert ctl["ECATSend"]["products"] == ["agd155-ec"]      # KW_ROW_EC
    assert ctl["Pos"]["products"] == []                      # every controller
    assert cim["PhaseVoltage"]["products"] == []             # KW_ROW_CIM_ONLY: every ci-master
    assert "PhaseVoltage" not in ctl and "RptCount" not in cim
    # Facts come from the reference product (agd301-et-2d05), not agd155-ec.
    assert ctl["CurrLim"]["attributes"]["range"] == [-16000000, 16000000]


def test_missing_product_config_raises(tmp_path):
    (tmp_path / "CommonC").mkdir()
    (tmp_path / "CommonC" / "AG300_CTL01Params.c").write_text("")
    (tmp_path / "CommonIncludes").mkdir()
    (tmp_path / "CommonIncludes" / "ProductConfig.h").write_text("// no products\n")
    with pytest.raises(TableError):
        parse_kw_row_table(tmp_path)


def test_collapse_records_per_product_differences(per_product):
    cells = collapse_by_product_type(per_product)
    # The cell carries the reference product's bound; agd155-ec's own is kept per product.
    assert cells["controller"]["CurrLim"]["product_overrides"] == {"agd155-ec": {"range": [-8000000, 8000000]}}
    assert cells["controller"]["Pos"]["product_overrides"] == {}
    assert cells["ci-master"]["CurrLim"]["product_overrides"] == {}
