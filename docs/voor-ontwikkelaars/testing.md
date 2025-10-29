# Testing

Voor het testen van code wordt het [pytest framework](https://docs.pytest.org/en/8.0.x/index.html) gebruikt. Meer informatie is te vinden over het framework.
Passende tests worden altijd met de nieuw geschreven code opgeleverd.
Er zijn verschillende "test-scopes" te bedenken, zoals het testen van details en specifieke functies.
Daarnaast is het testen van een hele keten of stelselgroep-object ook vereist.
Bij het opleveren van nieuwe code moet aan beide test-scopes gedacht worden.

## Test coverage rapport

Na het uitvoeren van `pytest` wordt er een code coverage report getoond. Hierin is per file te zien welk percentage van de code in de files getest is.
Daarnaast wordt de code coverage ook naar een file `lcov.info` geschreven. Die kan gebruikt worden in VSCode om de coverage weer te geven met een plugin zoals "Coverage Gutters".

## Conventies voor tests

Tests worden toegevoegd aan de `tests`-folder in de root van de repository.
Voor de structuur in de `tests`-folder wordt dezelfde structuur aangehouden als die in de `woningwaardering`-folder.
De naam van het bestand waarin de tests staan geschreven is `test_<file_name>.py`.
Elke testfunctie begint met `test_`, gevolgd door de naam van de functie of class die getest wordt, bijvoorbeeld `def test_<functie_naam>()` of `def test_<ClassNaam>()`.
Hierin wordt de naam de van de functie of class exact gevolgd.
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
def test_OppervlakteVanVertrekken():
    opp_v_v = OppervlakteVanVertrekken()
    assert self.opp_v_v.functie_een() == 1
    assert self.opp_v_v.functie_twee() == 2
```

## Test modellen

Om de woningwaardering-package zo nauwkeurig mogelijk te testen, zijn er eenheidmodellen (in .json format) toegevoegd in `tests/data/...`. De modellen volgen de VERA standaard en dienen als een testinput voor de geschreven tests. De resulterende outputs zijn met de hand nagerekend om de kwaliteit van de tests te waarborgen.

Om heel specifieke regelgeving uit het beleidsboek te testen, kunnen er handmatig test modellen gemaakt worden. Deze test modellen worden opgeslagen in de test folder van een stelselgroep waarvoor de specifieke regelgeving die getest wordt. Zie bijvoorbeeld `tests/data/zelfstandige_woonruimten/stelselgroepen/oppervlakte_van_vertrekken/input/gedeelde_berging.json`: hier is een gedeelde berging gedefinieerd om een specifieke set van regels in oppervlakte_van_vertrekken te testen. 