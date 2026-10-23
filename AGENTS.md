# Instructies Voor Agents

Werk in dit project voorzichtig met domeinlogica: kleine regelwijzigingen kunnen direct invloed hebben op woningwaarderingen. Wijzig alleen wat nodig is voor de taak.

## Wat Lees Je Wanneer

| Als de taak raakt aan                                                                                    | Lees dan eerst                                                                                                                |
| -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Puntberekening, stelsel, stelselgroep, gedeelde logica, lookuptabel of een waarschuwing die punten raakt | De relevante pagina in `docs/implementatietoelichtingen/` en de bronnen onder [Domeinregels](#domeinregels)                   |
| Outputstructuur, criterium-id's of builders                                                              | `docs/voor-ontwikkelaars/criteriumstrategie.md`, `docs/index.md` en de inline voorbeeld-output in `docs/aan-de-slag/index.md` |
| Tests of testdata                                                                                        | `docs/voor-ontwikkelaars/testing.md` en `data.md`                                                                             |
| Naamgeving                                                                                               | `docs/voor-ontwikkelaars/naamgeving.md`                                                                                       |
| Warnings of logging                                                                                      | `docs/voor-ontwikkelaars/logging.md` en `docs/index.md`                                                                       |
| Installatie, repository-opzet of releases                                                                | `docs/voor-ontwikkelaars/index.md` en `releases.md`                                                                           |
| Domeintermen in code, docs of comments                                                                   | `GLOSSARY.md`                                                                                                                 |
| Triviale fix: typefout, formatting of eenduidige testfix zonder domeinvraag                              | Niets extra                                                                                                                   |

## Omgeving En Commands

Zie [docs/voor-ontwikkelaars/index.md](docs/voor-ontwikkelaars/index.md) voor installatie, tests en pre-commit. Kort:

- Gebruik een Python-versie die voldoet aan `requires-python` in `pyproject.toml`.
- Gebruik [uv](https://docs.astral.sh/uv/) voor dependency management; installeer ontwikkelaarsdependencies met `uv sync --extra dev`.
- Activeer `.venv` voordat je Python-code, tests of scripts draait (of gebruik `uv run`).
- Tasks: zie `taskfile.yml`
- Run tests: `uv run python -m pytest`
- Run commit-checks: `uv run pre-commit run --all-files`
- Run pre-push checks: `uv run pre-commit run --all-files --hook-stage pre-push`

## Codeconventies

Codeconventies staan in [`CODING_STANDARDS.md`](CODING_STANDARDS.md) en worden bij review afgedwongen. Houd tijdens het implementeren in elk geval rekening met:

- Citeer bij beleidslogica de bron (beleidsboek, implementatietoelichting of wettekst) letterlijk in een comment, met regelnummer/artikel; zie het voorbeeld in `CODING_STANDARDS.md`.
- Bouw de output van een stelselgroep op met de builders in `woningwaardering/stelsels/builders.py`; zie `docs/voor-ontwikkelaars/criteriumstrategie.md`.

## Tests

- Na code- of testwijzigingen: draai pytest en beide pre-commit-stappen vóór elke commit en voordat je de taak afrondt:

```bash
uv run python -m pytest
uv run pre-commit run --all-files
uv run pre-commit run --all-files --hook-stage pre-push
```

- Lees [testing.md](docs/voor-ontwikkelaars/testing.md) voordat je een test schrijft of wijzigt: daar staat welke soort test je nodig hebt en hoe je hem opbouwt.

### Verwachte output

De verwachte output van de tests staat op twee plekken: de testreferenties (`tests/**/testreferenties/*.md`) en `tests/docs/output_json_*.json`. `task genereer-test-output` overschrijft ze allebei. Daarna slaagt elke vergelijking, ook als de output fout is: een groene suite zegt dan alleen dat de verwachte output is meegeschoven, niet dat de code klopt.

- Draai `task genereer-test-output` wanneer uit de taak blijkt dat de output gaat wijzigen (punten, namen, criterium-id's, rapport), zoals bij een bugfix voor verkeerde punten, of wanneer de gebruiker vooraf heeft gezegd dat de output mag wijzigen. Een nieuwe test heeft nog geen verwachte output en valt hier ook onder.
- Bekijk daarna de diff: alleen de verwachte output die de taak hoort te raken is gewijzigd. Is er meer gewijzigd, zet die bestanden dan terug.
- Wijkt een test af terwijl de taak geen outputwijziging voorziet: herstel de code en laat de verwachte output zoals hij was. Kom je er niet uit, laat de test dan rood en meld welke test afwijkt, wat er verschilt en wat volgens jou de oorzaak is.
- Werk verwachte output alleen bij met `task genereer-test-output`; bewerk die bestanden niet met de hand. Een bestand verwijderen mag alleen wanneer de bijbehorende test of het bijbehorende model bewust is verwijderd of hernoemd.
- Meld in je eindbericht en in de PR-beschrijving welke verwachte output is gewijzigd en waarom.

## Pull Requests

- Geef de PR-titel de vorm van een Conventional Commit, zoals bij commitberichten. Het type bepaalt het label en daarmee de rubriek in de release notes; zie [releases.md](docs/voor-ontwikkelaars/releases.md#labels-en-release-notes).
- Gebruik de PR-template in [`.github/pull_request_template.md`](.github/pull_request_template.md).
- Vervang `☐` door `☑` bij invullen; gebruik geen GitHub-task-syntax (`- [ ]` / `- [x]`) — die telt mee als PR-tasks op GitHub.
- Push je naar een branch met een open pull request, werk dan in dezelfde beurt de titel en beschrijving bij als die de wijziging nog niet dekken. Pas alleen aan wat door de push verandert en laat tekst van anderen staan.

## Skills

De [Matt Pocock-skills](https://github.com/mattpocock/skills) staan vastgezet op een tag in `.claude/skills/`; zie [Agent skills](docs/voor-ontwikkelaars/index.md#agent-skills) voor upgraden.

Grill **vroeg en proactief** wanneer de taak meer is dan een eenduidige, lokale wijziging. `/grill-with-docs` kan alleen de gebruiker starten; als agent start je zelf de skills die het aanroept: `grilling` en `domain-modeling`. Triggers (niet exhaustief):

- plannen, ontwerpen, architectuur of refactor-voorstellen
- domeinlogica, stelselgroepen, beleidsregel-interpretatie of VERA-modellering
- nieuwe features, gedragswijzigingen, waarschuwingen of onduidelijke requirements
- terminologie, projectgrenzen of documentatie die moet worden aangescherpt

Sla grillen over bij een triviale fix. Tijdens het grillen zijn wettekst, beleidsboek en implementatietoelichting feiten die je zelf opzoekt en citeert volgens [Domeinregels](#domeinregels).

Is de interpretatie of implementatiestatus van een beleidsregel beslist, bied dan aan de betreffende pagina in `docs/implementatietoelichtingen/` bij te werken, met letterlijk geciteerde bron (beleidsboek/wettekst), in plaats van een ADR. ADR's zijn voor technische en architectuurbeslissingen.

Waar een skill botst met dit bestand, gaat dit bestand voor:

- `/pr`: volg de PR-template. Zet de visual en het voor/na-bewijs uit `/pr` onder **Samenvatting**, met het oordeel one-way/two-way door.
- Issues en specs (`/to-spec`, `/to-tickets`, `/triage`): volg de conventies in `docs/agents/issue-tracker.md`.

## Agent skills

### Issue tracker

Issues staan als GitHub issues in `woonstadrotterdam/woningwaardering` (`gh` CLI). See `docs/agents/issue-tracker.md`.

### Triage labels

Standaardlabels: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: `GLOSSARY.md` + `docs/adr/` in de repo-root. See `docs/agents/domain.md`.

## Documentatie

- Controleer bij elke gedrags-, beleids- of datamodelwijziging of documentatie moet worden bijgewerkt.
- Let bij output-wijzigingen (punten, criteria, naming, ID-structuur) op `docs/aan-de-slag/index.md`: die bevat inline voorbeeld-output (JSON en rapport) en wordt niet automatisch meegenomen bij wijzigingen.
- Leg implementatiekeuzes rond beleidsboekregels vast in `docs/implementatietoelichtingen/`.
- Leg ontwikkelaarsafspraken vast in `docs/voor-ontwikkelaars/`.
- Houd documentatie kort en verwijs naar bestaande bronnen in plaats van dezelfde uitleg op meerdere plekken te dupliceren.
- Werk `GLOSSARY.md` alleen bij wanneer een domeinterm duurzaam verduidelijkt is. Neem alleen termen op die betekenisvol zijn voor domeinexperts of terugkerend nodig zijn om code en documentatie te begrijpen; houd definities op één à twee zinnen, zonder implementatiedetails (die horen in `docs/voor-ontwikkelaars/` of codecommentaar).

## Domeinregels

- Volg voor puntberekeningen de volgorde van autoriteit in [`docs/voor-ontwikkelaars/bronnen.md`](docs/voor-ontwikkelaars/bronnen.md), ook voor de huurprijscheck. Vermeld tegenstrijdigheden tussen bronnen.
- Wettekst: zoek en citeer eerst in de lokale XML-kopie `wettelijke-documenten/BWBR0003237_2026-01-01_0.xml` en verifieer daarna tegen de officiële [online wettekst](https://wetten.overheid.nl/BWBR0003237/2026-01-01), die leidend blijft.
- Online beleidsboek: check en citeer de actuele HTML-pagina's ([zelfstandig](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-zelfstandige-woonruimte), [onzelfstandig](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-onzelfstandige-woonruimte)), niet de PDF-versie die gedurende het jaar kan achterlopen.
- Implementatietoelichting: onze kopie kan achterlopen op het online beleidsboek; check daarom altijd beide.
- Huurprijscheck: geven wettekst en beleidsboek geen uitsluitsel, reken het scenario dan door met de skill [`huurprijscheck`](skills/huurprijscheck/SKILL.md).
- Geef bij een citaat uit een online bron, ook in antwoorden aan de gebruiker, de link naar de pagina waar de tekst staat (de rubriekpagina van het online beleidsboek of het artikel in de online wettekst), zodat de lezer op de tekst reageert en niet op jouw samenvatting.
- Maak expliciet wanneer VERA-data of het inputmodel onvoldoende is om een beleidsregel volledig te implementeren.
- Verander waarschuwing- of errorlogica niet stilzwijgend.
- Vermeld in gebruikersgerichte voorbeelden wanneer `warnings.simplefilter("default", UserWarning)` nodig is om incomplete input als warning in plaats van error te behandelen.

## Git En Veiligheid

- Revert geen bestaande wijzigingen die je niet zelf hebt gemaakt.
- Push alleen wanneer de gebruiker daar expliciet om vraagt.
- Schrijf commitberichten als [Conventional Commits](https://www.conventionalcommits.org/nl/v1.0.0/) met een Nederlandse omschrijving, bijvoorbeeld `fix(onz): corrigeer maximale huurprijs bij 106 punten`. De scope is optioneel en benoemt het geraakte onderdeel (bijv. `stelsels`, `sanitair`, `rapport`, `deps`). Eén logische wijziging per commit; verwijs in de footer naar een gerelateerde issue met `Closes #N` of `Refs #N`.
- Noem een branch `<type>/<korte-omschrijving>` in kebab-case, met hetzelfde Conventional Commits-type als de wijziging (`feat`, `fix`, `docs`, `chore`, `refactor`, ...) en waar van toepassing het issuenummer, bijvoorbeeld `fix/399-toiletruimte-classificatie`. Uitzondering: de `prototype/<naam>`-branches van `/prototype`. Push geen branch met een tool-prefix zoals `claude/` of `cursor/`: hernoem die vóór de eerste push.
- Voeg geen lokale, niet-gecommitte of organisatie-interne datastromen toe aan de publieke projectcontext.
- Commit geen secrets, credentials of lokale configuratiebestanden.
