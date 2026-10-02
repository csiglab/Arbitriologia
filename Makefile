# Load local defaults from .env (e.g. ARBITRIOLOGIA_PORT); real exported
# env vars and `make VAR=...` overrides still win. Missing .env is not
# an error. The include is skipped when ARBITRIOLOGIA_PORT already has a
# non-file origin, since a makefile assignment would otherwise shadow it.
ifeq ($(origin ARBITRIOLOGIA_PORT), undefined)
-include .env
endif
export

PYTHON ?= python3
# Single port concept: .env (or exported env) sets ARBITRIOLOGIA_PORT,
# default 8080. PORT stays as a per-invocation override for deploy-local.
ARBITRIOLOGIA_PORT ?= 8080
ifeq ($(strip $(ARBITRIOLOGIA_PORT)),)
override ARBITRIOLOGIA_PORT := 8080
endif
PORT ?= $(ARBITRIOLOGIA_PORT)
IMAGE := ghcr.io/csiglab/arbitriologia:latest
CONTAINER := arbitriologia
DOMAIN ?= arbitriologia.example.com
EMAIL ?=
CLASIFICADOR_PDF ?= data/Clasificador-Institucional.pdf
TREE_OUT ?= graph.png
TEXT ?= example title
DOWNLOAD_ARGS ?=

.PHONY: help build serve dev deploy-local deploy-server setup-server clasificador download tree slugify clean

help:
	@echo "build         build the mkdocs site (delegates to build.sh, uv + .venv)"
	@echo "serve         preview the site locally on 127.0.0.1:$(ARBITRIOLOGIA_PORT)"
	@echo "dev           preview with live reload on 127.0.0.1:$(ARBITRIOLOGIA_PORT)"
	@echo "deploy-local  build docker image and run it locally on PORT=$(PORT)"
	@echo "deploy-server pull $(IMAGE) and run it (delegates to deploy.sh)"
	@echo "setup-server  one-time server bootstrap (DOMAIN=$(DOMAIN) EMAIL=$(EMAIL))"
	@echo "clasificador  extract institutional rows to data/clasificadores.xlsx"
	@echo "download      fetch datos.gob.do metadata into data/raw/ (DOWNLOAD_ARGS='--help')"
	@echo "tree          render institutional-code graph to $(TREE_OUT)"
	@echo "slugify       slugify TEXT='$(TEXT)'"
	@echo "clean         remove pycache artifacts + web/site + generated bin outputs"

build:
	bash build.sh

serve:
	uv run --project . mkdocs serve -f web/mkdocs.yml -a 127.0.0.1:$(ARBITRIOLOGIA_PORT)

dev:
	uv run --project . mkdocs serve -f web/mkdocs.yml -a 127.0.0.1:$(ARBITRIOLOGIA_PORT) --dirtyreload

deploy-local:
	docker build -t arbitriologia .
	docker rm -f $(CONTAINER) 2>/dev/null || true
	docker run -d --name $(CONTAINER) --restart unless-stopped -p $(PORT):80 arbitriologia

deploy-server:
	bash deploy.sh

setup-server:
	sudo bash deploy/setup-server.sh $(DOMAIN) $(EMAIL)

clasificador:
	uv run --project . python3 bin/build_clasificadores.py --pdf $(CLASIFICADOR_PDF)

download:
	bash bin/download_datos_gob_do.sh $(DOWNLOAD_ARGS)

tree:
	uv run --project . python3 bin/build_tree.py --out $(TREE_OUT) --print-nodes

slugify:
	uv run --project . python3 bin/slugify_text.py $(TEXT)

clean:
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -type d -exec rm -r {} + 2>/dev/null || true
	rm -rf web/site
	rm -f graph.png data_*.json
	rm -f data/Clasificador-Institucional.md data/clasificadores.xlsx
