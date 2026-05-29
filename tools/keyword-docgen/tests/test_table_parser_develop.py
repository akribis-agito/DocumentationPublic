from pathlib import Path

from keyworddocgen.defines import DefineTable
from keyworddocgen.table_parser import parse_params

FIX = Path(__file__).parent / "fixtures"


def parse():
    defines = DefineTable.from_headers([FIX / "defs.h"])
    return parse_params(FIX / "params_sample_develop.c", defines)


def test_parses_develop_format_two_products():
    t = parse()
    assert set(t) == {"standalone", "central-i"}
    assert set(t["standalone"]) == {"PosGain", "PosKi", "AInPort", "CompFiltFreq", "VqFFW"}


def test_develop_posgain_attributes_and_int64_datatype():
    pg = parse()["standalone"]["PosGain"]
    assert pg["can_code"] == 100
    a = pg["attributes"]
    assert a["access"] == "rw"
    assert a["scope"] == "axis"
    assert a["flash"] is True
    assert a["type"] == "array"
    assert a["array_size"] == 6
    assert a["ok_in_motion"] is True
    assert a["range"] == [0, 20000]
    assert a["default"] == 0
    assert a["implemented"] == "final"
    assert a["data_type"] == "int64"      # LONG64


def test_develop_datatype_tokens():
    sa = parse()["standalone"]
    assert sa["PosKi"]["attributes"]["data_type"] == "int32"    # 0
    assert sa["AInPort"]["attributes"]["data_type"] == "float32"  # FLOAT


def test_develop_skips_sentinel():
    assert "ZZZZ" not in parse()["standalone"]


def test_develop_float_range_default_and_scaling():
    # specific float min/max/default resolve; float scaling macro resolves
    a = parse()["standalone"]["CompFiltFreq"]["attributes"]
    assert a["data_type"] == "float32"
    assert a["range"] == [1.0, 1000.0]
    assert a["default"] == 200.0
    assert a["scaling"] == 1.526


def test_develop_float_type_sentinel_range_is_null():
    # FLOAT_MIN/FLOAT_MAX is the float-type limit, not a real bound -> unbounded
    a = parse()["standalone"]["VqFFW"]["attributes"]
    assert a["range"] is None
    assert a["scaling"] == 1.526
