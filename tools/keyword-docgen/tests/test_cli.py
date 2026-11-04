from pathlib import Path

from keyworddocgen.cli import run
from keyworddocgen.frontmatter import split_doc

FIX = Path(__file__).parent / "fixtures"


def setup_docs(tmp_path: Path) -> Path:
    docs = tmp_path / "docs"
    kw = docs / "02-keywords" / "11-control-tuning"
    kw.mkdir(parents=True)
    # Only PosGain has a doc; the other keywords land in the manifest.
    (kw / "PosGain.md").write_text(
        "---\nsummary: Proportional gain.\n---\n# PosGain\n\nProportional gain.\n"
    )
    return docs


def run_scan(docs, mode="append"):
    return run([
        mode,
        "--firmware-root", str(FIX / "v5_firmware"),
        "--docs-root", str(docs),
        "--manifest", str(docs / "_manifest" / "undocumented.md"),
    ])


def test_updates_existing_doc_frontmatter(tmp_path):
    docs = setup_docs(tmp_path)
    run_scan(docs)
    fm, body = split_doc((docs / "02-keywords/11-control-tuning/PosGain.md").read_text())
    assert fm["can_code"] == 2
    assert fm["attributes"]["range"] == [0, 4095]
    assert fm["availability"] == ["controller", "ci-master"]
    assert fm["summary"] == "Proportional gain."        # preserved
    assert "Proportional gain." in body                  # body preserved


def test_does_not_create_doc_for_undocumented_keyword(tmp_path):
    docs = setup_docs(tmp_path)
    run_scan(docs)
    assert not (docs / "02-keywords/11-control-tuning/CurrLim.md").exists()


def test_writes_manifest_with_undocumented(tmp_path):
    docs = setup_docs(tmp_path)
    run_scan(docs)
    manifest = (docs / "_manifest" / "undocumented.md").read_text()
    assert "| CurrLim | controller, ci-master |" in manifest
    assert "PosGain" not in manifest


def test_append_twice_errors(tmp_path, capsys):
    docs = setup_docs(tmp_path)
    run_scan(docs)
    rc = run_scan(docs)              # second append
    assert rc != 0
    assert "already recorded" in capsys.readouterr().err.lower()


def test_overwrite_twice_is_idempotent(tmp_path):
    docs = setup_docs(tmp_path)
    run_scan(docs, mode="append")
    rc = run_scan(docs, mode="overwrite")
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
    (lg / "CurrLim.md").write_text("# CurrLim\n\nlegacy body B\n")        # no frontmatter

    run_scan(docs)

    fm_pg, body_pg = split_doc((sf / "PosGain.md").read_text())
    assert fm_pg["can_code"] == 2
    assert fm_pg["availability"] == ["controller", "ci-master"]
    assert "legacy body A" in body_pg          # body preserved
    fm_pk, body_pk = split_doc((lg / "CurrLim.md").read_text())
    assert fm_pk.get("can_code") is not None   # CurrLim also onboarded
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

    run_scan(docs)

    fm_c, _ = split_doc((canon_dir / "PosGain.md").read_text())
    assert fm_c["can_code"] == 2                       # canonical got facts
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

    run_scan(docs)

    zh_fm, zh_body = split_doc((kw / "PosGain.zh.md").read_text())
    assert zh_fm["language"] == "zh-CN"
    assert zh_fm["summary"] == "比例增益。"          # translated, preserved
    assert zh_fm["can_code"] == 2                  # generated fact propagated
    assert zh_fm["attributes"]["range"] == [0, 4095]
    assert zh_fm["availability"] == ["controller", "ci-master"]
    assert "中文正文" in zh_body                       # translated body preserved


def test_append_does_not_create_zh_sidecar_when_absent(tmp_path):
    docs = setup_docs(tmp_path)
    run_scan(docs)
    assert not (docs / "02-keywords/11-control-tuning/PosGain.zh.md").exists()


def test_index_skips_underscore_dirs(tmp_path):
    # Scratch/_-prefixed dirs (_triage, _files, _manifest) are never indexed.
    docs = tmp_path / "docs"
    tri = docs / "02-keywords" / "_triage"
    tri.mkdir(parents=True)
    (tri / "PosGain.md").write_text("# scratch\n")   # not a real doc

    run_scan(docs)

    assert (tri / "PosGain.md").read_text() == "# scratch\n"   # untouched


def test_manifest_lists_every_v5_keyword_without_a_page(tmp_path):
    docs = setup_docs(tmp_path)
    assert run_scan(docs) == 0
    manifest = (docs / "_manifest" / "undocumented.md").read_text()
    assert "| PhaseVoltage | ci-master |" in manifest
    assert "| Display7Seg | controller |" in manifest
    assert "| RptCount | controller |" in manifest


def write_page(docs, name, front=""):
    kw = docs / "02-keywords" / "11-control-tuning"
    kw.mkdir(parents=True, exist_ok=True)
    (kw / f"{name}.md").write_text(f"---\n{front}---\n# {name}\n")
    return kw / f"{name}.md"


def test_product_gated_keyword_carries_products(tmp_path):
    docs = tmp_path / "docs"
    page = write_page(docs, "Display7Seg")
    run_scan(docs)
    fm, _ = split_doc(page.read_text())
    assert fm["availability"] == ["controller"]
    assert fm["products"] == ["agd155-ec"]


def test_ci_master_width_is_an_override(tmp_path):
    docs = tmp_path / "docs"
    page = write_page(docs, "Pos")
    run_scan(docs)
    fm, _ = split_doc(page.read_text())
    assert fm["attributes"]["data_type"] == "int32"
    assert fm["overrides"] == {"ci-master": {"data_type": "int64"}}
    assert "products" not in fm


def test_overwrite_replaces_v1_front_matter(tmp_path):
    docs = tmp_path / "docs"
    page = write_page(docs, "PosGain", (
        "keyword: PosGain\nsummary: Gain.\ncan_code: 100\n"
        "availability:\n  standalone: [v4]\n  central-i: [v4, v5]\n"
        "attributes: {range: [0, 20000], default: 7, data_type: float}\n"
        "overrides:\n  central-i.v5: {can_code: 348}\n"
        "removed_in: [v5]\n"
    ))
    assert run_scan(docs, mode="overwrite") == 0
    text = page.read_text()
    fm, _ = split_doc(text)
    assert "v4" not in text and "v5" not in text and "removed_in" not in fm
    assert fm["availability"] == ["controller", "ci-master"]
    assert fm["can_code"] == 2
    assert fm["attributes"]["default"] == 20.0     # v1 values are never carried over
    assert fm["overrides"] == {}
    assert fm["summary"] == "Gain."


def test_overwrite_writes_scanned_data_types_over_stray_spellings(tmp_path):
    # Eleven v1 pages carry `float` / `double`; the scan only emits the schema enum.
    docs = tmp_path / "docs"
    page = write_page(docs, "DInPort", "attributes: {data_type: float}\noverrides:\n  central-i.v5: {data_type: double}\n")
    assert run_scan(docs, mode="overwrite") == 0
    fm, _ = split_doc(page.read_text())
    assert fm["attributes"]["data_type"] == "float32"
    assert "double" not in page.read_text()
