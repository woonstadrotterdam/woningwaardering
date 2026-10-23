# Instructies Voor Agents

Werk in dit project voorzichtig met domeinlogica: kleine regelwijzigingen kunnen direct invloed hebben op woningwaarderingen. Lees eerst de relevante context en wijzig alleen wat nodig is voor de taak.

## Eerst Lezen

- Lees `GLOSSARY.md` voor de gedeelde domeintaal.
- Lees `README.md` voor doel, disclaimer en actuele beleidsboek- en VERA-ankers.
- Lees `docs/index.md` voor de gebruikersgerichte uitleg van warnings en outputstructuur.
- Lees `docs/voor-ontwikkelaars/` voor repository-opzet, lookup-tabellen, logging/warnings en de criteriumstrategie.
- Lees bij wijzigingen in domeinlogica eerst de relevante pagina's in `docs/implementatietoelichtingen/`.
- Check en citeer de actuele HTML-pagina's van het online beleidsboek ([zelfstandig](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-zelfstandige-woonruimte), [onzelfstandig](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-onzelfstandige-woonruimte)), niet de PDF-versie die gedurende het jaar kan achterlopen.
- Gebruik voor de wettekst eerst de lokale XML-kopie `wettelijke-documenten/BWBR0003237_2026-01-01_0.xml` om te zoeken en citeren. Verifieer deze daarna tegen de officiële [online wettekst](https://wetten.overheid.nl/BWBR0003237/2026-01-01), die leidend blijft.
- Pas daarna code aan. Zie `docs/voor-ontwikkelaars/bronnen.md` voor de relatie tussen deze bronnen. Dit geldt onder meer voor stelsels, gedeelde logica, lookup-tabellen en waarschuwingen die punten raken.
- Lees bij ontwikkelwerk de relevante pagina in `docs/voor-ontwikkelaars/`, vooral `naamgeving.md`, `data.md` en `logging.md`.

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

- Volg de VERA-referentiedata voor naamgeving van stelsels en stelselgroepen.
- Plaats stelselgroep-logica in de map van het juiste stelsel onder `woningwaardering/stelsels/`.
- Plaats logica die door meerdere stelsels gedeeld wordt in `woningwaardering/stelsels/gedeelde_logica/`.
- Bouw de output van een stelselgroep op met de builders in `woningwaardering/stelsels/builders.py` (`met_onderliggend` / `met_subgroep` / `gedeeld_met`); zie `docs/voor-ontwikkelaars/criteriumstrategie.md` voor de criteriumstrategie.
- Behandel gegenereerde code onder `woningwaardering/vera/` terughoudend. Wijzig deze alleen via de bestaande scripts of wanneer de taak daar expliciet om vraagt.
- Gebruik bestaande patronen voor stelsels, stelselgroepen, criterium-id's en lookup-tabellen voordat je nieuwe abstraheringen toevoegt.
- Houd imports bovenaan het bestand; voeg geen inline imports toe.
- Gebruik `warnings.warn(..., UserWarning)` voor gebruikersgerichte waarschuwingen over incomplete of onjuiste input, volgens de bestaande warning-semantiek.
- Gebruik `loguru` voor logging volgens `docs/voor-ontwikkelaars/logging.md`.
- Gebruik comments vooral om beleidsregels herleidbaar te maken: neem waar mogelijk de relevante tekst uit het beleidsboek, de implementatietoelichting of de [wettekst](https://wetten.overheid.nl/BWBR0003237/2026-01-01) letterlijk op bij de bijbehorende code, met vermelding van het regelnummer/artikel.
- Schrijf comments voor de lezer van de huidige code, niet voor de reviewer van de wijziging: verwijs niet naar verwijderde of oude code ("dit is niet meer nodig", "voorheen gebeurde hier X"). Zulke uitleg hoort in het commitbericht of de PR-beschrijving.

```python
# 2.2.2.3 Zolderruimte zonder vaste trap
# Als een zolderruimte geen vertrek is maar wel als overige ruimte kan worden
# aangemerkt en er is geen vaste trap naar de zolder, dan worden er 5 punten
# afgetrokken van de waarde die aan het vloeroppervlak wordt toegekend.
if (
    ruimte.detail_soort == Ruimtedetailsoort.zolder
    and heeft_bouwkundig_element(ruimte, Bouwkundigelementdetailsoort.vlizotrap)
    and classificeer_ruimte(ruimte) == Ruimtesoort.overige_ruimten
):
    ...
```

## Tests

- Na code- of testwijzigingen: draai pytest en beide pre-commit-stappen voordat je de taak afrondt of de gebruiker vraagt om te committen:

```bash
uv run python -m pytest
uv run pre-commit run --all-files
uv run pre-commit run --all-files --hook-stage pre-push
```

- Voeg passende tests toe bij nieuwe of gewijzigde code.
- Lees [testing.md](docs/voor-ontwikkelaars/testing.md) voordat je een test schrijft of wijzigt: daar staat welke soort test je nodig hebt en hoe je hem opbouwt.
- Spiegel de package-structuur waar praktisch: tests voor `woningwaardering/.../module.py` horen onder `tests/.../test_module.py`.
- Laat testfuncties beginnen met `test_`.
- Test geen gegenereerde VERA-code alleen om coverage te verhogen.

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

## Skills

De [Matt Pocock-skills](https://github.com/mattpocock/skills) staan vastgezet op een tag in `.claude/skills/`; zie [Agent skills](docs/voor-ontwikkelaars/index.md#agent-skills) voor upgraden.

Gebruik `/grill-with-docs` **vroeg en proactief** wanneer de taak meer is dan een eenduidige, lokale wijziging. Triggers (niet exhaustief):

- plannen, ontwerpen, architectuur of refactor-voorstellen
- domeinlogica, stelselgroepen, beleidsregel-interpretatie of VERA-modellering
- nieuwe features, gedragswijzigingen, waarschuwingen of onduidelijke requirements
- terminologie, projectgrenzen of documentatie die moet worden aangescherpt

Stel eerst verhelderende vragen (één tegelijk) en check tegen `GLOSSARY.md`, implementatietoelichtingen, online beleidsboek/wettekst en code. Sla over bij triviale fixes (typo's, formatting, eenduidige testfixes zonder domeinvraag).

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

- Behandel voor puntberekeningen de volgorde van autoriteit in `docs/voor-ontwikkelaars/bronnen.md`: [wettekst](https://wetten.overheid.nl/BWBR0003237/2026-01-01) > online beleidsboek ([zelfstandig](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-zelfstandige-woonruimte), [onzelfstandig](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-onzelfstandige-woonruimte)) > huurprijscheck > implementatietoelichting. Agents kunnen de huurprijscheck niet raadplegen; als wettekst en beleidsboek niet sluitend zijn, vraag een mens de tool te controleren en leg de uitkomst vast in de implementatietoelichting. Check zowel onze implementatietoelichting als het actuele online beleidsboek, omdat onze kopie kan achterlopen. Indien er tegenstrijdigheden in deze bronnen staan, vermeld dit.
- Maak expliciet wanneer VERA-data of het inputmodel onvoldoende is om een beleidsregel volledig te implementeren.
- Verander waarschuwing- of errorlogica niet stilzwijgend.
- Vermeld in gebruikersgerichte voorbeelden wanneer `warnings.simplefilter("default", UserWarning)` nodig is om incomplete input als warning in plaats van error te behandelen.

## Git En Veiligheid

- Revert geen bestaande wijzigingen die je niet zelf hebt gemaakt.
- Commit of push alleen wanneer de gebruiker daar expliciet om vraagt.
- Schrijf commitberichten als [Conventional Commits](https://www.conventionalcommits.org/nl/v1.0.0/) met een Nederlandse omschrijving, bijvoorbeeld `fix(onz): corrigeer maximale huurprijs bij 106 punten`. De scope is optioneel en benoemt het geraakte onderdeel (bijv. `stelsels`, `sanitair`, `rapport`, `deps`). Eén logische wijziging per commit; verwijs in de footer naar een gerelateerde issue met `Closes #N` of `Refs #N`.
- Voeg geen lokale, niet-gecommitte of organisatie-interne datastromen toe aan de publieke projectcontext.
- Commit geen secrets, credentials of lokale configuratiebestanden.
