# Instructies Voor Agents

Werk in dit project voorzichtig met domeinlogica: kleine regelwijzigingen kunnen direct invloed hebben op woningwaarderingen. Wijzig alleen wat nodig is voor de taak.

## Wat Lees Je Wanneer

Lees alleen wat bij de taak hoort.

| Als de taak raakt aan                                                                                    | Lees dan eerst                                                                                                                |
| -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Puntberekening, stelsel, stelselgroep, gedeelde logica, lookuptabel of een waarschuwing die punten raakt | De relevante pagina in `docs/implementatietoelichtingen/` en de bronnen onder [Domeinregels](#domeinregels)                   |
| Outputstructuur, criterium-id's of builders                                                              | `docs/voor-ontwikkelaars/criteriumstrategie.md`, `docs/index.md` en de inline voorbeeld-output in `docs/aan-de-slag/index.md` |
| Tests of testdata                                                                                        | `docs/voor-ontwikkelaars/testing.md` en `data.md`                                                                             |
| Naamgeving                                                                                               | `docs/voor-ontwikkelaars/naamgeving.md`                                                                                       |
| Warnings of logging                                                                                      | `docs/voor-ontwikkelaars/logging.md` en `docs/index.md`                                                                       |
| Installatie, repository-opzet of releases                                                                | `docs/voor-ontwikkelaars/index.md` en `releases.md`                                                                           |
| Doel, disclaimer en actuele beleidsboek- en VERA-versies                                                 | `README.md` en `pyproject.toml`                                                                                               |
| Domeintermen in code, docs of comments                                                                   | `CONTEXT.md`                                                                                                                  |
| Typefout, formatting of eenduidige testfix zonder domeinvraag                                            | Niets extra                                                                                                                   |

## Omgeving En Commands

Zie [docs/voor-ontwikkelaars/index.md](docs/voor-ontwikkelaars/index.md) en [testing.md](docs/voor-ontwikkelaars/testing.md) voor installatie, tests en pre-commit. Kort:

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
- `woningwaardering/vera/bvg/generated.py` en `woningwaardering/vera/referentiedata/` zijn gegenereerd. Bewerk ze niet met de hand, want de generator overschrijft handmatige wijzigingen; draai in plaats daarvan `task genereer-vera-bvg-modellen` of `task genereer-vera-referentiedata`. De modeluitbreidingen in `woningwaardering/vera/bvg/model_uitbreidingen/` zijn handgeschreven en mag je wel bewerken.
- Gebruik bestaande patronen voor stelsels, stelselgroepen, criterium-id's en lookup-tabellen voordat je nieuwe abstraheringen toevoegt.
- Houd imports bovenaan het bestand; voeg geen inline imports toe.
- Gebruik `warnings.warn(..., UserWarning)` voor gebruikersgerichte waarschuwingen over incomplete of onjuiste input, volgens de bestaande warning-semantiek.
- Gebruik `loguru` voor logging volgens `docs/voor-ontwikkelaars/logging.md`.
- Gebruik comments vooral om beleidsregels herleidbaar te maken: neem waar mogelijk de relevante tekst uit het beleidsboek, de implementatietoelichting of de wettekst letterlijk op bij de bijbehorende code, met vermelding van het regelnummer/artikel.
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
- Spiegel de package-structuur waar praktisch: tests voor `woningwaardering/.../module.py` horen onder `tests/.../test_module.py`.
- Laat testfuncties beginnen met `test_`.
- Gebruik `tests/data/...` voor VERA-realistische inputmodellen en handmatig nagerekende verwachte output.
- Denk bij stelselgroepwijzigingen aan zowel detailtests voor specifieke regels als ketentests voor de hele stelselgroep wanneer dat waarde toevoegt.
- Test geen gegenereerde VERA-code alleen om coverage te verhogen.
- Laat een falende test niet slagen door de verwachte output te wijzigen of te regenereren (`task genereer-test-output` overschrijft alle bestanden in `tests/data/**/output/`): die output is handmatig nagerekend. Wijzig verwachte output alleen wanneer de punten volgens de bronnen moeten veranderen of wanneer de gebruiker er expliciet om vraagt.

## Pull Requests

- Gebruik de PR-template in [`.github/pull_request_template.md`](.github/pull_request_template.md).
- Vervang `☐` door `☑` bij invullen; gebruik geen GitHub-task-syntax (`- [ ]` / `- [x]`) — die telt mee als PR-tasks op GitHub.

## Skills

Gebruik de skill [`grill-me-with-docs`](skills/grill-me-with-docs/SKILL.md) vóór de implementatie wanneer een taak domeinlogica, puntberekening, waarschuwings- of foutgedrag of VERA-modellering wijzigt en de interpretatie van de beleidsregel of de gewenste uitkomst nog niet vaststaat. Sla de skill over bij typefouten, formatting, dependency-updates en fixes waarvan de uitkomst al vastligt.

Gebruik de skill [`huurprijscheck`](skills/huurprijscheck/SKILL.md) om een scenario door te rekenen in de rekentool van de Huurcommissie; zie [Domeinregels](#domeinregels) voor wanneer dat nodig is.

## Documentatie

- Controleer bij elke gedrags-, beleids- of datamodelwijziging of documentatie moet worden bijgewerkt.
- Let bij output-wijzigingen (punten, criteria, naming, ID-structuur) op `docs/aan-de-slag/index.md`: die bevat inline voorbeeld-output (JSON en rapport) en wordt niet automatisch meegenomen bij wijzigingen.
- Leg implementatiekeuzes rond beleidsboekregels vast in `docs/implementatietoelichtingen/`.
- Leg ontwikkelaarsafspraken vast in `docs/voor-ontwikkelaars/`.
- Houd documentatie kort en verwijs naar bestaande bronnen in plaats van dezelfde uitleg op meerdere plekken te dupliceren.
- Werk `CONTEXT.md` alleen bij wanneer een domeinterm of projectgrens duurzaam verduidelijkt is.

## Domeinregels

- Voor puntberekeningen geldt deze volgorde van autoriteit: **wettekst > online beleidsboek > huurprijscheck > implementatietoelichting**. Bij twijfel of tegenstrijdigheid is de hoger geplaatste bron leidend.
- Wettekst: zoek en citeer eerst in de lokale XML-kopie `wettelijke-documenten/BWBR0003237_2026-01-01_0.xml` en verifieer daarna tegen de officiële [online wettekst](https://wetten.overheid.nl/BWBR0003237/2026-01-01), die leidend blijft.
- Online beleidsboek: check en citeer de actuele HTML-pagina's ([zelfstandig](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-zelfstandige-woonruimte), [onzelfstandig](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-onzelfstandige-woonruimte)), niet de PDF-versie die gedurende het jaar kan achterlopen.
- Huurprijscheck: als wettekst en beleidsboek niet sluitend zijn, reken het scenario dan door met de skill [`huurprijscheck`](skills/huurprijscheck/SKILL.md) en leg de uitkomst vast in de implementatietoelichting. Verzin geen tooluitkomst: lukt het doorrekenen niet, vraag dan een mens de huurprijscheck te controleren. Is de wettekst wél eenduidig, dan blijft die leidend, ook als de tool afwijkt.
- Implementatietoelichting: onze kopie kan achterlopen op het online beleidsboek; check daarom altijd beide.
- Elke wijziging in domeinlogica citeert het regelnummer of artikel van de bron in het codecommentaar en in de sectie Bronverwijzing van de pull request, en vermeldt tegenstrijdigheden tussen bronnen.
- Geef bij elk citaat uit een online bron, in de pull request en in antwoorden aan de gebruiker, ook de link naar de pagina waar de tekst staat, zo specifiek als de bron toelaat: de rubriekpagina van het online beleidsboek of het artikel in de online wettekst.
- Maak expliciet wanneer VERA-data of het inputmodel onvoldoende is om een beleidsregel volledig te implementeren.
- Verander waarschuwing- of errorlogica niet stilzwijgend.
- Vermeld in gebruikersgerichte voorbeelden wanneer `warnings.simplefilter("default", UserWarning)` nodig is om incomplete input als warning in plaats van error te behandelen.

## Git En Veiligheid

- Revert geen bestaande wijzigingen die je niet zelf hebt gemaakt.
- Commit of push alleen wanneer de gebruiker daar expliciet om vraagt.
- Schrijf commitberichten als [Conventional Commits](https://www.conventionalcommits.org/nl/v1.0.0/) met een Nederlandse omschrijving, bijvoorbeeld `fix(onz): corrigeer maximale huurprijs bij 106 punten`. De scope is optioneel en benoemt het geraakte onderdeel (bijv. `stelsels`, `sanitair`, `rapport`, `deps`). Eén logische wijziging per commit; verwijs in de footer naar een gerelateerde issue met `Closes #N` of `Refs #N`.
- Voeg geen lokale, niet-gecommitte of organisatie-interne datastromen toe aan de publieke projectcontext.
- Commit geen secrets, credentials of lokale configuratiebestanden.
