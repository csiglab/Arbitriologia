# bin/

Executable data/tooling CLIs (Naturgnosis-style: one self-contained script
per task, `Usage:` in the docstring, `argparse` + `main()`, no import
side effects). Formerly `scripts/` — moved in the reorg.

| Script | Replaces | Purpose |
| --- | --- | --- |
| `build_clasificadores.py` | `scripts/clasificadores.py` | PDF → markdown cache → `clasificadores.xlsx` |
| `parse_organization.py` | `scripts/organization.py` + `scripts/dataset.py` | Parse 11-field pipe rows; also hosts the `Dataset` container for the research notebook |
| `download_datos_gob_do.sh` | `scripts/download.bash` | Paginated download of datos.gob.do metadata into `data/raw/` |
| `slugify_text.py` | `scripts/slugify.py` | Slugify a text fragment (hyphen rule) |
| `build_tree.py` | `scripts/tree.py` | Institutional-code graph demo image |

Notes:

- Run via `uv run --project . python3 bin/<script>.py --help`.
- Heavy deps (`pandas`, `pymupdf4llm`, `matplotlib`, `networkx`,
  `openpyxl`) are declared in `pyproject.toml`; run `uv sync` first.
- Slug rule: `slugify_text.py` emits **hyphens** for text slugs. This
  differs from Naturgnosis `bin/slugify_files.py`, which emits
  **underscores** for file names. Kept deliberately; do not mix them.
- `build_clasificadores.py` defaults: `--pdf
  data/Clasificador-Institucional.pdf`, `--md-out
  data/Clasificador-Institucional.md`, `--xlsx-out
  data/clasificadores.xlsx`.
- `download_datos_gob_do.sh` writes to `data/raw/` and never commits
  session cookies. If Cloudflare blocks you, export a fresh `CF_COOKIE`.
