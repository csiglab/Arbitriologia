# Laboratorium Arbitristae

> A space for prototyping ideas—researching and designing strategies to drive the technological and productive advancement of the Dominican Republic.

> This directory contains project files and prototypes developed as part of the lab's ongoing work.

## Pipeline inputs/outputs (`bin/`)

- `bin/build_clasificadores.py` reads `Clasificador-Institucional.pdf` (place it here; see `--pdf`) and writes `Clasificador-Institucional.md` + `clasificadores.xlsx` (see `--md-out` / `--xlsx-out`).
- `bin/download_datos_gob_do.sh` writes paginated API responses to `raw/` (`make download`, `DOWNLOAD_ARGS='--help'` for options).
- `bin/build_tree.py` defaults to writing `graph.png` at the repo root (`make tree TREE_OUT=...`).

`raw/` and the generated `.md`/`.xlsx` are local artifacts, not committed.

![image](https://github.com/user-attachments/assets/2a4a529e-d4ea-49e4-9f46-fe6364f86b92)