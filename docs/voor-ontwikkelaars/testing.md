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

Bij code-wijzigingen die leiden tot wijzigingen in de output moeten de expected outputs onder `tests/data/**/output/*.json` (en voor unit-tests ook `*.txt`), en `tests/docs/output_json_*.json` opnieuw gegenereerd worden.

> ⚠️ Let op: als je de expected output-jsons opnieuw genereerd na code-changes zullen alle tests slagen. Het is dus belangrijk om te analyseren welke expected outputs hoe veranderen na de code-changes die je hebt doorgevoerd om te begrijpen of je code-changes wel het gewenste effect hebben gehad en niet ook nog ongewenste neveneffecten.

Gebruik het Task target (zie `taskfile.yml`):

```bash
task genereer-test-output
```

Dit draait `scripts/genereer_test_output.py` en overschrijft alle expected outputs onder `tests/data/**/output/` en `tests/docs/output_json_*.json`.

Voor unit-inputs onder `tests/data/<stelsel>/input/` (niet voor `stelselgroepen/`) schrijft het script naast JSON ook een `*.txt` met de woningwaardering in leesbaar tabelformaat. Die bestanden zijn bedoeld om output-wijzigingen in PRs te reviewen; pytest vergelijkt alleen de JSONs.

Let ook op: `docs/aan-de-slag/index.md` bevat inline voorbeeld-output (JSON en tabel). Als output, namen of criterium-id’s wijzigen, moet je die voorbeelden handmatig nalopen/bijwerken zodat de docs niet stilzwijgend verouderen.

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

Om de woningwaardering-package zo nauwkeurig mogelijk te testen, zijn er eenheidmodellen (in .json format) toegevoegd in `tests/data/...`. De modellen volgen de VERA standaard en dienen als een testinput voor de geschreven tests. De resulterende outputs zijn met de hand nagerekend om de kwaliteit van de tests te waarborgen.

Om heel specifieke regelgeving uit het beleidsboek te testen, kunnen er handmatig test modellen gemaakt worden. Deze test modellen worden opgeslagen in de test folder van een stelselgroep waarvoor de specifieke regelgeving die getest wordt. Zie bijvoorbeeld `tests/data/zelfstandige_woonruimten/stelselgroepen/oppervlakte_van_vertrekken/input/gedeelde_berging.json`: hier is een gedeelde berging gedefinieerd om een specifieke set van regels in oppervlakte_van_vertrekken te testen. 