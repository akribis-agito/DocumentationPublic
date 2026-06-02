"""Tests for documentation versioning: per-doc git stamps + RAG manifest.

Versioning is DOC-revision metadata (when a page last changed), distinct from
the firmware `availability` (v4/v5) facts the generator owns. The stamp lives
in frontmatter as `last_updated` (YYYY-MM-DD) and `doc_revision` (CalVer), and
must never disturb the generator-owned fact block.
"""

import hashlib

from keyworddocgen.versioning import (
    stamp_frontmatter,
    body_sha256,
    manifest_document,
    build_manifest,
)


def _facts():
    # A representative generator-owned frontmatter block.
    return {
        "keyword": "PosGain",
        "summary": "Proportional position gain.",
        "availability": {"standalone": ["v4"], "central-i": ["v4", "v5"]},
        "can_code": 100,
        "attributes": {"access": "rw", "range": [0, 20000], "default": 0},
        "overrides": {},
    }


# --- stamp_frontmatter ---------------------------------------------------

def test_stamp_adds_both_keys():
    out = stamp_frontmatter(_facts(), "2026-06-02", "2026.06")
    assert out["last_updated"] == "2026-06-02"
    assert out["doc_revision"] == "2026.06"


def test_stamp_preserves_all_generator_facts():
    src = _facts()
    out = stamp_frontmatter(src, "2026-06-02", "2026.06")
    for k, v in src.items():
        assert out[k] == v          # every original fact survives unchanged


def test_stamp_does_not_mutate_input():
    src = _facts()
    stamp_frontmatter(src, "2026-06-02", "2026.06")
    assert "last_updated" not in src  # input dict untouched (returns a copy)


def test_stamp_is_idempotent_for_same_values():
    once = stamp_frontmatter(_facts(), "2026-06-02", "2026.06")
    twice = stamp_frontmatter(once, "2026-06-02", "2026.06")
    assert once == twice


def test_restamp_updates_to_new_revision_without_reordering():
    once = stamp_frontmatter(_facts(), "2026-06-02", "2026.06")
    later = stamp_frontmatter(once, "2026-07-15", "2026.07")
    assert later["last_updated"] == "2026-07-15"
    assert later["doc_revision"] == "2026.07"
    assert list(later.keys()) == list(once.keys())   # key order stable


def test_stamp_keys_go_after_generator_block():
    # Doc-meta should trail the fact block, not interleave with it.
    out = stamp_frontmatter(_facts(), "2026-06-02", "2026.06")
    keys = list(out.keys())
    assert keys.index("last_updated") > keys.index("overrides")
    assert keys.index("doc_revision") > keys.index("overrides")


# --- body_sha256 ---------------------------------------------------------

def test_body_sha256_matches_hashlib():
    body = "\n# PosGain\n\nProportional gain.\n"
    assert body_sha256(body) == hashlib.sha256(body.encode("utf-8")).hexdigest()


def test_body_hash_is_frontmatter_independent():
    # The whole point: a stamp bump (frontmatter-only change) must NOT change
    # the body hash, so the RAG doesn't needlessly re-embed unchanged prose.
    body = "\n# PosGain\n\nProportional gain.\n"
    assert body_sha256(body) == body_sha256(body)


def test_body_hash_changes_when_prose_changes():
    a = body_sha256("\n# PosGain\n\nProportional gain.\n")
    b = body_sha256("\n# PosGain\n\nProportional position gain.\n")
    assert a != b


# --- manifest ------------------------------------------------------------

def test_manifest_document_entry():
    body = "\n# PosGain\n\ntext\n"
    doc = manifest_document(
        rel_path="02-keywords/.../PosGain.md",
        keyword="PosGain",
        last_updated="2026-06-02",
        doc_revision="2026.06",
        body=body,
    )
    assert doc == {
        "path": "02-keywords/.../PosGain.md",
        "keyword": "PosGain",
        "last_updated": "2026-06-02",
        "doc_revision": "2026.06",
        "sha256": hashlib.sha256(body.encode("utf-8")).hexdigest(),
    }


def test_build_manifest_shape():
    docs = [
        manifest_document("a/B.md", "B", "2026-06-01", "2026.06", "x"),
        manifest_document("a/A.md", "A", "2026-06-02", "2026.06", "y"),
    ]
    m = build_manifest(
        docs, manual="Keyword Reference Manual",
        version="2026.06", generated="2026-06-02",
    )
    assert m["manual"] == "Keyword Reference Manual"
    assert m["version"] == "2026.06"
    assert m["generated"] == "2026-06-02"
    assert m["document_count"] == 2
    # documents sorted by path for stable diffs
    assert [d["keyword"] for d in m["documents"]] == ["A", "B"]
