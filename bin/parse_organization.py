#!/usr/bin/env python3
"""
Organization row parser (institutional classifier format).

Parses pipe-delimited organization rows with 11 fields:
sector | subsector | area | subarea | seccion | poderes | entidad |
capitulo | subcapitulo | unidad_ejecutora | denominacion

The caller is responsible for stripping the leading/trailing "|" before
calling parse() (the notebook does `line.strip()[1:-1]` first).

Also hosts the minimal Dataset container (moved from scripts/dataset.py),
kept for the research notebook.

Usage:
    python3 bin/parse_organization.py [--json] [FILE ...]
    echo "a|b|..." | python3 bin/parse_organization.py --json

    With no FILE (or FILE "-"), lines are read from stdin.
"""

import argparse
import json
import sys

COLUMNS = [
    "sector",
    "subsector",
    "area",
    "subarea",
    "seccion",
    "poderes",
    "entidad",
    "capitulo",
    "subcapitulo",
    "unidad_ejecutora",
    "denominacion",
]


def parse(line):
    """
    Parses a given line of text and returns a dictionary representation.

    Args:
        line (str): The input string to parse (11 pipe-separated fields,
            without leading/trailing pipes).

    Returns:
        dict: A dictionary containing the parsed data from the line.
    """
    fields = line.split("|")
    if len(COLUMNS) != len(fields):
        raise ValueError(
            f"Mismatch: Expected {len(COLUMNS)} columns, "
            f"but found {len(fields)} fields in the row: {line!r}"
        )
    return dict(zip(COLUMNS, fields))


class Dataset:
    """Minimal in-memory dataset container (moved from scripts/dataset.py)."""

    def __init__(self, name=None, schema=None, records=None, metadata=None):
        """
        Initialize the Dataset class.

        Args:
            name (str, optional): Name of the dataset.
            schema (dict, optional): Schema of the dataset.
            records (optional): The dataset records.
            metadata (optional): Dataset metadata.
        """
        self.records = records
        self.name = name
        self.schema = schema
        self.metadata = metadata


def _iter_lines(files):
    if not files:
        for line in sys.stdin:
            line = line.rstrip("\n")
            if line:
                yield line
        return
    for name in files:
        if name == "-":
            for line in sys.stdin:
                line = line.rstrip("\n")
                if line:
                    yield line
            continue
        with open(name, encoding="utf-8") as fh:
            for line in fh:
                line = line.rstrip("\n")
                if line:
                    yield line


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="parse_organization.py")
    parser.add_argument("files", nargs="*", help="Input files (default: stdin).")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit one JSON object per line (default: repr of dict).",
    )
    parser.add_argument(
        "--skip-errors",
        action="store_true",
        help="Warn on malformed rows instead of exiting non-zero.",
    )
    args = parser.parse_args(argv)

    failed = 0
    for line in _iter_lines(args.files):
        try:
            result = parse(line)
        except ValueError as exc:
            failed += 1
            print(f"[parse_organization] skip: {exc}", file=sys.stderr)
            if not args.skip_errors:
                return 1
            continue
        if args.json:
            print(json.dumps(result, ensure_ascii=False))
        else:
            print(result)
    if failed and not args.skip_errors:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
