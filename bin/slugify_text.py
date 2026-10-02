#!/usr/bin/env python3
"""
Slugify a text fragment to a URL slug (hyphen rule).

Rule: lowercase, drop non-word characters, runs of spaces/underscores
become a single hyphen, trim leading/trailing hyphens. Unicode word
characters are kept (unlike the ASCII-only file renamer in Naturgnosis).

Moved from scripts/slugify.py. Difference from the original:
- Import-safe: the CLI lives in main(); importing this module has no
  side effects (the original prompted on stdin at import time).
- argparse CLI with --stdin support instead of a bare input() fallback.

Usage:
    python3 bin/slugify_text.py "Mi Título De Prueba"
    echo "Mi Título" | python3 bin/slugify_text.py --stdin
"""

import argparse
import re
import sys


def slugify(text):
    # Convert to lowercase
    text = text.lower()
    # Replace non-alphanumeric characters (excluding spaces) with nothing
    text = re.sub(r"[^\w\s-]", "", text)
    # Replace spaces and underscores with hyphens
    text = re.sub(r"[\s_]+", "-", text)
    # Remove leading/trailing hyphens
    text = text.strip("-")
    return text


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="slugify_text.py")
    parser.add_argument("text", nargs="*", help="Text to slugify.")
    parser.add_argument(
        "--stdin",
        action="store_true",
        help="Read a line from stdin instead of argv.",
    )
    args = parser.parse_args(argv)

    if args.stdin or not args.text:
        if sys.stdin.isatty() and not args.text:
            parser.error("no text given (pass TEXT args or use --stdin).")
        input_text = sys.stdin.readline().strip()
    else:
        input_text = " ".join(args.text)

    print(slugify(input_text))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
