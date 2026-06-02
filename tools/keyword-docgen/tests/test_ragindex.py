"""Tests for the RAG export: fact-enriched, document-level chunks."""

import json

from keyworddocgen.cli import run
from keyworddocgen.ragindex import fact_header, extract_links, chunk_record


def _fm():
    return {
        "keyword": "PosGain",
        "summary": "Proportional position gain.",
        "availability": {"standalone": ["v4"], "central-i": ["v4", "v5"]},
        "can_code": 100,
        "attributes": {
            "access": "rw", "scope": "axis", "units": "user",
            "range": [0, 20000], "default": 0, "data_type": "int32",
        },
    }


# --- fact_header ---------------------------------------------------------

def test_fact_header_includes_key_facts():
    h = fact_header(_fm())
    assert "PosGain" in h
    assert "100" in h                       # can_code
    assert "axis" in h                      # scope
    assert "20000" in h                     # range bound
    assert "v4" in h and "v5" in h          # versions
    assert "Proportional position gain." in h


def test_fact_header_handles_prose_doc_without_facts():
    # A page with only a summary (no attributes/can_code) still gets a header.
    h = fact_header({"keyword": "Intro", "summary": "How to read this manual."})
    assert "Intro" in h and "How to read this manual." in h


# --- extract_links -------------------------------------------------------

def test_extract_links_dedupes_strips_and_ignores_external():
    body = (
        "See [PosKi](PosKi.md) and [Vel](../10/VelGain.md). Again [PosKi](PosKi.md).\n"
        "External [site](https://x.com), anchor [s](#sec), image ![d](d.svg)."
    )
    assert extract_links(body) == ["PosKi", "VelGain"]


def test_extract_links_strips_anchor_in_target():
    assert extract_links("[x](VelGain.md#range)") == ["VelGain"]


# --- chunk_record --------------------------------------------------------

def test_chunk_record_structure():
    rec = chunk_record(
        "02-keywords/01-system/PosGain.md", _fm(),
        "# PosGain\n\nText. See [PosKi](PosKi.md).\n",
        last_updated="2026-06-02", doc_revision="2026.06", sha256="abc123",
    )
    assert rec["id"] == "02-keywords/01-system/PosGain.md"
    assert rec["keyword"] == "PosGain"
    assert rec["text"].startswith("Keyword PosGain")     # fact header leads
    assert "See [PosKi](PosKi.md)." in rec["text"]        # body included
    md = rec["metadata"]
    assert md["can_code"] == 100
    assert md["scope"] == "axis"
    assert md["units"] == "user"
    assert md["availability"] == {"standalone": ["v4"], "central-i": ["v4", "v5"]}
    assert md["last_updated"] == "2026-06-02"
    assert md["doc_revision"] == "2026.06"
    assert md["sha256"] == "abc123"
    assert rec["related"] == ["PosKi"]


def test_chunk_record_keyword_falls_back_to_path_stem():
    rec = chunk_record(
        "01-intro/getting-started.md", {}, "# Getting started\n\nbody\n",
        last_updated="2026-06-02", doc_revision="2026.06", sha256="z",
    )
    assert rec["keyword"] == "getting-started"
    assert rec["text"].startswith("Keyword getting-started") or "getting-started" in rec["text"]


def test_cli_rag_export(tmp_path):
    content = tmp_path / "content"
    (content / "02-keywords").mkdir(parents=True)
    (content / "02-keywords" / "PosGain.md").write_text(
        "---\nkeyword: PosGain\nsummary: P.\ncan_code: 100\n"
        "attributes:\n  scope: axis\n---\n# PosGain\n\nSee [PosKi](PosKi.md).\n"
    )
    manifest = {"documents": [{
        "path": "02-keywords/PosGain.md", "keyword": "PosGain",
        "last_updated": "2026-06-02", "doc_revision": "2026.06", "sha256": "abc",
    }]}
    mpath = tmp_path / "manifest.json"
    mpath.write_text(json.dumps(manifest))
    out = tmp_path / "chunks.jsonl"

    rc = run(["rag-export", "--content-root", str(content),
              "--manifest", str(mpath), "--out", str(out)])
    assert rc == 0

    lines = out.read_text().splitlines()
    assert len(lines) == 1
    rec = json.loads(lines[0])
    assert rec["keyword"] == "PosGain"
    assert rec["text"].startswith("Keyword PosGain")
    assert rec["metadata"]["scope"] == "axis"
    assert rec["metadata"]["doc_revision"] == "2026.06"
    assert rec["related"] == ["PosKi"]
