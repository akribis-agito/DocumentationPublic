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
