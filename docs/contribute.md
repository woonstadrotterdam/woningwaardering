# Contribute

## Setup

Om de woningwaardering-package en de daarbij behorende developer dependencies te installeren, run onderstaand command:

```
git clone https://github.com/woonstadrotterdam/woningwaardering.git
cd woningwaardering
pip install -e ".[dev]"
```

## Naamgeving van classes

Voor de naamgeving van de classes in de woningwaardering module volgen we de VERA referentiedata. Deze referentiedata is gedefinieerd in de referentiedata enums, te vinden onder [woningwaardering/vera/referentiedata](woningwaardering/vera/referentiedata).

### Genereren opzet woningwaarderingstelsels en -groepen

Om alle onderstaande naamgevingen correct en consequent door te voeren, is er een task beschikbaar die de opzet van een woningwaarderingstelsel en -groep volgens deze regels voor je kan aanmaken.

Zorg er voor dat [Task](https://taskfile.dev/installation/) en de dev dependencies zijn geïnstalleerd:

```
pip install -e ".[dev]"
```

Vervolgens voer je onderstaand command uit:

```
task genereer-opzet-woningwaarderinggroep
```

Dit script stelt je een aantal vragen, waarna de code voor het stelsel en de stelselgroep aangemaakt worden.

### Stelsels

De namen voor de stelsels zijn te vinden in de `Woningwaarderingstelsel` Enum. Bijvoorbeeld: het stelsel voor zelfstandige woonruimten wordt aangeduid als `Woningwaarderingstelsel.zelfstandige_woonruimten`. De implementatie van dit `Stelsel` bevindt zich in [woningwaardering/stelsels/zelfstandige_woonruimten/zelfstandige_woonruimten.py](woningwaardering/stelsels/zelfstandige_woonruimten/zelfstandige_woonruimten.py).
De geldigheid van een stelsel wordt bepaald door de begin- en einddatum, die in de constructor van de corresponderende klasse worden vastgelegd.

### Stelselgroepen

De namen voor de stelselgroepen zijn te vinden in de `Woningwaarderingstelselgroep` Enum. Bijvoorbeeld: de stelselgroep voor oppervlakte van vertrekken wordt aangeduid als `Woningwaarderingstelselgroep.oppervlakte_van_vertrekken`. De implementatie van deze `Stelselgroep` bevindt zich in [woningwaardering/stelsels/zelfstandige_woonruimten/oppervlakte_van_vertrekken/oppervlakte_van_vertrekken.py](woningwaardering/stelsels/zelfstandige_woonruimten/oppervlakte_van_vertrekken/oppervlakte_van_vertrekken.py).
De geldigheid van een stelselgroep wordt bepaald door de begin- en einddatum, die in de constructor van de corresponderende klasse worden vastgelegd.

## Releasemanagement

### Versienummering

Voor versienummering maken we gebruik van [SemVer](https://semver.org/lang/nl/):

Bij SemVer wordt een versienummer in de vorm MAJOR.MINOR.PATCH gebruikt, waarbij elk element als volgt wordt verhoogd:

- `MAJOR` wordt verhoogd bij incompatibele API-wijzigingen,
- `MINOR` wordt verhoogd bij het toevoegen van functionaliteit die compatibel is met de vorige versie, en
- `PATCH` wordt verhoogd bij compatibele bugfixes.

Er zijn aanvullende labels beschikbaar voor pre-release en build-metadata om toe te voegen aan het `MAJOR.MINOR.PATCH`-formaat.

Bijvoorbeeld: stel dat de huidige versie `0.1.3-alpha` is.

- De suffix `-alpha` wordt gebruikt zolang de software nog niet volledig is, bijvoorbeeld zolang nog niet alle beoogde stelselgroepen geïmplementeerd zijn
- Wanneer een nieuwe release alleen compatibele bugfixes of updates van dependencies bevat, wordt de nieuwe versie `0.1.4-alpha`
- Wanneer een nieuwe release ook compatibele nieuwe functionaliteit toevoegt, bijvoorbeeld de implementatie van een nieuwe stelselgroep, dan wordt de nieuwe versie `0.2.0-alpha`.
- Wanneer alle beoogde stelselgroepen geïmplementeerd zijn, wordt de nieuwe versie `1.0.0-beta`. De publieke api mag vanaf dan enkel nog backwards-compatible wijzigen.
- Wanneer de software volledig is en in productie genomen wordt, wordt de nieuwe versie `1.0.0`
- Wanneer er een incompatible wijziging is in de VERA modellen, wordt de nieuwe versie `2.0.0`, eventueel met het `-alpha` of `-beta` label, afhankelijk van de implementatiestatus.

### Releaseproces

Om een nieuwe release te starten, moet er een Git tag aangemaak worden volgens het format `v<versienummer>`. De prefix `v` geeft aan dat de tag een versiepunt markeert.

Bijvoorbeeld:

```cli
$ git tag v0.2.3-alpha
$ git push --tags
```

Hiermee start het releaseproces, gedefinieerd in een GitHub workflow: [.github/workflows/publish-to-pypi.ymls](.github/workflows/publish-to-pypi.yml)

In dit proces wordt een package aangemaakt met een [Python versienummer](https://packaging.python.org/en/latest/discussions/versioning/), afgeleid van het SemVer nummer in de tag. Bijvoorbeeld: `0.2.3-alpha` wordt `0.2.3a0`

De package wordt eerst gepubliceerd op [TestPyPi](https://test.pypi.org/project/woningwaardering/). Na goedkeuring wordt de package naar [PyPi](https://pypi.org/project/woningwaardering/) gepubliceerd. Daarna wordt er een release aangemaakt in GitHub, met een changelog met de titel en link naar alle pull requests die deel uitmaken van deze release.

## Testing

Voor het testen van code wordt het [pytest framework](https://docs.pytest.org/en/8.0.x/index.html) gebruikt. Meer informatie is te vinden over het framework.
Passende tests worden altijd met de nieuw geschreven code opgeleverd.
Er zijn verschillende "test-scopes" te bedenken, zoals het testen van details en specifieke functies.
Daarnaast is het testen van een hele keten of stelselgroep-object ook vereist.
Bij het opleveren van nieuwe code moet aan beide test-scopes gedacht worden.

### Test coverage rapport

Na het uitvoeren van `pytest` wordt er een code coverage report getoond. Hierin is per file te zien welk percentage van de code in de files getest is.
Daarnaast wordt de code coverage ook naar een file `lcov.info` geschreven. Die kan gebruikt worden in VSCode om de coverage weer te geven met een plugin zoals "Coverage Gutters".

### Conventies voor tests

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

### Test modellen

Om de woningwaardering-package zo nauwkeurig mogelijk te testen, zijn er eenheidmodellen (in .json format) toegevoegd in `tests/data/...`. De modellen volgen de VERA standaard en dienen als een testinput voor de geschreven tests. De resulterende outputs zijn met de hand nagerekend om de kwaliteit van de tests te waarborgen.

Om heel specifieke regelgeving uit het beleidsboek te testen, kunnen er handmatig test modellen gemaakt worden. Deze test modellen worden opgeslagen in de test folder van een stelselgroep waarvoor de specifieke regelgeving die getest wordt. Zie bijvoorbeeld `tests/data/zelfstandige_woonruimten/stelselgroepen/oppervlakte_van_vertrekken/input/gedeelde_berging.json`: hier is een gedeelde berging gedefinieerd om een specifieke set van regels in oppervlakte_van_vertrekken te testen.

## Logger Guidelines

In de woningwaardering package wordt de logger van `loguru` gebruikt voor logging.
Voor het developen in de woningwaardering package worden de logging levels `DEBUG`, `INFO`, `WARNING` en `ERROR` gebruikt.
De verschillende levels worden gebruikt voor de verschillende types van logging, zoals beschreven in de [python 3.11 documentatie](https://docs.python.org/3.11/library/logging.html#logging-levels).
Hieronder is de tabel van de python documentatie gekopieerd waarin de verschillende logging levels staan beschreven.
De tabel is aangevuld met de kolom "Gebruik Woningwaardering Package", waarin wordt aangegeven met voorbeelden welke soort logging gedaan wordt op de verschillende logging levels.

| Level    | Numerieke waarde | Wat het betekent / Wanneer te gebruiken                                                                                                                                                                                                                                                   | Gebruik Woningwaardering Package                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NOTSET   | 0                | Wanneer ingesteld op een logger, geeft dit aan dat bovenliggende loggers geraadpleegd moeten worden om het effectieve niveau te bepalen. Als dit nog steeds NOTSET oplevert, worden alle gebeurtenissen gelogd. Wanneer ingesteld op een handler, worden alle gebeurtenissen afgehandeld. | Wordt niet gebruikt in de woningwaardering package.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| DEBUG    | 10               | Gedetailleerde informatie, meestal alleen van belang voor een ontwikkelaar die een probleem probeert te diagnosticeren.                                                                                                                                                                   | Wordt alleen gebruikt om details weer the geven aan een developer. bijvoorbeeld: wat een functie terug geeft of welke type een variabele heeft.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| INFO     | 20               | Bevestiging dat alles werkt zoals verwacht.                                                                                                                                                                                                                                               | Bevat beschrijvingen van de werking van de code. Bijvoorbeeld: Het berekende resultaat voor een stelselgroep of welke code op basis van de input data wordt gerund.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| WARNING  | 30               | Een indicatie dat er iets onverwachts is gebeurd, of dat er in de nabije toekomst een probleem kan optreden (bijv. 'schijfruimte bijna vol'). De software werkt nog steeds zoals verwacht.                                                                                                | Een warning wordt gelogd wanneer er bijvoorbeeld iets mist in de input data of een functie deprecated is. Dit kan er toe leiden dat bepaalde code niet uitgevoerd kan worden. Voor warnings aan de package gebruiker, wordt altijd `warnings.warn()` gebruikt. Zie het kopje [warnings](#warnings) voor meer informatie over het geven van warnings voor gebruikers en hoe hier mee omgegaan wordt.                                                                                                                                                                                                                                                                         |
| ERROR    | 40               | Vanwege een ernstiger probleem heeft de software een bepaalde functie niet kunnen uitvoeren.                                                                                                                                                                                              | Een error wordt in de woningwaardering package gelogd wanneer het gedrag verwacht is en de error een extra toelichting nodig heeft. Wanneer een error kritiek is voor het functioneren van de package wordt deze error geraisd. Ook kan het voorkomen dat de verwachte error toegestaan is. Dit kan bijvoorbeeld in een `try`/`except` patroon. Er kan dan gekozen worden om de error te loggen maar niet te raisen. Hierdoor kan het programma wel doorgaan en is het wel duidelijk dat er een `exception` heeft plaatsgevonden. Zoals een error geraisd kan worden en het programma kan laten stoppen, zo kunnen warnings ook geraisd worden om het progromma te stoppen. |
| CRITICAL | 50               | Een ernstige fout, die aangeeft dat het programma zelf mogelijk niet meer kan blijven draaien.                                                                                                                                                                                            | Wordt niet gebruikt in de woningwaardering package.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## Datamodellen

De datamodellen in de `woningwaardering` package zijn gebaseerd op de OpenAPI-specificatie van het [VERA BVG domein](https://aedes-datastandaarden.github.io/vera-openapi/Ketenprocessen/BVG.html).

Wanneer je deze modellen wilt bijwerken, zorg er dan voor dat [Task](https://taskfile.dev/installation/) en de dev dependencies zijn geïnstalleerd:

```
pip install -e ".[dev]"
```

Update het versienummer van de VERA OpenAPI-specificatie in `pyproject.toml`

Vervolgens kan je met dit commando de modellen in deze repository bijwerken:

```
task genereer-vera-bvg-modellen
```

De classes voor deze modellen worden gegeneerd in `woningwaardering/vera/bvg/generated.py`

### Datamodellen uitbreiden

Wanneer de VERA modellen niet toereikend zijn om de woningwaardering te berekenen, kan het VERA model uitgebreid worden.

Maak hiervoor altijd eerst een issue aan in de [VERA OpenApi repository](https://github.com/Aedes-datastandaarden/vera-openapi).

Maak vervolgens in de map [woningwaardering/vera/bvg/model_uitbreidingen](woningwaardering/vera/bvg/model_uitbreidingen) een class aan met de missende attributen. De naamgeving voor deze classes is: `_{classNaam}`.

Zet in de class bij het toegevoegde attribuut een comment met een link naar het issue in de VERA OpenApi repository zodat duidelijk is waar de toevoeging voor dient, en we kunnen volgen of de aanpassing is doorgevoerd in de VERA modellen.

Daarnaast neem je in de class een docstring op met uitleg over het gebruik en doel van de uitbreiding.

Bijvoorbeeld: voor het uitbreiden van de class `EenhedenRuimte` maak je een class `_EenhedenRuimte` aan:

```python
from typing import Optional

from pydantic import BaseModel, Field


class _EenhedenRuimte(BaseModel):
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/44
    gedeeld_met_aantal_eenheden: Optional[int] = Field(
        default=None, alias="gedeeldMetAantalEenheden"
    )
    """
    Het aantal eenheden waarmee deze ruimte wordt gedeeld. Deze waarde wordt gebruikt bij het berekenen van de waardering van een gedeelde ruimte met ruimtedetailsoort berging.
    """
```

De task `genereer-vera-bvg-modellen` zal de body van deze classes samenvoegen met de gelijknamige VERA class en zo de toegevoegde attributen beschikbaar maken.

## Referentiedata

We maken gebruik van de [VERA Referentiedata](https://github.com/Aedes-datastandaarden/vera-referentiedata).

Wanneer je de referentiedata wilt bijwerken, zorg er dan voor dat [Task](https://taskfile.dev/installation/) is geïnstalleerd

Update het versienummer van de referentiedata in `pyproject.toml`
Vervolgens kan je met dit commando de referentiedata in deze repository bijwerken:

```
task genereer-vera-referentiedata
```

De referentiedata wordt gegenereerd in `woningwaardering/vera/referentiedata`

## Woonplaatsen en COROP-gebieden

Om te bepalen in welk COROP-gebied een woonplaats ligt, maken we gebruik van de CBS datasets "Woonplaatsen in Nederland" en "Gebieden in Nederland".
Het CBS publiceert eens per jaar nieuwe datasets, daarom hebben we een script gemaakt dat een extract van deze data als resource in de package opslaat in `woningwaardering/data/corop/corop.generated.csv`.

Wanneer je deze data bij wilt werken, zorg er dan voor dat [Task](https://taskfile.dev/installation/) is geïnstalleerd.

Vervolgens kan je met dit commando de woonplaatsen en COROP-gebieden in deze repository bijwerken:

```
task genereer-corop-data
```

## Gemiddelde WOZ-waarden per vierkante meter per COROP-gebied

Bij het beleidsboek wordt een bijlage gepubliceerd met de gemiddelde WOZ-waarden per vierkante meter per COROP-gebied. Na publicatie van een nieuwe bijlage dient het bestand `woningwaardering/stelsels/onzelfstandige_woonruimten/punten_voor_de_woz_waarde/lookup_tabellen/corop_gebied_gemiddelde_woz_waarde_per_m2.csv` bijgewerkt te worden, door een kolom toe te voegen met als kolomnaam het jaar van de waardepeildatum waarvoor de nieuwe gemiddelde waarden gelden.
