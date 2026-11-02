from pathlib import Path

import pytest

from keyworddocgen.cli import run
from keyworddocgen.frontmatter import split_doc
from keyworddocgen.table_parser import parse_expanded, parse_params
from keyworddocgen.defines import DefineTable


def source(tmp_path, rows=None):
    rows = rows or [
        '{"ZZZZZZZZZZZZZ",{0,0,0,0,0,0,0,0,0,0,0,0},0,0,0,0,1,{0},0}',
        '{"PosGain",{0,0,0,0,1,0,1,1,1,2,0,3},(1<<3)-1,0,20000,0,1,{0},0}',
    ]
    p = tmp_path / "expanded.c"
    p.write_text("KeywordsTableArray[2] = {" + ",".join(rows) + "};", encoding="utf-8")
    return p


def test_physical_index_includes_placeholder_and_numeric_attributes(tmp_path):
    record = parse_expanded(source(tmp_path), 2)["PosGain"]
    assert record["can_code"] == 1
    assert record["attributes"] == dict(access="rw", scope="axis", flash=True,
        type="array", array_size=8, data_type="int64", ok_in_motion=True,
        ok_motor_on=True, units="none", range=[0, 20000], default=0, scaling=1,
        implemented="final")


@pytest.mark.parametrize("fault", ["truncated", "count", "attribute", "bound", "duplicate"])
def test_rejects_incomplete_or_unexpanded_tables(tmp_path, fault):
    p = source(tmp_path)
    text = p.read_text(encoding="utf-8")
    if fault == "truncated": text = text[:-3]
    if fault == "attribute": text = text.replace("{0,0,0,0,1,0", "{0,0,0,RO,1,0")
    if fault == "bound": text = text.replace("(1<<3)-1", "UNKNOWN_SIZE")
    if fault == "duplicate": text = text.replace('"ZZZZZZZZZZZZZ"', '"PosGain"')
    p.write_text(text, encoding="utf-8")
    with pytest.raises(ValueError): parse_expanded(p, 3 if fault == "count" else 2)


def test_macro_input_does_not_silently_emit_empty_manifest(tmp_path):
    p = tmp_path / "raw.c"
    p.write_text('KW_ROW(0, "PosGain", {0})', encoding="utf-8")
    with pytest.raises(ValueError, match="preprocessed"):
        parse_params(p, DefineTable({}))


def test_scaling_tag_and_unknown_factor_are_not_assumed_unit_scaling(tmp_path):
    p = source(tmp_path)
    text = p.read_text(encoding="utf-8").replace('{0,0,0,0,1,0', '{0,0,4,0,1,0')
    text = text.replace('20000,0,1,{0}', '20000,0,UNKNOWN_FACTOR,{0}')
    p.write_text(text, encoding="utf-8")
    attrs = parse_expanded(p, 2)["PosGain"]["attributes"]
    assert attrs["units"] == "scaling"
    assert attrs["scaling"] is None


def test_cli_requires_both_products_before_writing(tmp_path):
    docs = tmp_path / "docs" / "02-keywords"
    docs.mkdir(parents=True)
    page = docs / "PosGain.md"
    page.write_text("# PosGain\n", encoding="utf-8")
    p = source(tmp_path)
    args = ["overwrite", "--version", "v5", "--expected-rows", "2",
            "--expanded-table", f"standalone={p}", "--docs-root", str(docs.parent),
            "--manifest", str(tmp_path / "manifest.md")]
    assert run(args) == 1
    assert page.read_text(encoding="utf-8") == "# PosGain\n"
    assert run(args + ["--expanded-table", f"central-i={p}"]) == 0
    fm, body = split_doc(page.read_text(encoding="utf-8"))
    assert fm["availability"] == {"standalone": ["v5"], "central-i": ["v5"]}
    assert body == "# PosGain\n"
