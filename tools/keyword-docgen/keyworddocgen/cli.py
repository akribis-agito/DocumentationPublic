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
    manifest = stamp_corpus(
        docs,
        repo_root=args.repo_root,
        content_root=args.content_root,
        version=args.corpus_version,
        generated=args.generated,
    )
    args.manifest_out.parent.mkdir(parents=True, exist_ok=True)
    args.manifest_out.write_text(json.dumps(manifest, indent=2) + "\n")
    args.version_file.write_text(args.corpus_version + "\n")
    print(f"stamped {manifest['document_count']} docs at {args.corpus_version}")
    return 0


def _index_docs(docs_root: Path) -> dict[str, Path]:
    """Map mnemonic -> doc path for every existing keyword .md."""
    index: dict[str, Path] = {}
    keywords_dir = docs_root / "02-keywords"
    for path in keywords_dir.rglob("*.md"):
        if path.stem.startswith("00-"):
            continue
        index[path.stem] = path
    return index


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
