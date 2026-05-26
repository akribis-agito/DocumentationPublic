from pathlib import Path

from keyworddocgen.defines import DefineTable
from keyworddocgen.table_parser import parse_params

FIX = Path(__file__).parent / "fixtures"


def parse():
    defines = DefineTable.from_headers([FIX / "defs.h"])
    return parse_params(FIX / "params_sample.c", defines)


def test_splits_two_products():
    tables = parse()
    assert set(tables) == {"standalone", "central-i"}


def test_skips_sentinel_zzzz_row():
    assert "ZZZZ" not in parse()["standalone"]


def test_posgain_attributes_standalone():
    pg = parse()["standalone"]["PosGain"]
    assert pg["can_code"] == 100
    a = pg["attributes"]
    assert a["access"] == "rw"
    assert a["scope"] == "axis"
    assert a["flash"] is True
    assert a["type"] == "array"
    assert a["array_size"] == 6          # CONTROL_SIZE-1 -> 5, +1
    assert a["data_type"] == "int32"
    assert a["ok_in_motion"] is True
    assert a["ok_motor_on"] is True
    assert a["units"] == "none"
    assert a["range"] == [0, 20000]
    assert a["default"] == 0
    assert a["scaling"] == 1.0
    assert a["implemented"] == "final"


def test_poski_scalar_non_axis_nomotion():
    pk = parse()["standalone"]["PosKi"]
    a = pk["attributes"]
    assert a["type"] == "scalar"
    assert a["array_size"] == 1
    assert a["scope"] == "non-axis"
    assert a["flash"] is False
    assert a["ok_in_motion"] is False
    assert a["range"] == [0, 1000]


def test_central_i_has_only_posgain():
    assert set(parse()["central-i"]) == {"PosGain"}
