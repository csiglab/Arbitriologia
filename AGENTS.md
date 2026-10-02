# AGENTS.md

## Purpose

Instructions for AI agents working in this repository. Follow the conventions below; when a
directory contains its own `AGENTS.md`, it takes precedence for work inside that directory.

## Project Context

### Description

Laboratorium Arbitristae is a space for prototyping ideas — investigating and designing strategies
for the technological and productive greatness of the Dominican Republic. It has two halves that
must stay separable: a **published corpus** (an mkdocs site served from `docs/`) and a **data
pipeline** (`bin/` CLIs feeding `data/`), plus exploratory notebooks in `research/`.

### Objectives

- Keep the published corpus coherent and navigable (`docs/` → `web/mkdocs.yml` → nginx).
- Keep `bin/` runnable one-script-per-task, with the Makefile as the documented entry point.
- Keep the deploy path reproducible: Dockerfile → GHCR (`ghcr.io/csiglab/arbitriologia`) →
  `deploy.sh`.

### Scope

- In: the corpus under `docs/`, the site configuration under `web/`, the CLIs under `bin/`,
  artifacts under `data/`, notebooks under `research/`, and the build/deploy tooling
  (`Makefile`, `build.sh`, `Dockerfile`, `deploy.sh`, `deploy/`, `.github/workflows/`).
- Out: the image and asset libraries vendored under `web/js/` (MathJax, KaTeX — third-party,
  never hand-edit); `img/` beyond adding new figures; anything outside this repository.

## Repository Structure

| Path | Role |
|------|------|
| `docs/` | The published corpus (~730 markdown files). `Locus-Instrumentorum/` (tools), `Locus-Meliorandis/` (change), `Locus-Social-Realitatis/` (structure and dynamics of social reality), `Breviarium/` (essays and cartillas), `Meta/`, `QA/`, `Reflection/`, `tree.html`. |
| `docs/README.md` | Curated reading list — update it when notes are added or promoted. |
| `web/mkdocs.yml` | Site config: `site_name: Arbitreria`, `docs_dir: ../docs`, material theme (indigo, light/dark), `pymdownx.arithmatex` with `generic: true`. |
| `web/js/` | Vendored MathJax (`mathjax/es5/`) and KaTeX (`katex/dist/`), served locally. Third-party — do not edit. |
| `web/hooks/copy_assets.py` | mkdocs `on_post_build` hook that copies the vendored assets into the site. Removing it breaks all math rendering. |
| `bin/` | Data/tooling CLIs, one self-contained script per task (see `bin/README.md`): `build_clasificadores.py`, `build_tree.py`, `parse_organization.py`, `slugify_text.py`, `download_datos_gob_do.sh`. |
| `data/` | Pipeline inputs/outputs: `metadata.md`, `raw/` (API dumps), generated `Clasificador-Institucional.md` + `clasificadores.xlsx`. See `data/README.md`. |
| `research/` | Exploratory Jupyter notebooks, one directory per domain (`burocracia/`, `economia/`, `trade/`, `poblacion/`, …). Not part of the site. |
| `operation/` | Operational lab notes (6 files). Not part of the site. |
| `img/` | Figures, some referenced from notes. |
| `deploy/` | `setup-server.sh` (one-time bootstrap), `nginx-arbitriologia.conf` (TLS reverse proxy). |
| `Makefile` | Documented entry point for every common task — prefer it over raw commands. |

## Agent Operating Principles

### Understand Before Changing

Read `docs/README.md` and the target note before editing it. The corpus is heavily
cross-linked: a moved or renamed file breaks inbound links across hundreds of notes, and there is
no link checker in CI to catch it.

Note naming is **not** uniform and each subtree owns its convention — `Breviarium/` uses
kebab-case (`a-theory-of-goverment.md`), `Locus-Social-Realitatis/` uses `TitleCase.md`. Match the
neighbours of the file you touch; do not normalize a whole subtree in passing.

### Prefer Existing Solutions

- Route work through the `Makefile` targets; they already wrap `uv run --project .` and the right
  paths. Add a target instead of documenting a raw command.
- Extend an existing `bin/` CLI (or add a sibling that follows its shape: `Usage:` in the
  docstring, `argparse` + `main()`, no import side effects) instead of writing a one-off script.
- Reuse the theme wiring in `web/mkdocs.yml` for styling and math; never hardcode colors or pull
  assets from a CDN (the site is built for offline/local serving).

### Minimize Change

The corpus is prose — keep edits surgical and in the voice of the surrounding note. When changing
`bin/` CLI flags or output paths, update `bin/README.md`, `data/README.md`, the `Makefile` defaults,
and the notebook callers in the same change set.

### Preserve Invariants

- `.env` is never committed; `.env.example` is the only committed template.
- Generated artifacts are never hand-edited and never committed: `web/site/`,
  `data/raw/`, `data/clasificadores.xlsx`, `data/Clasificador-Institucional.md`, `graph.png`,
  `data_*.json`. Change the generator in `bin/` and re-run the target.
- `web/hooks/copy_assets.py` must keep copying `js/mathjax/es5` and `js/katex/dist` into the
  build output; math depends on it.
- The `nav:` block in `web/mkdocs.yml` is intentionally commented out, so page URLs derive from
  `docs/` paths. Adding a `nav:` block would change every published URL — that is a
  content-owner decision, not an incidental edit.
- The Docker build only copies `pyproject.toml`, `web/`, and `docs/` (see `.dockerignore`). If a
  build needs a new input, it must live in one of those three paths.
- `deploy/nginx-arbitriologia.conf` proxies to `127.0.0.1:8080`, which must stay in sync with
  `ARBITRIOLOGIA_PORT` in `.env`.
- `.github/workflows/deploy.yml` publishes `:latest` on every push to `main`; the SSH deploy job is
  commented out, so pushing does not touch the live server.

### Keep Work Scoped

One concern per change set. Commit messages follow
`feat|fix|docs|style|refactor|test|chore(scope): summary`. Note that `prepare-commit-msg`
overwrites the message with a `type(<ref>): message` template — see Git Workflow.

## Development Environment

### Requirements

- Python 3.12+ (`.python-version`), dependencies via `uv` + `pyproject.toml`
- Docker (build and deploy), `mkdocs-material` for local preview

### Setup

```sh
uv sync                        # install dependencies into .venv
cp .env.example .env           # optional; sets ARBITRIOLOGIA_PORT
```

### Common commands

```sh
make help                      # list every target
make serve                     # preview at 127.0.0.1:$ARBITRIOLOGIA_PORT
make dev                       # preview with live reload
make build                     # build the site via build.sh
make clasificador              # data/Clasificador-Institucional.pdf -> md + xlsx
make download                  # datos.gob.do metadata -> data/raw/
make tree                      # institutional-code graph -> graph.png
make slugify TEXT='example'    # slug helper
make deploy-local              # build the image and run it on PORT
make setup-server DOMAIN=... EMAIL=...   # one-time server bootstrap
make clean                     # remove pycache, web/site, generated data artifacts
```

### Verification

There is no test suite. Before declaring done:

```sh
make build                     # must succeed
make serve                     # then load the affected page
```

Check the pages you touched render, that math typesets (MathJax loaded, no raw `$…$`), and that
internal links resolve. For `bin/` changes, run the script with `--help` and a real invocation via
its Makefile target, and confirm the output lands at the documented path.

## Git Workflow

Global git configuration lives in `~/configs/global/git` (hooks via `core.hooksPath`) and
`~/configs/bin` (helper scripts). Every commit passes through four active hooks.

### Check-in policy (`pre-commit.d/00-authorization-policy.sh`)

A staged file is only accepted if it carries the extended attribute `user.checkin=1` — otherwise
the commit is rejected with "Required check mark is missing".

```sh
mark-for-commit <file>…        # mark files (alias: mfc; ~/configs/bin/mark-for-commit)
mark-for-commit --list         # list marked files
mark-for-commit --unmark <f>…  # remove the mark
git diff --cached --name-only -z --diff-filter=ACM | xargs -0 mark-for-commit   # bulk-mark staged
```

The mark is a filesystem xattr: it survives staging, is not versioned, and must be re-applied on
new files.

### Annotation policy (`pre-commit.d/01-annotation-policy.sh`)

Staged source files (patterns in `annotations.conf`) must not contain BLOCK annotations —
`@WORKING`, `@FIXME`, `@QUESTION`, `@VERIFY` — or the commit is rejected. `@TODO`, `@HACK`,
`@WORKAROUND` only warn; `@TECH-DEBT`, `@NOTE`, etc. are informational.

### Encoding policy (`pre-commit.d/02-encoding-policy.sh`)

Staged text files must be UTF-8, without a BOM, with LF line endings only. Fix with
`dos2unix <file>` / `sed -i '1s/^\xEF\xBB\xBF//' <file>` / `iconv`.

### Commit message hook (`prepare-commit-msg`)

`git commit -m "…"` is **overwritten** by the template `type(<ref>): message` (plus the staged
file list), where `<ref>` is the branch name. The intended flow: run `git commit`, let the editor
open with the pre-filled template, replace it with the real message, save. Passing `-m` is clobbered
the same way; to supply a full message programmatically, use the editor flow:

```sh
GIT_EDITOR='<script that writes your message into $1>' git commit --amend
```

### Signing & branches

- Commits are SSH-signed; treat signing as an environment-provided concern.
- Branches: `<type>/<slug>`.
- Never inspect git configuration internals: do not read, print, or search `.git/config` — nor any
  identity/signing config values (`user.*`, `commit.*`, `gpg.*`) from any source. If a commit fails
  on identity or signing, stop and ask the human instead of diagnosing configuration.

## When to Ask

- Moving or renaming a note under `docs/` (breaks inbound links across the corpus and changes
  published URLs).
- Un-commenting or restructuring the `nav:` block, or changing `site_name` / theme.
- Changing the MathJax/KaTeX wiring, `web/hooks/copy_assets.py`, or anything under `web/js/`.
- Changing `bin/` CLI contracts, generated-data paths, or the Makefile default port.
- Changing the deploy topology: `Dockerfile`, `deploy/`, `deploy.sh`, the GHCR image name, or the
  commented-out SSH deploy job. Note that `deploy/setup-server.sh` currently installs a root
  `docker-compose.yml` that is not in the repository, so bootstrap is expected to fail at that
  step.
- Pushing to `main` — it republishes `:latest` to GHCR.
