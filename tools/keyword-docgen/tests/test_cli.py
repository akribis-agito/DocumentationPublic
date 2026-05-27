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
