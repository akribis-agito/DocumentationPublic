"""Build fact-enriched, document-level chunks for RAG ingestion.

Each keyword page becomes ONE chunk whose embedded `text` is the page body
prefixed with a synthesized fact header (so the embedding captures the
structured facts, not just prose). Frontmatter facts and version stamps ride
along as filterable `metadata`, and intra-manual links become `related[]` for
graph-aware re-ranking.
"""

from __future__ import annotations

import re
from pathlib import Path

_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

# Attribute keys surfaced into chunk metadata (in a stable order).
_META_ATTRS = (
    "access", "scope", "flash", "type", "array_size", "data_type",
    "ok_in_motion", "ok_motor_on", "units", "range", "default",
    "scaling", "implemented",
)


def fact_header(fm: dict) -> str:
    """Synthesize a one-line header carrying the page's key facts, so a fact
    query (range/scope/availability/CAN code) embeds well."""
    keyword = fm.get("keyword", "")
    parts: list[str] = []
    if fm.get("can_code") is not None:
        parts.append(f"CAN {fm['can_code']}")
    attrs = fm.get("attributes") or {}
    if attrs.get("scope"):
        parts.append(str(attrs["scope"]))
    if attrs.get("access"):
        parts.append(str(attrs["access"]))
    units = attrs.get("units")
    if units and units != "none":
        parts.append(f"units={units}")
    rng = attrs.get("range")
    if rng:
        parts.append(f"range={rng}")
    avail = fm.get("availability") or {}
    versions = sorted({v for vs in avail.values() if vs for v in vs})
    if versions:
        parts.append("/".join(versions))

    head = f"Keyword {keyword}"
    if parts:
        head += f" ({'; '.join(parts)})"
    summary = fm.get("summary")
    if summary:
        head += f": {summary}"
    return head


def extract_links(body: str) -> list[str]:
    """Return the keyword stems this page links to (intra-manual `*.md` links),
    de-duplicated, in first-seen order. Ignores external URLs, anchors and
    images."""
    out: list[str] = []
    seen: set[str] = set()
    for match in _LINK.finditer(body):
        target = match.group(1).split("#", 1)[0].strip()
        if not target.endswith(".md"):
            continue
        stem = target.rsplit("/", 1)[-1][:-3]
        if stem and stem not in seen:
            seen.add(stem)
            out.append(stem)
    return out


def chunk_record(
    rel_path: str,
    fm: dict,
    body: str,
    *,
    last_updated: str,
    doc_revision: str,
    sha256: str,
) -> dict:
    """Build one document-level chunk for `rel_path`."""
    fm = fm or {}
    keyword = fm.get("keyword") or Path(rel_path).stem
    header = fact_header({**fm, "keyword": keyword})
    text = f"{header}\n\n{body}"

    metadata: dict = {
        "path": rel_path,
        "keyword": keyword,
        "last_updated": last_updated,
        "doc_revision": doc_revision,
        "sha256": sha256,
    }
    if fm.get("can_code") is not None:
        metadata["can_code"] = fm["can_code"]
    attrs = fm.get("attributes") or {}
    for key in _META_ATTRS:
        if key in attrs:
            metadata[key] = attrs[key]
    if fm.get("availability"):
        metadata["availability"] = fm["availability"]
    if fm.get("removed_in"):
        metadata["removed_in"] = fm["removed_in"]

    return {
        "id": rel_path,
        "keyword": keyword,
        "text": text,
        "metadata": metadata,
        "related": extract_links(body),
    }
