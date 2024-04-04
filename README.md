# Woningwaardering

⌛️ **Work in Progress**

Het Microservices team van Woonstad Rotterdam is in Q1 2024 begonnen met het ontwikkelen met een open-source Python-package waarmee het mogelijk zal zijn om het puntensysteeem van het [woningwaarderingsstelsel](https://aedes.nl/huurbeleid-en-betaalbaarheid/woningwaarderingsstelsel-wws) toe te passen. We gaan hierbij zo veel mogelijk uit van de [VERA-standaard](https://www.coraveraonline.nl/index.php/VERA-standaard) van de corporatiesector. Het doel is om tot een completere woningwaarderingsstelsel-berekening te komen dan die nu beschikbaar zijn via tools zoals bijvoorbeeld die van de [huurcommissie](https://www.huurcommissie.nl/huurders/sociale-huurwoning/maximale-huurprijs-berekenen).

Voor vragen kunt u contact opnemen met de Product Owner van Team Microservices [Wouter Kolbeek](mailto:wouter.kolbeek@woonstadrotterdam.nl) of één van de maintainers van deze repo.

## Implementatie Beleidsboek Huurcommissie

Voor het berekenen van een woningwaardering worden de [beleidsboeken van de Nederlandse Huurcommissie](https://www.huurcommissie.nl/huurcommissie-helpt/beleidsboeken) voor de waarderingstelsels voor zelfstandige en onzelfstandige woningen gevolgd.
De beleidsboeken van de Huurcommissie Nederland volgen Nederlandse wet- en regelgeving zoals beschreven in [Artikel 14 van het "Besluit huurprijzen woonruimte"](https://wetten.overheid.nl/BWBR0003237/2024-01-01#Artikel14).

Om berekeningen te maken met betrekking tot een woningwaardering wordt het gepubliceerde beleid vertaald naar Python-code.
Een woningwaardering wordt gemaakt op basis van woningelementen.
De stelselgroepen waarop gescoord wordt, zijn vastgelegd in het [woningwaarderingstelselgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP) op www.coraveraonline.nl.
Deze worden aangehouden in de opzet van de `woningwaardering`-package.
Voor elke stelselgroep wordt een apart Python-object gemaakt met een naam die overeenkomt met [woningwaarderingstelselgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP).
Elk stelselgroep-object zal mee veranderen met nieuw gepubliceerde wet- en regelgeving, die is opgenomen in de [beleidsboeken van de Nederlandse Huurcommissie](https://www.huurcommissie.nl/huurcommissie-helpt/beleidsboeken).

## Opzet woningwaardering

### Repository-structuur

De repository-structuur is ingedeeld volgens de [referentiedata van stelselgroepen van de VERA-standaard](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP); eerst de stelsels (bijvoorbeeld _zelfstandig_, _onzelfstandig_) en vervolgens de stelselgroepen (bijvoorbeeld _Energieprestatie_, _Wasgelegenheid_).
In de folders van de stelselgroepen bevindt zich de code voor het berekenen van de punten per stelselgroep.

### Design

Het design van de `woningwaardering`-package is zo gekozen dat stelselgroep-objecten en bijbehorende regels modulair zijn.
Dit houdt in dat regels in een stelselgroep-object vervangbaar en inwisselbaar zijn, met als resultaat dat op basis van de gegeven input de woningwaardering berekend wordt met de juiste set aan stelselgroep-objecten en bijbehorende regels.
Ook wanneer een wet verandert met ingang van een bepaalde datum zorgt de modulariteit ervoor dat de juiste regels worden gebruikt voor de stelselgroep.
De `woningwaardering`-package selecteert op basis van een peildatum de juiste set aan regels die volgens de Nederlandse wet gelden voor de desbetreffende peildatum.
Hieronder is het modulaire principe op basis van een peildatum schematisch weergegeven voor het stelselgroep-object `OppervlakteVanVertrekken`.
Voor de duidelijkheid: Onderstaand voorbeeld is niet gebaseerd op een echte verandering in het beleidshandboek.
Het voorbeeld laat zien hoe de berekening van de `OppervlakteVanVertrekken` afhangt van de peildatum.
Op basis van de peildatum wordt voor de bovenste beleidsregel gekozen omdat die berekening geldig is voor de opgegeven peildatum.

![Voorbeeld modulaire oppervlakte van vertrekken](./docs/afbeeldingen/oppervlakte_van_vertrekken.png)

### Referentiedata

Onder referentiedata worden constanten, variabelen en tabellen verstaan die nodig zijn in het berekenen van een score.
In de `woningwaardering` package wordt CSV gebruikt als bestandstype voor het opslaan van referentiedata.
De keuze is op CSV gevallen omdat referentiedata soms bestaat uit meerdere datarijen waardoor dit vaak minder leesbaar wordt wanneer dit bijvoorbeeld in json of yaml wordt opgeslagen.
Voor VSCode-gebruikers is de extensie Excel Viewer van GrapeCity aan te raden.
Met behulp van deze extensie kunnen CSV-bestanden als tabel weergegeven worden in VSCode.
Hieronder is een voorbeeldtabel te zien zoals deze met Excel Viewer in VSCode wordt weergegeven.

![Excel Viewer](./docs/afbeeldingen/excel_viewer.png)

Door gebruik van CSV-bestanden, wordt het selecteren van de juiste rij of waarde doormiddel van een peildatum vergemakkelijkt.
In de `woningwaardering`-package wordt een peildatum gebruikt om de juiste waarde van bijvoorbeeld een variabele uit een tabel te selecteren.
Dit kan worden gedaan opbasis van de `Begindatum` en de `Einddatum` kolommen in een CSV-bestand.
Wanneer er geen `Begindatum` of `Einddatum` is gespecificeerd, dan is deze niet bekend.
Dit betekent niet dat er geen werkabre en geldige rij geselecteerd kan worden.
Wel zou het kunnen dat er door het ontbreken van een `Begindatum` of `Einddatum` meerdere rijen geldig zijn voor een peildatum.
In dit geval zal de `woningwaardering`-package een error geven die duidelijk maakt dat er geen geldige rij gekozen kan worden op basis van de peildatum voor het desbtreffende CSV-bestand.

## Contributing

### Setup

### Naamgeving van classes

Voor de naamgeving van de classes in de woningwaardering module volgen we de VERA referentiedata. Deze referentiedata is gedefinieerd in de referentiedata enums, te vinden onder [woningwaardering/vera/referentiedata](woningwaardering/vera/referentiedata).

#### Stelsels

De namen voor de stelsels zijn te vinden in de `Woningwaarderingstelsel` Enum. Bijvoorbeeld: het stelsel voor zelfstandige woonruimten wordt aangeduid als `Woningwaarderingstelsel.zelfstandige_woonruimten`. De implementatie van dit `Stelsel` bevindt zich in [woningwaardering/stelsels/zelfstandige_woonruimten/zelfstandige_woonruimten.py](woningwaardering/stelsels/zelfstandige_woonruimten/zelfstandige_woonruimten.py).
De begin- en einddatum van de geldigheid van een stelsel wordt vastgelegd in de configuratie `.yml` van het betreffende stelsel. Bijvoorbeeld: voor zelfstandige woonruimten is dit [woningwaardering/stelsels/config/zelfstandige_woonruimten.yml](woningwaardering/stelsels/config/zelfstandige_woonruimten.yml)

#### Stelselgroepen

De namen voor de stelselgroepen zijn te vinden in de `Woningwaarderingstelselgroep` Enum. Bijvoorbeeld: de stelselgroep voor oppervlakte van vertrekken wordt aangeduid als `Woningwaarderingstelselgroep.oppervlakte_van_vertrekken`. De implementatie van deze `Stelselgroep` bevindt zich in [woningwaardering/stelsels/zelfstandige_woonruimten/oppervlakte_van_vertrekken/oppervlakte_van_vertrekken.py](woningwaardering/stelsels/zelfstandige_woonruimten/oppervlakte_van_vertrekken/oppervlakte_van_vertrekken.py).
De begin- en einddatum van de geldigheid van een stelselgroep wordt vastgelegd in de configuratie `.yml` van het betreffende stelsel.

#### Stelselgroepversies

De daadwerkelijke implementatie van een stelselgroep is een `Stelselgroepversie`. Voor stelselgroepversies wordt de naam van de stelselgroep gevolgd door het jaar waarin de versie van de stelselgroep in gebruik gaat. Bijvoorbeeld: de implementatie van de `Stelselgroepversie` voor oppervlakte van vertrekken die in gaat in het jaar 2024 bevindt zich in [woningwaardering/stelsels/zelfstandige_woonruimten/oppervlakte_van_vertrekken/oppervlakte_van_vertrekken_2024.py](woningwaardering/stelsels/zelfstandige_woonruimten/oppervlakte_van_vertrekken/oppervlakte_van_vertrekken_2024.py).
Omdat het lastig is met terugwerkende kracht te achterhalen in welk jaar een versie van een stelselgroep ingegaan is, gebruiken we voor de eerste versie van een stelselgroep het jaar van de implementatie van de stelselgroep in deze module. Wanneer de berekening van een stelselgroep in een bepaald jaar niet wijzigt, wordt er geen nieuwe stelselgroepversie aangemaakt. De begin- en einddatum van de geldigheid van een stelselgroepversie wordt vastgelegd in de configuratie `.yml` van het betreffende stelsel.

### Testing

Voor het testen van code wordt het [pytest framework](https://docs.pytest.org/en/8.0.x/index.html) gebruikt. Meer informatie is te vinden over het framework.
Passende tests worden altijd met de nieuw geschreven code opgeleverd.
Er zijn verschillende "test-scopes" te bedenken, zoals het testen van details en specifieke functies.
Daarnaast is het testen van een hele keten of stelselgroep-object ook vereist.
Bij het opleveren van nieuwe code moet aan beide test-scopes gedacht worden.

#### Conventies voor Tests

Tests worden toegevoegd aan de `tests`-folder in de root van de repository.
Voor de structuur in de `tests`-folder wordt dezelfde structuur aangehouden als die in de `woningwaardering`-folder.
De naam van het bestand waarin de tests staan geschreven is `test_<file_name>.py`.
Wanneer er een class getest wordt, wordt er een `class Test<class_naam>` aangemaakt met daarin testfuncties.
Elke testfunctie in deze class moet starten met `test`, gevolgd door de naam van de functie die getest wordt uit de desbetreffende class, bijvoorbeeld `def test_<functie_naam>()`.
`test` is voor pytest een indicator om de functie te herkennen als een testfunctie.

Stel dat de functionaliteiten van `woningwaardering/stelsels/zelfstandige_woonruimten/oppervlakte_van_vertrekken/oppervlakte_van_vertrekken.py` getest moeten worden, dan is het pad naar het bijbehorende testbestand `tests/stelsels/zelfstandige_woonruimten/oppervlakte_van_vertrekken/test_oppervlakte_van_vertrekken.py`.
In `test_oppervlakte_van_vertrekken.py` worden testfuncties en/of testobjecten geschreven met bijbehorende naamconventies.
Hieronder is de functienaamconventie en python code weergegeven voor het testen van een losse functie:

```python
def test_losse_functie() -> None:
    assert losse_functie() == True
```

Als er een class getest wordt, bijvoorbeeld `OppervlakteVanVertrekken`, dan is de test-class opzet als volgt:

```python
class TestOppervlakteVanVertrekken:

    @classmethod
    def setup_class(cls):
        # initieer de class
        cls.test_object = OppervlakteVanVertrekken()

    def test_functie_een(self):
        assert self.test_object.functie_een() == 1

    def test_functie_twee(self):
        assert self.test_object.functie_twee() == 2
```

### Datamodellen

De datamodellen in de `woningwaardering` package zijn gebaseerd op de OpenAPI-specificatie van het [VERA BVG domein](https://aedes-datastandaarden.github.io/vera-openapi/Ketenprocessen/BVG.html).

Wanneer je deze modellen wilt bijwerken, zorg er dan voor dat [Task](https://taskfile.dev/installation/) is geïnstalleerd, en dat de dev dependencies zijn geinstalleerd:

```
pip install -e .[dev]
```

Vervolgens kan je met dit commando de modellen in deze repository bijwerken:

```
task genereer-vera-bvg-modellen
```

De classes voor deze modellen worden gegeneerd in `woningwaardering/vera/bvg/generated.py`

#### Uitbreidingen op datamodellen

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

### Referentiedata

Naast de referentiedata specifiek voor deze package, maken we ook gebruik van de [VERA Referentiedata](https://github.com/Aedes-datastandaarden/vera-referentiedata).

Wanneer je deze referentiedata wilt bijwerken, zorg er dan voor dat [Task](https://taskfile.dev/installation/) is geïnstalleerd

Vervolgens kan je met dit commando de referentiedata in deze repository bijwerken:

```
task genereer-vera-referentiedata
```

De referentiedata wordt gegenereerd in `woningwaardering/vera/referentiedata`
