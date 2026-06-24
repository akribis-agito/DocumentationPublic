"""Tests for the bilingual zh-CN sidecar: fact propagation that preserves the
translated `summary`, the `language` marker, and the translated body."""

from keyworddocgen.frontmatter import split_doc, render_doc, zh_sidecar_path
from keyworddocgen.frontmatter import propagate_facts_to_sidecar


def _en_facts():
    return {
        "keyword": "PosGain",
        "summary": "Proportional position gain.",
        "availability": {"standalone": ["v4"], "central-i": ["v4", "v5"]},
        "can_code": 100,
        "attributes": {"access": "rw", "range": [0, 20000], "default": 0},
        "overrides": {},
    }


# --- path helper ---------------------------------------------------------

def test_zh_sidecar_path(tmp_path):
    en = tmp_path / "02-keywords" / "PosGain.md"
    assert zh_sidecar_path(en) == tmp_path / "02-keywords" / "PosGain.zh.md"


def test_zh_sidecar_path_only_strips_final_md(tmp_path):
    # Idempotent-ish: stem is the keyword, suffix is swapped for .zh.md.
    en = tmp_path / "AutoExec.md"
    assert zh_sidecar_path(en).name == "AutoExec.zh.md"


# --- propagation: no sidecar -> no-op ------------------------------------

def test_no_sidecar_does_nothing(tmp_path):
    en = tmp_path / "PosGain.md"
    en.write_text(render_doc(_en_facts(), "# PosGain\n\nbody\n"))
    changed = propagate_facts_to_sidecar(en, _en_facts())
    assert changed is False
    # No empty sidecar created.
    assert not (tmp_path / "PosGain.zh.md").exists()


# --- propagation: existing sidecar preserves prose -----------------------

def test_propagation_preserves_summary_language_and_body(tmp_path):
    en = tmp_path / "PosGain.md"
    en.write_text(render_doc(_en_facts(), "# PosGain\n\nEnglish body\n"))

    zh_fm = {
        "keyword": "PosGain",
        "language": "zh-CN",
        "summary": "比例位置增益。",   # translated summary
        "availability": {"standalone": ["v4"], "central-i": ["v4"]},  # STALE facts
        "can_code": 999,                                              # STALE
        "attributes": {"access": "ro"},                               # STALE
    }
    zh = tmp_path / "PosGain.zh.md"
    zh_body = "# PosGain\n\n中文正文\n"               # translated body
    zh.write_text(render_doc(zh_fm, zh_body))

    changed = propagate_facts_to_sidecar(en, _en_facts())
    assert changed is True

    new_fm, new_body = split_doc(zh.read_text())
    # Facts now match English exactly.
    assert new_fm["can_code"] == 100
    assert new_fm["attributes"] == {"access": "rw", "range": [0, 20000], "default": 0}
    assert new_fm["availability"] == {"standalone": ["v4"], "central-i": ["v4", "v5"]}
    # Translated prose preserved.
    assert new_fm["language"] == "zh-CN"
    assert new_fm["summary"] == "比例位置增益。"
    assert new_body == zh_body


def test_propagation_defaults_language_when_missing(tmp_path):
    # A sidecar that somehow lacks `language` gets zh-CN (it IS the zh file).
    en = tmp_path / "PosGain.md"
    en.write_text(render_doc(_en_facts(), "# PosGain\n\nEnglish body\n"))
    zh = tmp_path / "PosGain.zh.md"
    zh.write_text(render_doc(
        {"keyword": "PosGain", "summary": "译文"}, "身体\n"))

    propagate_facts_to_sidecar(en, _en_facts())
    new_fm, _ = split_doc(zh.read_text())
    assert new_fm["language"] == "zh-CN"
    assert new_fm["summary"] == "译文"


def test_propagation_never_overwrites_summary_with_english(tmp_path):
    en = tmp_path / "PosGain.md"
    en.write_text(render_doc(_en_facts(), "# PosGain\n\nbody\n"))
    zh = tmp_path / "PosGain.zh.md"
    zh.write_text(render_doc(
        {"keyword": "PosGain", "language": "zh-CN", "summary": "译文"},
        "身体\n"))
    propagate_facts_to_sidecar(en, _en_facts())
    new_fm, _ = split_doc(zh.read_text())
    assert new_fm["summary"] != "Proportional position gain."
    assert new_fm["summary"] == "译文"
