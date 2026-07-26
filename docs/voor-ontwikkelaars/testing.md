# Testing

Voor het testen van code wordt het [pytest framework](https://docs.pytest.org/en/8.0.x/index.html) gebruikt.

## Tests uitvoeren

Zorg dat de dev dependencies geïnstalleerd zijn (zie [Installatie](index.md)), en run:

```bash
uv run python -m pytest
```

Met geactiveerde `.venv` mag je ook `python -m pytest` gebruiken. Coverage wordt automatisch meegenomen via de pytest-configuratie in `pyproject.toml`.

Na wijzigingen in code of tests draai je ook de pre-commit hooks (dezelfde set als CI); zie [Tests en checks](index.md#tests-en-checks).

Passende tests worden altijd met de nieuw geschreven code opgeleverd.
Er zijn verschillende "test-scopes" te bedenken, zoals het testen van details en specifieke functies.
Daarnaast is het testen van een hele keten of stelselgroep-object ook vereist.
Bij het opleveren van nieuwe code moet aan beide test-scopes gedacht worden.

## Expected test outputs genereren

Bij code-wijzigingen die leiden tot wijzigingen in de output moeten de expected outputs onder `tests/stelsels/**/output.json`, `tests/docs/output_json_*.json` en de gerelateerde output-txt bestanden opnieuw gegenereerd worden. Gebruik hiervoor:

```bash
task genereer-test-output
```

Dit draait `scripts/genereer_test_output.py` en overschrijft per case-map onder `tests/stelsels/` de bestanden `output.json` en `output.txt` (plus `output.log` voor review), en daarnaast `tests/docs/output_json_*.json`.

`output.txt` bevat de woningwaardering in leesbaar rapportformaat en is bedoeld om output-wijzigingen in PRs te reviewen; pytest vergelijkt alleen de JSONs.

> ⚠️ Let op: als je de expected output-jsons opnieuw genereert na code-changes zullen alle tests slagen. Het is dus belangrijk om te analyseren hoe expected outputs veranderd zijn na de code-changes die je hebt doorgevoerd. Zo kun je achterhalen of de code-changes wel het gewenste effect hebben gehad en niet ook nog ongewenste neveneffecten.

Let ook op: `docs/aan-de-slag/index.md` bevat inline voorbeeld-output (JSON en rapport). Als output, namen of criterium-id’s wijzigen, moet je die voorbeelden handmatig nalopen/bijwerken zodat de docs niet stilzwijgend verouderen.

## Test coverage rapport

Na het uitvoeren van `pytest` wordt er een code coverage report getoond. Hierin is per file te zien welk percentage van de code in de files getest is.
Daarnaast wordt de code coverage ook naar een file `lcov.info` geschreven. Die kan gebruikt worden in VSCode om de coverage weer te geven met een plugin zoals "Coverage Gutters".

## Conventies voor tests

Tests worden toegevoegd aan de `tests`-folder in de root van de repository.
Voor de structuur in de `tests`-folder wordt dezelfde structuur aangehouden als die in de `woningwaardering`-folder.
De naam van het bestand waarin de tests staan geschreven is `test_<file_name>.py`.
Elke testfunctie begint met `test_`, gevolgd door de naam van de functie of class die getest wordt, bijvoorbeeld `def test_<functie_naam>()` of `def test_<ClassNaam>()`.
Hierin wordt de naam van de functie of class exact gevolgd.
Voor pytest is `test_` een indicator om de functie te herkennen als een testfunctie.

Stel dat de functionaliteiten van `woningwaardering/stelsels/zelfstandige_woonruimten/oppervlakte_van_vertrekken/oppervlakte_van_vertrekken.py` getest moeten worden, dan is het pad naar het bijbehorende testbestand `tests/stelsels/zelfstandige_woonruimten/oppervlakte_van_vertrekken/test_oppervlakte_van_vertrekken.py`.
In `test_oppervlakte_van_vertrekken.py` worden testfuncties geschreven met bijbehorende naamconventies.
Hieronder is de functienaamconventie en python code weergegeven voor het testen van een losse functie (`def losse_functie`):

```python
def test_losse_functie() -> None:
    assert losse_functie() == True
```

Als er een class getest wordt, bijvoorbeeld `OppervlakteVanVertrekken`, dan is de testfunctie opzet als volgt:

```python
def test_OppervlakteVanVertrekken() -> None:
    opp_v_v = OppervlakteVanVertrekken()
    assert opp_v_v.functie_een() == 1
    assert opp_v_v.functie_twee() == 2
```

## Test modellen

Om de woningwaardering-package zo nauwkeurig mogelijk te testen, zijn er VERA-eenheidmodellen toegevoegd onder `tests/stelsels/`. Elke testcase is een map met vaste bestandsnamen:

```
<case_naam>/
  input.json
  output.json
  output.log      # gegenereerd (review)
  output.txt      # gegenereerd (leesbare tabel)
  input_context.md # verplicht: doel en beleidsbron
```

**Stelsel-ketentests** (volledige woningwaardering per eenheid):

`tests/stelsels/{stelsel}/eenheden/{vera_id}/`

**Stelselgroep-specifieke tests:**

`tests/stelsels/{stelsel}/{stelselgroep}/{case_naam}/`

De testbestanden staan naast de cases in dezelfde stelselgroep-map, bijvoorbeeld `tests/stelsels/zelfstandige_woonruimten/sanitair/test_Sanitair.py`.

### input_context.md

Elke case-map met `input.json` heeft een `input_context.md` met minimaal `## Doel` en `## Beleidsbron`. Link naar de implementatietoelichting met een pad relatief aan de case-map (zodat klikken in de editor werkt), bijvoorbeeld:

```markdown
## Beleidsbron
- Implementatietoelichting: [§2.6 Rubriek 6: Sanitair](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#26-rubriek-6-sanitair)
```

Voorbeeld stelselgroep-case: `tests/stelsels/zelfstandige_woonruimten/oppervlakte_van_vertrekken/gedeelde_berging/` — een gedeelde berging om specifieke regels in oppervlakte_van_vertrekken te testen.