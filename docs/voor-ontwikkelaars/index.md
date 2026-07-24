# Installatie

Dit onderdeel bevat informatie voor ontwikkelaars die willen bijdragen aan de package.

## Repository-structuur

De repository-structuur volgt de [referentiedata van stelselgroepen van de VERA-standaard](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP): eerst de stelsels (bijvoorbeeld _zelfstandig_ en _onzelfstandig_) en daarbinnen de stelselgroepen (bijvoorbeeld _Energieprestatie_ en _Wasgelegenheid_).
In de folders van de stelselgroepen staat de code voor het berekenen van de punten per stelselgroep. Als bepaalde logica voor zowel zelfstandige als onzelfstandige woningen geldt, staat die in de folder _gedeelde_logica_.
De `woningwaardering`-package is zo opgezet dat stelselgroep-objecten en bijbehorende regels modulair zijn.

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

Of handmatig met geactiveerde virtualenv:

```bash
task check
```

Na code- of testwijzigingen horen pytest en beide pre-commit-stappen (inclusief `--hook-stage pre-push`) te slagen voordat je commit of de taak afrondt. Zie [testing.md](testing.md).

## Pull requests

Gebruik de PR-template in [`.github/pull_request_template.md`](../../.github/pull_request_template.md). Verwijs naar een gerelateerd issue (`Closes #123` als het issue wordt opgelost) of leg uit welke verbetering je probeert toe te voegen met je PR.
