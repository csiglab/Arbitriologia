#!/usr/bin/env python3
"""
Institutional classifier extractor.

Converts the Clasificador-Institucional PDF to markdown (via pymupdf4llm,
only when the markdown cache is missing or --refresh is given), then
extracts the 11-column institutional rows and writes them to .xlsx.

Moved from scripts/clasificadores.py. Differences from the original:
- No hardcoded absolute PDF path (defaults to data/Clasificador-Institucional.pdf).
- argparse CLI (--pdf, --md-out, --xlsx-out, --refresh, --quiet).
- No bare `except: pass`; malformed rows are counted and reported.
- Import-safe: nothing runs at import time.

Usage:
    python3 bin/build_clasificadores.py
    python3 bin/build_clasificadores.py --pdf data/Clasificador-Institucional.pdf \
        --md-out data/Clasificador-Institucional.md --xlsx-out data/clasificadores.xlsx
"""

import argparse
import re
import sys
from pathlib import Path

ROW_RE = re.compile(r"^\|\d+\|\d+\|\d+\|\d+\|\d+.*")

FIELDS = [
    "sector",
    "sub_sector",
    "area",
    "sub_area",
    "seccion",
    "poderes",
    "entidad",
    "capitulo",
    "sub_capitulo",
    "unidad_ejecutora",
    "denominacion",
]


class Clasificador:
    def __init__(self) -> None:
        self.sector: str = ""
        self.sub_sector: str = ""
        self.area: str = ""
        self.sub_area: str = ""
        self.seccion: str = ""
        self.poderes: str = ""
        self.entidad: str = ""
        self.capitulo: str = ""
        self.sub_capitulo: str = ""
        self.unidad_ejecutora: str = ""
        self.denominacion: str = ""


def extract_rows(md_text):
    """Yield Clasificador objects parsed from markdown table text."""
    parsed = 0
    skipped = 0
    for line in md_text.splitlines():
        if not ROW_RE.match(line):
            continue
        data = line.split("|")
        row = data[1:-1]
        if row.count("") > 0:
            skipped += 1
            continue
        if len(row) != len(FIELDS):
            skipped += 1
            continue
        try:
            parsed += 1
            c = Clasificador()
            c.__dict__.update(dict(zip(FIELDS, row)))
            if c.unidad_ejecutora.isnumeric():
                yield c
            else:
                skipped += 1
        except Exception as exc:  # noqa: BLE001 - counted, reported, never silent
            skipped += 1
            print(f"[build_clasificadores] skip row: {exc}", file=sys.stderr)
    print(
        f"[build_clasificadores] parsed={parsed} skipped={skipped}",
        file=sys.stderr,
    )


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="build_clasificadores.py")
    parser.add_argument(
        "--pdf",
        default="data/Clasificador-Institucional.pdf",
        help="Source PDF path.",
    )
    parser.add_argument(
        "--md-out",
        default="data/Clasificador-Institucional.md",
        help="Markdown cache path.",
    )
    parser.add_argument(
        "--xlsx-out",
        default="data/clasificadores.xlsx",
        help="Output .xlsx path.",
    )
    parser.add_argument(
        "--refresh",
        action="store_true",
        help="Re-render markdown from PDF even if the cache exists.",
    )
    parser.add_argument(
        "--quiet", action="store_true", help="Do not print parsed rows to stdout."
    )
    args = parser.parse_args(argv)

    try:
        import pandas as pd
        import pymupdf4llm
    except ModuleNotFoundError as exc:
        print(
            f"[build_clasificadores] missing dependency {exc.name}; "
            "run `uv sync` (see pyproject.toml).",
            file=sys.stderr,
        )
        return 2

    pdf_path = Path(args.pdf)
    md_path = Path(args.md_out)
    xlsx_path = Path(args.xlsx_out)

    if not pdf_path.is_file() and (args.refresh or not md_path.is_file()):
        print(f"[build_clasificadores] ERROR: PDF not found: {pdf_path}", file=sys.stderr)
        return 1

    if args.refresh or not md_path.is_file():
        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(pymupdf4llm.to_markdown(str(pdf_path)), encoding="utf-8")
        print(f"[build_clasificadores] markdown cache written: {md_path}", file=sys.stderr)

    content = md_path.read_text(encoding="utf-8")
    objs = list(extract_rows(content))

    for c in objs:
        if not args.quiet:
            print(
                f"|{c.sector:>5}|{c.sub_sector:>5}|{c.area:>5}|{c.sub_area:>5}|"
                f"{c.seccion:>5}|{c.poderes:>5}|{c.entidad:>5}|{c.capitulo:>5}|"
                f"{c.sub_capitulo:>5}|{c.unidad_ejecutora:>5}|{c.denominacion:>85}|"
            )

    print(f"[build_clasificadores] extracted {len(objs)} rows", file=sys.stderr)
    if not objs:
        print("[build_clasificadores] ERROR: no rows extracted.", file=sys.stderr)
        return 1

    xlsx_path.parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame([o.__dict__ for o in objs])
    df.to_excel(xlsx_path, index=False)
    print(f"[build_clasificadores] wrote {xlsx_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
