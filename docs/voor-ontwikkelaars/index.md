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

## Tests en checks

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
