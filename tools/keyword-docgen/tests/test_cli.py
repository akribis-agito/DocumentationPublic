from pathlib import Path

from keyworddocgen.cli import run
from keyworddocgen.frontmatter import split_doc

FIX = Path(__file__).parent / "fixtures"


def setup_docs(tmp_path: Path) -> Path:
    docs = tmp_path / "docs"
    kw = docs / "02-keywords" / "11-control-tuning"
    kw.mkdir(parents=True)
    # Only PosGain has a doc; PosKi will land in the manifest.
    (kw / "PosGain.md").write_text(
        "---\nsummary: Proportional gain.\n---\n# PosGain\n\nProportional gain.\n"
    )
    return docs


def run_v4(docs, mode="append"):
    return run([
        mode, "--version", "v4",
        "--params", str(FIX / "params_sample.c"),
        "--defines", str(FIX / "defs.h"),
        "--docs-root", str(docs),
        "--manifest", str(docs / "_manifest" / "undocumented.md"),
    ])


def run_v5(docs, mode="append"):
    return run([
        mode, "--version", "v5",
        "--params", str(FIX / "params_sample_develop.c"),
        "--defines", str(FIX / "defs.h"),
        "--docs-root", str(docs),
        "--manifest", str(docs / "_manifest" / "undocumented.md"),
    ])


def test_v5_scan_does_not_record_standalone(tmp_path):
    # v5 is central-i only: a v5 scan must not add standalone availability,
    # even though the develop source still has a CONTROLLER (standalone) table.
    docs = setup_docs(tmp_path)
    run_v4(docs)
    run_v5(docs)
    fm, _ = split_doc((docs / "02-keywords/11-control-tuning/PosGain.md").read_text())
    assert fm["availability"]["standalone"] == ["v4"]          # no v5 for standalone
    assert fm["availability"]["central-i"] == ["v4", "v5"]      # central-i gains v5


def test_updates_existing_doc_frontmatter(tmp_path):
    docs = setup_docs(tmp_path)
    run_v4(docs)
    fm, body = split_doc((docs / "02-keywords/11-control-tuning/PosGain.md").read_text())
    assert fm["can_code"] == 100
    assert fm["attributes"]["range"] == [0, 20000]
    assert fm["availability"]["standalone"] == ["v4"]
    assert fm["summary"] == "Proportional gain."        # preserved
    assert "Proportional gain." in body                  # body preserved


def test_does_not_create_doc_for_undocumented_keyword(tmp_path):
    docs = setup_docs(tmp_path)
    run_v4(docs)
    assert not (docs / "02-keywords/11-control-tuning/PosKi.md").exists()


def test_writes_manifest_with_undocumented(tmp_path):
    docs = setup_docs(tmp_path)
    run_v4(docs)
    manifest = (docs / "_manifest" / "undocumented.md").read_text()
    assert "PosKi" in manifest
    assert "PosGain" not in manifest


def test_append_twice_same_version_errors(tmp_path, capsys):
    docs = setup_docs(tmp_path)
    run_v4(docs)
    rc = run_v4(docs)                # second append of v4
    assert rc != 0
    assert "already recorded" in capsys.readouterr().err.lower()


def test_overwrite_twice_is_idempotent(tmp_path):
    docs = setup_docs(tmp_path)
    run_v4(docs, mode="append")
    rc = run_v4(docs, mode="overwrite")
    assert rc == 0


def test_indexes_special_features_and_legacy_roots(tmp_path):
    # Keyword pages that live OUTSIDE 02-keywords (legacy, no frontmatter) must
    # still be discovered and receive generated frontmatter.
    docs = tmp_path / "docs"
    sf = docs / "03-special-features" / "auto-gain"
    lg = docs / "05-legacy-keywords"
    sf.mkdir(parents=True)
    lg.mkdir(parents=True)
    (sf / "PosGain.md").write_text("# PosGain\n\nlegacy body A\n")   # no frontmatter
    (lg / "PosKi.md").write_text("# PosKi\n\nlegacy body B\n")        # no frontmatter

    run_v4(docs)

    fm_pg, body_pg = split_doc((sf / "PosGain.md").read_text())
    assert fm_pg["can_code"] == 100
    assert fm_pg["availability"]["standalone"] == ["v4"]
    assert "legacy body A" in body_pg          # body preserved
    fm_pk, body_pk = split_doc((lg / "PosKi.md").read_text())
    assert fm_pk.get("can_code") is not None   # PosKi also onboarded
    assert "legacy body B" in body_pk


def test_index_prefers_canonical_entry_on_stem_collision(tmp_path):
    # Same mnemonic in two places: a cross-ref stub (no `keyword:` field) that
    # sorts FIRST, and the canonical entry (has `keyword:`) that sorts later.
    # The generator must target the canonical one and never clobber the stub —
    # so the rule must beat plain sort order.
    # Mirror the real JerkMode case: canonical sorts FIRST, stub LATER, so a
    # naive last-wins index would wrongly target the stub.
    docs = tmp_path / "docs"
    canon_dir = docs / "02-keywords" / "01-aaa"         # sorts first
    stub_dir = docs / "02-keywords" / "02-bbb"          # sorts later
    stub_dir.mkdir(parents=True)
    canon_dir.mkdir(parents=True)
    (stub_dir / "PosGain.md").write_text(
        "---\nsummary: see the primary entry.\n---\n# PosGain\n\nstub pointer\n"
    )
    (canon_dir / "PosGain.md").write_text(
        "---\nkeyword: PosGain\nsummary: canonical.\n---\n# PosGain\n\ncanonical body\n"
    )

    run_v4(docs)

    fm_c, _ = split_doc((canon_dir / "PosGain.md").read_text())
    assert fm_c["can_code"] == 100                       # canonical got facts
    fm_s, body_s = split_doc((stub_dir / "PosGain.md").read_text())
    assert "can_code" not in fm_s                        # stub untouched
    assert fm_s["summary"] == "see the primary entry."
    assert "stub pointer" in body_s


def test_append_propagates_facts_into_zh_sidecar(tmp_path):
    # An existing .zh.md sidecar gets the same generated facts, while its
    # translated summary and body are preserved. No new sidecar is created for
    # docs that lack one.
    docs = setup_docs(tmp_path)
    kw = docs / "02-keywords" / "11-control-tuning"
    (kw / "PosGain.zh.md").write_text(
        "---\nkeyword: PosGain\nlanguage: zh-CN\nsummary: 比例增益。\n---\n"
        "# PosGain\n\n中文正文\n"
    )

    run_v4(docs)

    zh_fm, zh_body = split_doc((kw / "PosGain.zh.md").read_text())
    assert zh_fm["language"] == "zh-CN"
    assert zh_fm["summary"] == "比例增益。"          # translated, preserved
    assert zh_fm["can_code"] == 100                  # generated fact propagated
    assert zh_fm["attributes"]["range"] == [0, 20000]
    assert zh_fm["availability"]["standalone"] == ["v4"]
    assert "中文正文" in zh_body                       # translated body preserved


def test_append_does_not_create_zh_sidecar_when_absent(tmp_path):
    docs = setup_docs(tmp_path)
    run_v4(docs)
    assert not (docs / "02-keywords/11-control-tuning/PosGain.zh.md").exists()


def test_index_skips_underscore_dirs(tmp_path):
    # Scratch/_-prefixed dirs (_triage, _files, _manifest) are never indexed.
    docs = tmp_path / "docs"
    tri = docs / "02-keywords" / "_triage"
    tri.mkdir(parents=True)
    (tri / "PosGain.md").write_text("# scratch\n")   # not a real doc

    run_v4(docs)

    assert (tri / "PosGain.md").read_text() == "# scratch\n"   # untouched
