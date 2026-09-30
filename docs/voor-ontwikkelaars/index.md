# Voor ontwikkelaars

Dit onderdeel bevat informatie voor ontwikkelaars die willen bijdragen aan de package.

## Repository-structuur

De repository-structuur volgt de [referentiedata van stelselgroepen van de VERA-standaard](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP): eerst de stelsels (bijvoorbeeld *zelfstandig* en *onzelfstandig*) en daarbinnen de stelselgroepen (bijvoorbeeld *Energieprestatie* en *Wasgelegenheid*).
In de folders van de stelselgroepen staat de code voor het berekenen van de punten per stelselgroep. Als bepaalde logica voor zowel zelfstandige als onzelfstandige woningen geldt, staat die in de folder *gedeelde_logica*.
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

Hiermee worden hooks voor `git commit` en `git push` geïnstalleerd (zoals in `[.pre-commit-config.yaml](https://github.com/woonstadrotterdam/woningwaardering/blob/main/.pre-commit-config.yaml)`). Zonder deze stap draaien er bij commit of push geen lokale checks; dezelfde checks draaien dan pas in CI.

Na wijzigingen in `.pre-commit-config.yaml` volstaat meestal opnieuw committen of pushen; bij twijfel `uv run pre-commit install` opnieuw uitvoeren.

## Tests en checks

Met geïnstalleerde pre-commit-hooks draaien commit- en push-checks automatisch.

Of handmatig met geactiveerde virtualenv:

```bash
task check
```

Na code- of testwijzigingen horen pytest en beide pre-commit-stappen (inclusief `--hook-stage pre-push`) te slagen voordat je commit of de taak afrondt. Zie [testing.md](testing.md).

## Pull requests

Gebruik de PR-template in `[.github/pull_request_template.md](https://github.com/woonstadrotterdam/woningwaardering/blob/main/.github/pull_request_template.md)`. Verwijs naar een gerelateerd issue (`Closes #123` als het issue wordt opgelost) of leg uit welke verbetering je probeert toe te voegen met je PR.

### Bugbot

[Cursor Bugbot](https://cursor.com/docs/bugbot) kan pull requests reviewen. Projectregels staan in `[.cursor/BUGBOT.md](https://github.com/woonstadrotterdam/woningwaardering/blob/main/.cursor/BUGBOT.md)` (altijd meegenomen) en in geneste bestanden zoals `[woningwaardering/stelsels/.cursor/BUGBOT.md](https://github.com/woonstadrotterdam/woningwaardering/blob/main/woningwaardering/stelsels/.cursor/BUGBOT.md)` en `[woningwaardering/vera/.cursor/BUGBOT.md](https://github.com/woonstadrotterdam/woningwaardering/blob/main/woningwaardering/vera/.cursor/BUGBOT.md)` (meegenomen wanneer bestanden onder die mappen wijzigen).

Eenmalig: koppel GitHub via de Cursor-integratie en zet Bugbot aan voor deze repository in het [Bugbot-dashboard](https://cursor.com/dashboard/bugbot).

Bugbot draait handmatig door `cursor review` of `bugbot run` op de PR te commenten. Op GitHub verschijnt de check `Cursor Bugbot` (bevindingen zijn standaard `neutral`, niet `failure`).

### Cloud Agents

[Cursor Cloud Agents](https://cursor.com/docs/cloud-agent) draaien in geïsoleerde cloud-VM's en kunnen code schrijven, tests draaien en een PR openen. Cursor raadt [agent-driven setup](https://cursor.com/docs/cloud-agent/setup) vanuit het [Cloud Agents dashboard](https://cursor.com/dashboard/cloud-agents#environments) aan; commit eventueel later `.cursor/environment.json` als je de omgeving als code wilt vastleggen.

Eenmalig: koppel GitHub via de [Cursor GitHub-integratie](https://cursor.com/docs/integrations/github) en zorg dat de repository toegankelijk is voor Cloud Agents.

Repo-specifieke cloud-instructies staan in `[AGENTS.md](https://github.com/woonstadrotterdam/woningwaardering/blob/main/AGENTS.md)` onder **Cursor Cloud specific instructions**. Zie ook de [Cloud Agent best practices](https://cursor.com/docs/cloud-agent/best-practices).