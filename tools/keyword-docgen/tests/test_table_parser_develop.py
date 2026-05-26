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
    assert set(t["standalone"]) == {"PosGain", "PosKi", "AInPort"}


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
