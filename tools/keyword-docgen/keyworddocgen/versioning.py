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
import subprocess
from pathlib import Path

from .frontmatter import render_doc, split_doc


_STAMP_KEYS = ("last_updated", "doc_revision")
_MANUAL_NAME = "Keyword Reference Manual"


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


def last_commit_date(path, repo_root) -> str | None:
    """Return the YYYY-MM-DD of the most recent commit touching `path`, or None
    if the file has never been committed."""
    result = subprocess.run(
        ["git", "-C", str(repo_root), "log", "-1",
         "--format=%ad", "--date=short", "--", str(path)],
        capture_output=True, text=True,
    )
    out = result.stdout.strip()
    return out or None


def stamp_corpus(
    doc_paths,
    *,
    repo_root,
    content_root,
    version: str,
    generated: str,
    manual: str = _MANUAL_NAME,
    prev_manifest: dict | None = None,
) -> dict:
    """Stamp every doc that has frontmatter with its git-derived `last_updated`
    and a `doc_revision`, and return the RAG manifest covering ALL docs
    (frontmatter and legacy alike).

    `doc_revision` is **incremental**: a page keeps the revision it had in
    `prev_manifest` when its body hash is unchanged, and is bumped to `version`
    only when its body changed (or it is new / there is no previous manifest).
    This keeps per-page revisions meaningful release-over-release instead of all
    snapping to the latest version.

    Legacy docs that carry no frontmatter are left on disk untouched (we do not
    inject a frontmatter block into them) but still appear in the manifest with
    their git date and a body hash.
    """
    content_root = Path(content_root)
    prev_by_path = {
        d["path"]: d for d in (prev_manifest or {}).get("documents", [])
    }
    entries: list[dict] = []
    for raw in doc_paths:
        path = Path(raw)
        text = path.read_text()
        fm, body = split_doc(text)
        keyword = (fm.get("keyword") if fm else None) or path.stem
        rel = str(path.relative_to(content_root))
        hash_body = body if fm else text   # legacy: whole file is the prose
        sha = body_sha256(hash_body)
        prev = prev_by_path.get(rel)
        if prev and prev.get("sha256") == sha:
            # Body unchanged vs the previous manifest: keep both stamps stable.
            # This also prevents a stamp/metadata commit from pushing
            # last_updated forward (the stamp commit becomes the file's git
            # last-commit, but the prose did not change).
            last_updated = prev["last_updated"]
            doc_revision = prev["doc_revision"]
        else:
            last_updated = last_commit_date(path, repo_root) or generated
            doc_revision = version
        if fm:
            stamped = stamp_frontmatter(fm, last_updated, doc_revision)
            path.write_text(render_doc(stamped, body))
        entries.append(
            manifest_document(rel, keyword, last_updated, doc_revision, hash_body)
        )
    return build_manifest(
        entries, manual=manual, version=version, generated=generated
    )
