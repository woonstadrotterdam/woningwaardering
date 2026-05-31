# Installatie

Dit onderdeel bevat informatie voor ontwikkelaars die willen bijdragen aan de package.

## Vereisten

- Python-versie volgens `requires-python` in `pyproject.toml`
- [uv](https://docs.astral.sh/uv/getting-started/installation/) voor dependency management

## Project opzetten

```bash
git clone https://github.com/woonstadrotterdam/woningwaardering.git
cd woningwaardering
uv sync --extra dev
```

`uv sync` maakt of bijwerkt `.venv` en installeert de package inclusief de `[dev]`-extras uit `pyproject.toml`.

Voor interactief werk in de shell:

```bash
source .venv/bin/activate
```

## Pre-commit

`uv sync --extra dev` installeert het `pre-commit`-programma in `.venv`, maar **registreert geen git-hooks**. Doe dat eenmalig per clone (of nieuwe werkmap):

```bash
uv run pre-commit install
```

Hiermee worden hooks voor `git commit` en `git push` geïnstalleerd (zoals in [`.pre-commit-config.yaml`](../../.pre-commit-config.yaml)). Zonder deze stap draaien er bij commit of push geen lokale checks; dezelfde checks draaien dan pas in CI.

Na wijzigingen in `.pre-commit-config.yaml` volstaat meestal opnieuw committen of pushen; bij twijfel `uv run pre-commit install` opnieuw uitvoeren.

## Tests en checks

Met geïnstalleerde pre-commit-hooks draaien commit- en push-checks automatisch.

Met geactiveerde virtualenv:

```bash
python -m pytest
pre-commit run --all-files
pre-commit run --all-files --hook-stage pre-push
```

Zonder activatie, via `uv run`:

```bash
uv run python -m pytest
uv run pre-commit run --all-files
uv run pre-commit run --all-files --hook-stage pre-push
```

Na code- of testwijzigingen horen pytest en beide pre-commit-stappen (inclusief `--hook-stage pre-push`) te slagen voordat je commit of de taak afrondt. Zie [testing.md](testing.md).

## Pull requests

Gebruik de PR-template in [`.github/pull_request_template.md`](../../.github/pull_request_template.md). Verwijs naar een gerelateerd issue (`Closes #123` als het issue wordt opgelost) of leg uit welke verbetering je probeert toe te voegen met je PR.
