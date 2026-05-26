"""Command-line entrypoint: append/overwrite frontmatter + write manifest."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .defines import DefineTable
from .frontmatter import render_doc, split_doc
from .manifest import render_manifest
from .merge import VersionAlreadyRecorded, merge_version
from .model import PRODUCTS
from .table_parser import parse_params


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
    return parser


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
        scan_cells = {p: tables.get(p, {}).get(mnemonic) for p in PRODUCTS}
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
