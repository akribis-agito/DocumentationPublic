"""Command-line entrypoint: append/overwrite frontmatter + write manifest."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .defines import DefineTable
from .frontmatter import render_doc, split_doc
from .manifest import render_manifest
from .merge import VersionAlreadyRecorded, merge_version
from .model import PRODUCTS, product_supported
from .table_parser import parse_params
from .versioning import stamp_corpus


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="keyword-docgen")
    sub = parser.add_subparsers(dest="mode", required=True)
    for mode in ("append", "overwrite"):
        p = sub.add_parser(mode)
        p.add_argument("--version", required=True, choices=["v4", "v5"])
        p.add_argument("--params", required=True, type=Path)
        p.add_argument("--defines", required=True, type=Path, nargs="+",
                       help="Header file(s) defining MIN/MAX/DFLT/sizes")
        p.add_argument("--docs-root", required=True, type=Path)
        p.add_argument("--manifest", required=True, type=Path)

    v = sub.add_parser(
        "version", help="Stamp per-doc last_updated/doc_revision and write the "
                        "RAG manifest.json (DOC-revision metadata, from git)."
    )
    v.add_argument("--content-root", required=True, type=Path,
                   help="Manual content/ dir holding the doc tree")
    v.add_argument("--repo-root", required=True, type=Path,
                   help="Git repo root, for last-commit dates")
    v.add_argument("--corpus-version", required=True,
                   help="Corpus CalVer, e.g. 2026.06")
    v.add_argument("--generated", required=True,
                   help="Generation date YYYY-MM-DD (fallback for uncommitted)")
    v.add_argument("--manifest-out", required=True, type=Path)
    v.add_argument("--version-file", required=True, type=Path)
    return parser


_SKIP_NAMES = {"index.md", "README.md"}


def _discover_docs(content_root: Path) -> list[Path]:
    """Every content .md the RAG cares about (excludes _files/ and index/readme)."""
    docs: list[Path] = []
    for path in sorted(content_root.rglob("*.md")):
        if "_files" in path.parts or path.name in _SKIP_NAMES:
            continue
        docs.append(path)
    return docs


def run_version(args) -> int:
    docs = _discover_docs(args.content_root)
    # Load the previous manifest (if any) so doc_revision is bumped only for
    # pages whose body actually changed.
    prev_manifest = None
    if args.manifest_out.exists():
        try:
            prev_manifest = json.loads(args.manifest_out.read_text())
        except (OSError, json.JSONDecodeError):
            prev_manifest = None
    manifest = stamp_corpus(
        docs,
        repo_root=args.repo_root,
        content_root=args.content_root,
        version=args.corpus_version,
        generated=args.generated,
        prev_manifest=prev_manifest,
    )
    args.manifest_out.parent.mkdir(parents=True, exist_ok=True)
    args.manifest_out.write_text(json.dumps(manifest, indent=2) + "\n")
    args.version_file.write_text(args.corpus_version + "\n")
    print(f"stamped {manifest['document_count']} docs at {args.corpus_version}")
    return 0


_KEYWORD_ROOTS = ("02-keywords", "03-special-features", "05-legacy-keywords")


def _index_docs(docs_root: Path) -> dict[str, Path]:
    """Map mnemonic -> doc path for every keyword .md across the keyword roots.

    Keyword pages live under 02-keywords, but also under 03-special-features
    (auto-gain, UPM, spring/friction comp, …) and 05-legacy-keywords; all are
    indexed so they receive generated frontmatter. Section overviews (`00-*`)
    and any `_`-prefixed dir (`_triage`/`_files`/`_manifest`) are skipped.
    """
    candidates: dict[str, list[Path]] = {}
    for root in _KEYWORD_ROOTS:
        base = docs_root / root
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            if path.stem.startswith("00-"):
                continue
            rel = path.relative_to(docs_root)
            if any(part.startswith("_") for part in rel.parts):
                continue
            candidates.setdefault(path.stem, []).append(path)

    # On a stem collision (same mnemonic documented in two places — a canonical
    # entry plus a cross-ref stub or legacy alias), target the canonical entry,
    # i.e. the one that already carries a `keyword:` frontmatter field. This
    # avoids clobbering pointer stubs. If none is canonical yet (a brand-new
    # keyword doc), take the first in (root, sorted) order.
    index: dict[str, Path] = {}
    for stem, paths in candidates.items():
        canonical = next((p for p in paths if _has_keyword_field(p)), None)
        index[stem] = canonical or paths[0]
    return index


def _has_keyword_field(path: Path) -> bool:
    try:
        fm, _ = split_doc(path.read_text())
    except OSError:
        return False
    return isinstance(fm, dict) and "keyword" in fm


def run(argv: list[str]) -> int:
    args = _build_parser().parse_args(argv)
    if args.mode == "version":
        return run_version(args)
    defines = DefineTable.from_headers(list(args.defines))
    tables = parse_params(args.params, defines)
    docs = _index_docs(args.docs_root)

    # Build per-keyword scan cells across products.
    all_keywords = set()
    for names in tables.values():
        all_keywords |= set(names)

    for mnemonic in sorted(all_keywords):
        path = docs.get(mnemonic)
        if path is None:
            continue  # undocumented -> handled by the manifest below
        scan_cells = {
            p: (tables.get(p, {}).get(mnemonic)
                if product_supported(p, args.version) else None)
            for p in PRODUCTS
        }
        fm, body = split_doc(path.read_text())
        fm.setdefault("keyword", mnemonic)
        try:
            new_fm = merge_version(fm, scan_cells, args.version, mode=args.mode)
        except VersionAlreadyRecorded:
            print(
                f"error: {mnemonic}: version {args.version} already recorded "
                f"(use 'overwrite' to refresh)",
                file=sys.stderr,
            )
            return 1
        path.write_text(render_doc(new_fm, body))

    scanned = {p: set(tables.get(p, {})) for p in PRODUCTS}
    manifest = render_manifest(scanned, set(docs), args.version)
    args.manifest.parent.mkdir(parents=True, exist_ok=True)
    args.manifest.write_text(manifest)
    return 0


def main() -> None:
    sys.exit(run(sys.argv[1:]))


if __name__ == "__main__":
    main()
