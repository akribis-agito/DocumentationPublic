"""Documentation versioning: per-doc git stamps and a RAG manifest.

This is DOC-revision metadata — when a page last changed and at which corpus
revision — kept separate from the firmware `availability` facts the generator
owns. Two frontmatter keys are appended *after* the generator block so they
never interleave with or disturb the owned facts:

    last_updated: YYYY-MM-DD   # git last-commit date of the file
    doc_revision: YYYY.MM      # corpus CalVer at that change

The RAG manifest hashes the BODY only, so a stamp bump (a frontmatter-only
change) does not alter a document's hash and the consumer re-embeds only pages
whose prose actually changed.
"""

from __future__ import annotations

import hashlib


_STAMP_KEYS = ("last_updated", "doc_revision")


def stamp_frontmatter(fm: dict, last_updated: str, doc_revision: str) -> dict:
    """Return a copy of `fm` with the two stamp keys set, appended after the
    generator-owned block. Idempotent and order-stable: re-stamping updates the
    values in place without moving the keys or touching any owned fact."""
    out = {k: v for k, v in fm.items() if k not in _STAMP_KEYS}
    out["last_updated"] = last_updated
    out["doc_revision"] = doc_revision
    return out


def body_sha256(body: str) -> str:
    """SHA-256 (hex) of the document body, independent of frontmatter."""
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def manifest_document(
    rel_path: str,
    keyword: str,
    last_updated: str,
    doc_revision: str,
    body: str,
) -> dict:
    """Build one manifest entry; the body hash is computed here."""
    return {
        "path": rel_path,
        "keyword": keyword,
        "last_updated": last_updated,
        "doc_revision": doc_revision,
        "sha256": body_sha256(body),
    }


def build_manifest(
    documents: list[dict], *, manual: str, version: str, generated: str
) -> dict:
    """Assemble the manifest, documents sorted by path for stable diffs."""
    ordered = sorted(documents, key=lambda d: d["path"])
    return {
        "manual": manual,
        "version": version,
        "generated": generated,
        "document_count": len(ordered),
        "documents": ordered,
    }
