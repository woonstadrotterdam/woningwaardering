# Instructies Voor Agents

Werk in dit project voorzichtig met domeinlogica: kleine regelwijzigingen kunnen direct invloed hebben op woningwaarderingen. Lees eerst de relevante context en wijzig alleen wat nodig is voor de taak.

## Eerst Lezen

- Lees `CONTEXT.md` voor de gedeelde domeintaal.
- Lees `README.md` voor doel, disclaimer en actuele beleidsboek- en VERA-ankers.
- Lees `docs/introductie/opzet.md` voor repository-opzet, warnings, lookup-tabellen en criterium-id's.
- Lees bij wijzigingen in domeinlogica eerst de relevante pagina's in `docs/implementatietoelichtingen/`, check tegen het online beleidsboek ([zelfstandig](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-zelfstandige-woonruimte), [onzelfstandig](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-onzelfstandige-woonruimte)) en de [wettekst](https://wetten.overheid.nl/BWBR0003237/2026-01-01#Artikel6), en pas daarna code aan. Zie `CONTEXT.md` voor de relatie tussen deze bronnen. Dit geldt onder meer voor stelsels, gedeelde logica, lookup-tabellen en waarschuwingen die punten raken.
- Lees bij ontwikkelwerk de relevante pagina in `docs/voor-ontwikkelaars/`, vooral `testing.md`, `naamgeving.md`, `data.md` en `logging.md`.

## Omgeving En Commands

Zie [docs/voor-ontwikkelaars/index.md](docs/voor-ontwikkelaars/index.md) en [testing.md](docs/voor-ontwikkelaars/testing.md) voor installatie, tests en pre-commit. Kort:

- Gebruik een Python-versie die voldoet aan `requires-python` in `pyproject.toml`.
- Gebruik [uv](https://docs.astral.sh/uv/) voor dependency management; installeer ontwikkelaarsdependencies met `uv sync --extra dev`.
- Activeer `.venv` voordat je Python-code, tests of scripts draait (of gebruik `uv run`).
- Run tests: `uv run python -m pytest`
- Run commit-checks: `uv run pre-commit run --all-files`
- Run pre-push checks: `uv run pre-commit run --all-files --hook-stage pre-push`

## Codeconventies

- Volg de VERA-referentiedata voor naamgeving van stelsels en stelselgroepen.
- Plaats stelselgroep-logica in de map van het juiste stelsel onder `woningwaardering/stelsels/`.
- Plaats logica die door meerdere stelsels gedeeld wordt in `woningwaardering/stelsels/gedeelde_logica/`.
- Behandel gegenereerde code onder `woningwaardering/vera/` terughoudend. Wijzig deze alleen via de bestaande scripts of wanneer de taak daar expliciet om vraagt.
- Gebruik bestaande patronen voor stelsels, stelselgroepen, criterium-id's en lookup-tabellen voordat je nieuwe abstraheringen toevoegt.
- Houd imports bovenaan het bestand; voeg geen inline imports toe.
- Gebruik `warnings.warn(..., UserWarning)` voor gebruikersgerichte waarschuwingen over incomplete of onjuiste input, volgens de bestaande warning-semantiek.
- Gebruik `loguru` voor logging volgens `docs/voor-ontwikkelaars/logging.md`.
- Gebruik comments vooral om beleidsregels herleidbaar te maken: neem waar mogelijk de relevante tekst uit het beleidsboek, de implementatietoelichting of de [wettekst](https://wetten.overheid.nl/BWBR0003237/2026-01-01#Artikel6) letterlijk op bij de bijbehorende code, met vermelding van het regelnummer/artikel.

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

## Pull Requests

- Gebruik de PR-template in [`.github/pull_request_template.md`](.github/pull_request_template.md).
- Vervang `☐` door `☑` bij invullen; gebruik geen GitHub-task-syntax (`- [ ]` / `- [x]`) — die telt mee als PR-tasks op GitHub.

## Skills

Gebruik [`.cursor/skills/grill-me-with-docs/SKILL.md`](.cursor/skills/grill-me-with-docs/SKILL.md) **vroeg en proactief** wanneer de taak meer is dan een eenduidige, lokale wijziging. Triggers (niet exhaustief):

- plannen, ontwerpen, architectuur of refactor-voorstellen
- domeinlogica, stelselgroepen, beleidsregel-interpretatie of VERA-modellering
- nieuwe features, gedragswijzigingen, waarschuwingen of onduidelijke requirements
- terminologie, projectgrenzen of documentatie die moet worden aangescherpt

Stel eerst verhelderende vragen (één tegelijk) en check tegen `CONTEXT.md`, implementatietoelichtingen, online beleidsboek/wettekst en code. Sla over bij triviale fixes (typo's, formatting, eenduidige testfixes zonder domeinvraag).

## Documentatie

- Controleer bij elke gedrags-, beleids- of datamodelwijziging of documentatie moet worden bijgewerkt.
- Leg implementatiekeuzes rond beleidsboekregels vast in `docs/implementatietoelichtingen/`.
- Leg ontwikkelaarsafspraken vast in `docs/voor-ontwikkelaars/`.
- Houd documentatie kort en verwijs naar bestaande bronnen in plaats van dezelfde uitleg op meerdere plekken te dupliceren.
- Werk `CONTEXT.md` alleen bij wanneer een domeinterm of projectgrens duurzaam verduidelijkt is.

## Domeinregels

- Behandel [wettekst](https://wetten.overheid.nl/BWBR0003237/2026-01-01#Artikel6), online beleidsboek ([zelfstandig](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-zelfstandige-woonruimte), [onzelfstandig](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-onzelfstandige-woonruimte)) en implementatietoelichtingen als leidend voor puntberekeningen, in die volgorde van autoriteit (zie `CONTEXT.md`). Check zowel onze implementatietoelichting als het actuele online beleidsboek, omdat onze kopie kan achterlopen. Indien er tegenstrijdigheden in deze bronnen staan, vermeld dit.
- Maak expliciet wanneer VERA-data of het inputmodel onvoldoende is om een beleidsregel volledig te implementeren.
- Verander waarschuwing- of errorlogica niet stilzwijgend.
- Vermeld in gebruikersgerichte voorbeelden wanneer `warnings.simplefilter("default", UserWarning)` nodig is om incomplete input als warning in plaats van error te behandelen.

## Git En Veiligheid

- Revert geen bestaande wijzigingen die je niet zelf hebt gemaakt.
- Commit of push alleen wanneer de gebruiker daar expliciet om vraagt; volg dan [`.cursor/skills/managing-commits/SKILL.md`](.cursor/skills/managing-commits/SKILL.md).
- Voeg geen lokale, niet-gecommitte of organisatie-interne datastromen toe aan de publieke projectcontext.
- Commit geen secrets, credentials of lokale configuratiebestanden.
