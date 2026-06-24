"""Integration tests for the versioning driver against a real git repo.

No mocks: a tiny throwaway repo is created, committed at a fixed date, and the
driver is run over it. Covers the git last-commit date, frontmatter stamping,
the legacy (no-frontmatter) skip rule, and manifest assembly.
"""

import json
import os
import subprocess

from keyworddocgen.cli import run
from keyworddocgen.frontmatter import split_doc
from keyworddocgen.versioning import last_commit_date, stamp_corpus


def _git(repo, *args, date=None):
    env = dict(os.environ)
    if date:
        env["GIT_AUTHOR_DATE"] = date
        env["GIT_COMMITTER_DATE"] = date
    subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True, env=env,
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )


def _init(repo):
    _git(repo, "init")
    _git(repo, "config", "user.email", "t@example.com")
    _git(repo, "config", "user.name", "Tester")


def test_last_commit_date(tmp_path):
    _init(tmp_path)
    f = tmp_path / "a.md"
    f.write_text("hi\n")
    _git(tmp_path, "add", "a.md")
    _git(tmp_path, "commit", "-m", "x", date="2026-05-20T10:00:00")
    assert last_commit_date(f, tmp_path) == "2026-05-20"


def test_last_commit_date_uncommitted_is_none(tmp_path):
    _init(tmp_path)
    f = tmp_path / "b.md"
    f.write_text("hi\n")  # never committed
    assert last_commit_date(f, tmp_path) is None


def _make_corpus(tmp_path):
    content = tmp_path / "content"
    d1 = content / "02-keywords" / "01-system"
    d2 = content / "03-special-features" / "auto-gain"
    d1.mkdir(parents=True)
    d2.mkdir(parents=True)
    pg = d1 / "PosGain.md"
    pg.write_text(
        "---\n"
        "keyword: PosGain\n"
        "summary: Proportional gain.\n"
        "attributes:\n"
        "  range:\n"
        "  - 0\n"
        "  - 20000\n"
        "overrides: {}\n"
        "---\n"
        "# PosGain\n\nbody text\n"
    )
    ag = d2 / "AutoGOn.md"   # legacy: no frontmatter
    ag.write_text("# AutoGOn\n\nlegacy body\n")
    return content, pg, ag


def test_stamp_corpus_stamps_frontmatter_and_preserves_facts(tmp_path):
    _init(tmp_path)
    content, pg, ag = _make_corpus(tmp_path)
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-m", "init", date="2026-05-20T10:00:00")

    stamp_corpus([pg, ag], repo_root=tmp_path, content_root=content,
                 version="2026.06", generated="2026-06-02")

    fm, body = split_doc(pg.read_text())
    assert fm["last_updated"] == "2026-05-20"
    assert fm["doc_revision"] == "2026.06"
    assert fm["attributes"]["range"] == [0, 20000]   # owned fact preserved
    assert fm["keyword"] == "PosGain"
    assert body == "# PosGain\n\nbody text\n"          # body untouched


def test_stamp_corpus_leaves_legacy_doc_without_frontmatter(tmp_path):
    _init(tmp_path)
    content, pg, ag = _make_corpus(tmp_path)
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-m", "init", date="2026-05-20T10:00:00")

    stamp_corpus([pg, ag], repo_root=tmp_path, content_root=content,
                 version="2026.06", generated="2026-06-02")

    # No frontmatter is injected into a legacy doc.
    assert ag.read_text() == "# AutoGOn\n\nlegacy body\n"


def test_stamp_corpus_manifest(tmp_path):
    _init(tmp_path)
    content, pg, ag = _make_corpus(tmp_path)
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-m", "init", date="2026-05-20T10:00:00")

    manifest = stamp_corpus([pg, ag], repo_root=tmp_path, content_root=content,
                            version="2026.06", generated="2026-06-02")

    assert manifest["document_count"] == 2
    paths = [d["path"] for d in manifest["documents"]]
    assert paths == sorted(paths)                       # stable order
    by_kw = {d["keyword"]: d for d in manifest["documents"]}
    # manifest paths are relative to the content root
    assert by_kw["PosGain"]["path"] == "02-keywords/01-system/PosGain.md"
    assert by_kw["AutoGOn"]["path"] == "03-special-features/auto-gain/AutoGOn.md"
    assert by_kw["AutoGOn"]["last_updated"] == "2026-05-20"
    assert by_kw["AutoGOn"]["doc_revision"] == "2026.06"
    # legacy doc hashes its whole text; frontmatter doc hashes only its body
    import hashlib
    assert by_kw["AutoGOn"]["sha256"] == hashlib.sha256(
        b"# AutoGOn\n\nlegacy body\n").hexdigest()
    assert by_kw["PosGain"]["sha256"] == hashlib.sha256(
        b"# PosGain\n\nbody text\n").hexdigest()


def test_stamp_corpus_incremental_doc_revision(tmp_path):
    # On a later release, doc_revision must bump ONLY for pages whose body
    # changed (vs the previous manifest); unchanged pages keep their revision.
    _init(tmp_path)
    content, pg, ag = _make_corpus(tmp_path)
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-m", "init", date="2026-05-20T10:00:00")

    m1 = stamp_corpus([pg, ag], repo_root=tmp_path, content_root=content,
                      version="2026.06", generated="2026-06-02")

    # Change only PosGain's body; commit at a later date.
    pg.write_text(pg.read_text().replace("body text", "new body text"))
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-m", "edit", date="2026-07-10T10:00:00")

    m2 = stamp_corpus([pg, ag], repo_root=tmp_path, content_root=content,
                      version="2026.07", generated="2026-07-15", prev_manifest=m1)

    by = {d["keyword"]: d for d in m2["documents"]}
    assert by["AutoGOn"]["doc_revision"] == "2026.06"   # unchanged -> kept
    assert by["PosGain"]["doc_revision"] == "2026.07"   # changed -> bumped
    fm, _ = split_doc(pg.read_text())
    assert fm["doc_revision"] == "2026.07"               # stamp reflects bump
    assert fm["last_updated"] == "2026-07-10"


def test_last_updated_stable_across_stamp_commit(tmp_path):
    # A stamp/metadata commit must NOT push last_updated forward. When the body
    # is unchanged vs the previous manifest, keep the prior last_updated even
    # though the file's git last-commit date has since advanced.
    _init(tmp_path)
    content, pg, ag = _make_corpus(tmp_path)
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-m", "content", date="2026-05-20T10:00:00")

    m1 = stamp_corpus([pg, ag], repo_root=tmp_path, content_root=content,
                      version="2026.06", generated="2026-06-02")
    # m1 wrote pg's frontmatter stamp; commit THAT (body unchanged) at a later date.
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-m", "stamp", date="2026-06-02T10:00:00")

    m2 = stamp_corpus([pg, ag], repo_root=tmp_path, content_root=content,
                      version="2026.06", generated="2026-06-30", prev_manifest=m1)

    fm, _ = split_doc(pg.read_text())
    assert fm["last_updated"] == "2026-05-20"            # not pushed to the stamp date
    by = {d["keyword"]: d for d in m2["documents"]}
    assert by["PosGain"]["last_updated"] == "2026-05-20"


def test_stamp_corpus_no_prev_manifest_uses_current_version(tmp_path):
    # Baseline (no previous manifest): every page gets the current version.
    _init(tmp_path)
    content, pg, ag = _make_corpus(tmp_path)
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-m", "init", date="2026-05-20T10:00:00")
    m = stamp_corpus([pg, ag], repo_root=tmp_path, content_root=content,
                     version="2026.06", generated="2026-06-02")
    assert all(d["doc_revision"] == "2026.06" for d in m["documents"])


def test_stamp_corpus_adds_zh_variant_and_keeps_en_record(tmp_path):
    # A .zh.md sidecar must NOT appear as its own top-level document; instead the
    # English record gains an additive `variants` object. Records without a
    # sidecar get no `variants` key, and the English record stays unchanged.
    import hashlib
    _init(tmp_path)
    content, pg, ag = _make_corpus(tmp_path)
    zh = pg.with_name("PosGain.zh.md")
    zh_body = "# PosGain\n\n中文正文\n"
    zh.write_text(
        "---\nkeyword: PosGain\nlanguage: zh-CN\nsummary: 译文\n"
        "attributes:\n  range:\n  - 0\n  - 20000\n---\n" + zh_body
    )
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-m", "init", date="2026-05-20T10:00:00")

    m = stamp_corpus([pg, ag, zh], repo_root=tmp_path, content_root=content,
                     version="2026.06", generated="2026-06-02")

    by = {d["keyword"]: d for d in m["documents"]}
    # zh sidecar is not a standalone document
    paths = [d["path"] for d in m["documents"]]
    assert "02-keywords/01-system/PosGain.zh.md" not in paths
    assert m["document_count"] == 2          # PosGain + AutoGOn only
    # English PosGain gains a variants object
    variants = by["PosGain"]["variants"]
    assert variants["zh-CN"]["path"] == "02-keywords/01-system/PosGain.zh.md"
    assert variants["zh-CN"]["sha256"] == hashlib.sha256(
        zh_body.encode("utf-8")).hexdigest()
    # The English record is otherwise the normal shape.
    assert by["PosGain"]["sha256"] == hashlib.sha256(
        b"# PosGain\n\nbody text\n").hexdigest()
    # A doc without a sidecar gets NO variants key.
    assert "variants" not in by["AutoGOn"]


def test_stamp_corpus_zh_variant_does_not_disturb_en_stamp(tmp_path):
    # Presence of a sidecar must not change the English doc's own facts/body.
    _init(tmp_path)
    content, pg, ag = _make_corpus(tmp_path)
    zh = pg.with_name("PosGain.zh.md")
    zh.write_text(
        "---\nkeyword: PosGain\nlanguage: zh-CN\nsummary: 译文\n---\n中文\n")
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-m", "init", date="2026-05-20T10:00:00")

    stamp_corpus([pg, ag, zh], repo_root=tmp_path, content_root=content,
                 version="2026.06", generated="2026-06-02")

    fm, body = split_doc(pg.read_text())
    assert fm["last_updated"] == "2026-05-20"
    assert body == "# PosGain\n\nbody text\n"


def test_cli_version_subcommand(tmp_path):
    _init(tmp_path)
    content, pg, ag = _make_corpus(tmp_path)
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-m", "init", date="2026-05-20T10:00:00")

    manifest_out = tmp_path / "manifest.json"
    version_file = tmp_path / "VERSION"
    rc = run([
        "version",
        "--content-root", str(content),
        "--repo-root", str(tmp_path),
        "--corpus-version", "2026.06",
        "--generated", "2026-06-02",
        "--manifest-out", str(manifest_out),
        "--version-file", str(version_file),
    ])
    assert rc == 0

    m = json.loads(manifest_out.read_text())
    assert m["version"] == "2026.06"
    assert m["document_count"] == 2
    assert version_file.read_text().strip() == "2026.06"

    fm, _ = split_doc(pg.read_text())
    assert fm["doc_revision"] == "2026.06"
    assert fm["last_updated"] == "2026-05-20"
