# Woningwaardering

De `woningwaardering`-package is een opensource-pakket met functionaliteiten voor het berekenen van een woningwaardering op basis van het gepubliceerde woningwaarderingstelsel door de Nederlandse Huurcommissie.
Dit project is een initiatief van Woonstad Rotterdam.

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
 
De repository-structuur is ingedeeld volgens de [referentiedata van stelselgroepen van de VERA-standaard](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP); eerst de stelsels (bijvoorbeeld *zelfstandig*, *onzelfstandig*) en vervolgens de stelselgroepen (bijvoorbeeld *Energieprestatie*, *Wasgelegenheid*).
Referentiedata:WONINGWAARDERINGSTELSELGROEP - CORA VERA online, Woningcorporatie Referentiearchitectuur. 
In de folders van de stelselgroepen bevindt zich de code voor het berekenen van de punten per stelselgroep.

### Design
Het design van de `woningwaardering`-package is zo gekozen dat stelselgroep-objecten en bijbehorende regels modulair zijn.
Dit houdt in dat regels in een stelselgroep-object vervangbaar en inwisselbaar zijn, met als resultaat dat op basis van de gegeven input de woningwaardering berekend wordt met de juiste set aan stelselgroep-objecten en bijbehorende regels.
Ook wanneer een wet verandert met ingang op een bepaalde datum zorgt de modulariteit ervoor dat de juiste regels worden gebruikt voor de stelselgroep.
De `woningwaardering`-package selecteert op basis van een peildatum de juiste set aan regels die volgens de Nederlandse wet gelden voor de desbetreffende peildatum.
Hieronder is het modulaire principe op basis van een peildatum schematisch weergegeven voor het stelselgroep-object `OppervlakteVanVertrekken`.
Voor de duidelijkheid: Onderstaand voorbeeld is niet gebaseerd op een echte verandering in het beleidshandboek.
Het voorbeeld laat zien hoe de berekening van de `OppervlakteVanVertrekken` afhangt van de peildatum.
Op basis van de peildatum wordt voor de bovenste beleidsregel gekozen omdat die berekening geldig is voor de opgegeven peildatum.

![Voorbeeld modulaire oppervlakte van vertrekken](./docs/afbeeldingen/oppervlakte_van_vertrekken.png)

### Referentie Data
Onder referentiedata worden constanten, variabelen en tabellen verstaan die nodig zijn in het berekenen van een score.
In de `woningwaardering` package wordt CSV gebruikt als bestandstype voor het opslaan van referentiedata.
De keuze is op CSV gevallen omdat referentiedata soms bestaat uit meerdere datarijen waardoor dit vaak minder leesbaar wordt wanneer dit bijvoorbeeld in json of yaml wordt opgeslagen.
Voor VSCode-gebruikers is de extensie Excel Viewer van GrapeCity aan te raden.
Met behulp van deze extensie kunnen CSV-bestanden als tabel weergegeven worden in VSCode.
Hieronder is een voorbeeldtabel te zien zoals deze met Excel Viewer in VSCode wordt weergegeven.

![Excel Viewer](./docs/afbeeldingen/excel_viewer.png)

Daarnaast wordt in de `woningwaardering`-package een peildatum gebruikt om de juiste waarde van bijvoorbeeld een variabele of uit een tabel te selecteren.
Hierdoor heeft een variabele altijd een peildatum nodig en zal deze ook geregistreerd moeten worden.
Het gevolg hiervan is dat er altijd een peildatumkolom ontstaat in het CSV-bestand.
Door gebruik van CSV bestanden, wordt het selecteren van de juiste rij of waarde doormiddel van een peildatum vergemakkelijkt.


## Contributing

### Setup
Hoe je kunt bijdragen aan deze package \<to do\>

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

Stel dat de functionaliteiten van `woningwaardering/stelsels/zelfstandig/oppervlakte_van_vertrekken/oppervlakte_van_vertrekken.py` getest moeten worden, dan is het pad naar het bijbehorende testbestand `tests/stelsels/zelfstandig/oppervlakte_van_vertrekken/test_oppervlakte_van_vertrekken.py`.
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
