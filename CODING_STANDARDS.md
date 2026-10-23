# Codeerstandaarden

Deze standaarden worden bij review afgedwongen (`/code-review`). Mechanische regels staan niet hier maar in de checks van `.pre-commit-config.yaml` en `pyproject.toml`; dit bestand bevat alleen afwegingen die geen tool kan maken. Gebruik voor domeintermen [`GLOSSARY.md`](GLOSSARY.md).

## Structuur

- Volg de VERA-referentiedata voor naamgeving van stelsels en stelselgroepen; zie [naamgeving.md](docs/voor-ontwikkelaars/naamgeving.md).
- Plaats stelselgroep-logica in de map van het juiste stelsel onder `woningwaardering/stelsels/`.
- Plaats logica die door meerdere stelsels gedeeld wordt in `woningwaardering/stelsels/gedeelde_logica/`.
- Bouw de output van een stelselgroep op met de builders in `woningwaardering/stelsels/builders.py` (`met_onderliggend` / `met_subgroep` / `gedeeld_met`); zie [criteriumstrategie.md](docs/voor-ontwikkelaars/criteriumstrategie.md).
- Gebruik bestaande patronen voor stelsels, stelselgroepen, criterium-id's en lookup-tabellen voordat je nieuwe abstraheringen toevoegt.
- `woningwaardering/vera/bvg/generated.py` en `woningwaardering/vera/referentiedata/` zijn gegenereerd. Bewerk ze niet met de hand, want de generator overschrijft handmatige wijzigingen; draai in plaats daarvan `task genereer-vera-bvg-modellen` of `task genereer-vera-referentiedata`. De modeluitbreidingen in `woningwaardering/vera/bvg/model_uitbreidingen/` zijn handgeschreven en mag je wel bewerken.

## Waarschuwingen en logging

- Gebruik `warnings.warn(..., UserWarning)` voor gebruikersgerichte waarschuwingen over incomplete of onjuiste input, volgens de bestaande warning-semantiek.
- Gebruik `loguru` voor logging volgens [logging.md](docs/voor-ontwikkelaars/logging.md); ruff (TID251) verbiedt `import logging`.

## Imports

- Houd imports bovenaan het bestand. Een inline import mag alleen wanneer de import bovenaan niet kan, zoals bij een circulaire import of een optionele dependency; ruff (PLC0415) dwingt dit af. Zet de reden in een comment boven de import, met `# noqa: PLC0415` op de importregel.

## Comments

- Gebruik comments vooral om beleidsregels herleidbaar te maken: neem waar mogelijk de relevante tekst uit het beleidsboek, de implementatietoelichting of de [wettekst](https://wetten.overheid.nl/BWBR0003237/2026-01-01) letterlijk op bij de bijbehorende code, met vermelding van het regelnummer/artikel. Zet de link naar de pagina waar de tekst staat in de pull request (zie Domeinregels in [`AGENTS.md`](AGENTS.md)).
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

- Voeg passende tests toe bij nieuwe of gewijzigde code; zie [testing.md](docs/voor-ontwikkelaars/testing.md) voor welke soort test past.
- Spiegel de package-structuur waar praktisch: tests voor `woningwaardering/.../module.py` horen onder `tests/.../test_module.py`.
- Test geen gegenereerde VERA-code alleen om coverage te verhogen.
- Verwachte output (`tests/**/testreferenties/*.md`, `tests/docs/output_json_*.json`) wijzigt alleen via `task genereer-test-output` en alleen waar de taak dat voorziet; meld in de PR welke verwachte output is gewijzigd en waarom.
