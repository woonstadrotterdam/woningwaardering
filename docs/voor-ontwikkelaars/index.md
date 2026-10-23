# Voor ontwikkelaars

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

Hiermee worden hooks voor `git commit` en `git push` geïnstalleerd (zoals in [`.pre-commit-config.yaml`](https://github.com/woonstadrotterdam/woningwaardering/blob/main/.pre-commit-config.yaml)). Zonder deze stap draaien er bij commit of push geen lokale checks; dezelfde checks draaien dan pas in CI.

Na wijzigingen in `.pre-commit-config.yaml` volstaat meestal opnieuw committen of pushen; bij twijfel `uv run pre-commit install` opnieuw uitvoeren.

## Agent skills

We gebruiken de [Matt Pocock-skills](https://github.com/mattpocock/skills), vastgezet op een tag. De skills staan gecommit in `.claude/skills/`; de versie per skill staat in `skills-lock.json`. Die versie moet passen bij de bestanden die `/setup-matt-pocock-skills` in de repo zet (`docs/agents/` en het blok `## Agent skills` in `AGENTS.md`). Claude Code en Cursor lezen de skills direct uit `.claude/skills/`; je hoeft niets te installeren.

De agentinstructies staan alleen in [`AGENTS.md`](https://github.com/woonstadrotterdam/woningwaardering/blob/main/AGENTS.md); er is geen `CLAUDE.md`. Claude Code leest `AGENTS.md` direct vanaf v2.1.277, dus houd Claude Code bijgewerkt (`claude update`).

Installeer de skills niet daarnaast als Claude Code-plugin of via `npx skills add -g`; dan staan ze dubbel of laadt een andere versie. [`.claude/settings.json`](https://github.com/woonstadrotterdam/woningwaardering/blob/main/.claude/settings.json) zet de plugins `mattpocock-skills@mattpocock` en `mattpocock-skills@claude-plugins-official` daarom uit.

Upgraden: lees de [changelog](https://github.com/mattpocock/skills/blob/main/CHANGELOG.md), installeer de nieuwe tag met `npx skills add mattpocock/skills#<tag> -a claude-code`, draai zo nodig `/setup-matt-pocock-skills` opnieuw en commit `.claude/skills/`, `skills-lock.json` en de bestanden van de setup-skill samen.

We gebruiken niet alle skills uit de set. `setup-pre-commit`, `migrate-to-shoehorn`, `setup-ts-deep-modules` en `scaffold-exercises` zijn bedoeld voor JavaScript/TypeScript-projecten of cursusmateriaal en staan bewust niet in de repo. Een agent kan ze uit zichzelf starten, dus verwijder ze na het upgraden weer uit `.claude/skills/` en `skills-lock.json`.

Repo-specifieke aanvullingen op de skills staan in de sectie `## Skills` van `AGENTS.md`, in `docs/agents/domain.md` en in `docs/agents/issue-tracker.md` (sectie `## Issue content`), nooit in de skills uit `skills-lock.json` (een upgrade overschrijft die). Skills van deze repo zelf, zoals `huurprijscheck`, staan ernaast in `.claude/skills/` en staan niet in `skills-lock.json`. Controleer na een upgrade dat ze er nog staan. `/setup-matt-pocock-skills` schrijft `docs/agents/` opnieuw: controleer na het draaien de diff en herstel de repo-specifieke leeslijst en issueconventies.

## Tests en checks

Met geïnstalleerde pre-commit-hooks draaien commit- en push-checks automatisch.

Of handmatig met geactiveerde virtualenv:

```bash
task check
```

Na code- of testwijzigingen horen pytest en beide pre-commit-stappen (inclusief `--hook-stage pre-push`) te slagen voordat je commit of de taak afrondt. Zie [testing.md](testing.md).

## Pull requests

Gebruik de PR-template in [`.github/pull_request_template.md`](https://github.com/woonstadrotterdam/woningwaardering/blob/main/.github/pull_request_template.md). Verwijs naar een gerelateerd issue (`Closes #123` als het issue wordt opgelost) of leg uit welke verbetering je probeert toe te voegen met je PR.
