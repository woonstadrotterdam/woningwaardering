# Woningwaardering

⌛️ **Work in Progress**

Het Microservices team van Woonstad Rotterdam is in Q1 2024 begonnen met het ontwikkelen met een open-source Python-package waarmee het mogelijk zal zijn om het puntensysteeem van het [woningwaarderingsstelsel](https://aedes.nl/huurbeleid-en-betaalbaarheid/woningwaarderingsstelsel-wws) toe te passen. We gaan hierbij zo veel mogelijk uit van de [VERA-standaard](https://www.coraveraonline.nl/index.php/VERA-standaard) van de corporatiesector. Het doel is om tot een completere woningwaarderingsstelsel-berekening te komen dan die nu beschikbaar zijn via tools zoals bijvoorbeeld die van de [huurcommissie](https://www.huurcommissie.nl/huurders/sociale-huurwoning/maximale-huurprijs-berekenen).

Voor vragen kunt u contact opnemen met de Product Owner van Team Microservices [Wouter Kolbeek](mailto:wouter.kolbeek@woonstadrotterdam.nl) of één van de maintainers van deze repo.

## Inhoudsopgave

- [Woningwaardering](#woningwaardering)
  - [Inhoudsopgave](#inhoudsopgave)
  - [Implementatie Beleidsboek Huurcommissie](#implementatie-beleidsboek-huurcommissie)
    - [2024. Zelfstandige Woonruimten.](#2024-zelfstandige-woonruimten)
      - [_4.2 Oppervlakte van Vertrekken_](#42-oppervlakte-van-vertrekken)
        - [_4.2.1 Wat zijn vertrekken?_](#421-wat-zijn-vertrekken)
        - [_4.2.2 Hoe wordt de oppervlakte van vertrekken gemeten?_](#422-hoe-wordt-de-oppervlakte-van-vertrekken-gemeten)
  - [Opzet woningwaardering](#opzet-woningwaardering)
    - [Repository-structuur](#repository-structuur)
    - [Design](#design)
    - [Referentiedata](#referentiedata)
  - [Contributing](#contributing)
    - [Setup](#setup)
    - [Naamgeving van classes](#naamgeving-van-classes)
      - [Stelsels](#stelsels)
      - [Stelselgroepen](#stelselgroepen)
      - [Stelselgroepversies](#stelselgroepversies)
    - [Testing](#testing)
      - [Conventies voor Tests](#conventies-voor-tests)
    - [Datamodellen](#datamodellen)
      - [Uitbreidingen op datamodellen](#uitbreidingen-op-datamodellen)
    - [Referentiedata](#referentiedata-1)

## Implementatie Beleidsboek Huurcommissie

Voor het berekenen van een woningwaardering worden de [beleidsboeken van de Nederlandse Huurcommissie](https://www.huurcommissie.nl/huurcommissie-helpt/beleidsboeken) voor de waarderingstelsels voor zelfstandige en onzelfstandige woningen gevolgd.
De beleidsboeken van de Huurcommissie Nederland volgen Nederlandse wet- en regelgeving zoals beschreven in [Artikel 14 van het "Besluit huurprijzen woonruimte"](https://wetten.overheid.nl/BWBR0003237/2024-01-01#Artikel14).

Om berekeningen te maken met betrekking tot een woningwaardering wordt het gepubliceerde beleid vertaald naar Python-code.
Een woningwaardering wordt gemaakt op basis van woningelementen.
De stelselgroepen waarop gescoord wordt, zijn vastgelegd in het [woningwaarderingstelselgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP) op www.coraveraonline.nl.
Deze worden aangehouden in de opzet van de `woningwaardering`-package.
Voor elke stelselgroep wordt een apart Python-object gemaakt met een naam die overeenkomt met [woningwaarderingstelselgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP).
Elk stelselgroep-object zal mee veranderen met nieuw gepubliceerde wet- en regelgeving, die is opgenomen in de [beleidsboeken van de Nederlandse Huurcommissie](https://www.huurcommissie.nl/huurcommissie-helpt/beleidsboeken).

In de onderstaande hoofdstukken gaan we de beleidsboeken bij langs om aan te geven welke regels we hebben kunnen implementeren in de package en welke regels we niet hebben kunnen implementeren. De regels die we niet hebben kunnen implementeren en de gebruiker van de package daarom zelf rekening mee moet houden zijn ~~doorgestreept~~.

> Commentaar van de ontwikkelaars van deze package op het beleidsboek in dit soort blokken

### 2024. Zelfstandige Woonruimten.

#### _4.2 Oppervlakte van Vertrekken_

##### _4.2.1 Wat zijn vertrekken?_

_Het eerste onderdeel van de woningwaardering is de oppervlakte van vertrekken. Onder vertrek-
ken worden woonkamer, andere kamers (hobbykamer, studeerkamer, slaapkamer en eetkamer),
keuken, badkamer of doucheruimte verstaan. De waardering van vertrekken is 1 punt per m2
.
Geen vertrekken zijn: schuren, zolderberging, kelders, wasruimten, bijkeukens, garages en bergingen,
gang, (speel)hal en zogenoemde verkeersruimten (bijvoorbeeld overlopen). De oppervlakte van
deze ruimten tellen dus niet mee als vertrekken.
De Huurcommissie geeft op een aantal punten nadere invulling aan de hierboven genoemde
wettelijke begrippen. Dat wordt hierna beschreven._

**_Woonkamer of andere kamer_**

_Een woonkamer of een andere kamer is dus een vertrek in de zin van het
woningwaarderingsstelsel._

_Hiervan is alleen sprake als:_

- ~~_De vloer begaanbaar is._~~
- ~~_De muren en wanden uit vast materiaal bestaan._~~
- ~~_En de daglichttoetreding, de ventilatiemogelijkheid en het aantal elektrische lichtpunten in overeenstemming zijn met de geldende verkeersopvattingen._~~
- _De ruimte een oppervlakte heeft van minimaal 4 m2._
- ~~_De ruimte over de volle lengte ten minste 1,50 m breed is._~~
- ~~_De ruimte over ten minste 50% van de oppervlakte een vrije hoogte heeft van 2.10 m (gemeten
  vanaf de vloer tot het zichtbare plafond)._~~

_Alleen als aan al deze eisen is voldaan, wordt de (oppervlakte van de) woonruimte of andere
kamer meegeteld als “vertrek”. Zo niet, dan wordt de oppervlakte meegeteld als “overige ruimte”
(zie paragraaf 4.3.).
Uitzondering hierop geldt voor de keuken: de eisen van minimaal 4 m2 en ~~minimaal 1,50 m
breedte~~ gelden niet voor de keuken en verzetten zich er dus niet tegen om een keuken als “vertrek” aan te merken en overeenkomstig te waarderen_.

**_Badkamer of doucheruimte_**

_Een badkamer of doucheruimte is dus een vertrek in de zin van het woningwaarderingsstelsel._

_Hiervan is alleen sprake als:_

- ~~_De vloer begaanbaar is._~~
- ~~_De muren en wanden uit vast materiaal bestaan._~~
- ~~_En de ventilatiemogelijkheid en het aantal elektrische lichtpunten in overeenstemming zijn met
  de geldende verkeersopvattingen._~~
- ~~_De ruimte over ten minste 50% van de oppervlakte een vrije hoogte heeft van 2,00 m. (gemeten vanaf de vloer tot het zichtbare plafond)._~~

_~~Alleen als aan al deze eisen is voldaan, wordt de (oppervlakte van de) badkamer of doucheruimte
meegeteld als “vertrek”.~~ Zo niet, dan wordt de oppervlakte meegeteld als “overige ruimte” (zie
verderop)._

_Voor gecombineerde bad-/doucheruimte met toilet geldt een minimale oppervlakte van 0,64 m²_.

> In feite komt dit erop neer dat elke bad- of doucheruimte dat als vertrek is aangemerkt wordt meegeteld als vertrek voor deze Stelselgroep, tenzij de bad of doucheruimte een toilet bevat, of een `Badkamer/toilet` is, en de oppervlakte kleiner is dan 0,64 m² na aftrek van 1 m2 voor het hebben van een toilet (zie 5. in 4.2.2).

**_Zolderruimte_**

_Zolderruimten zijn in het algemeen “overige ruimte”. Echter, in geval een zolderruimte een functie
heeft als “vertrek” (dus woonkamer, andere kamers, badkamer of doucheruimte), en ook voldoet
aan de eisen die daarvoor gelden (zie hierboven), dan mag de zolderruimte meetellen als “vertrek”,
mits deze ruimte bereikbaar is via een vaste trap ~~en het dak beschoten is~~._

##### _4.2.2 Hoe wordt de oppervlakte van vertrekken gemeten?_

_De wetgever heeft in de toelichting op het woningwaarderingsstelsel een aantal meetinstructies
meegegeven:_

1. _~~Meting van de oppervlakte van vertrekken vindt plaats van muur tot muur, op een hoogte van
   1,50 m boven de vloer~~, inclusief de oppervlakte van alle tot de woning behorende losse en
   vaste kasten (kleiner dan 2m²). ~~Deze meethoogte geldt ook als de oppervlakte afwijkt van die
   op vloerniveau.~~_

_De Huurcommissie hanteert hierbij de volgende uitgangspunten._

_~~Als er sprake is van een pui wordt de binnenzijde van die pui (het kozijn) genomen. Een erker
wordt meegerekend indien deze inwendig een vrije hoogte heeft van ten minste 1,50 m. Indien er
sprake is van een zgn. entresol (tussenverdieping) dan dient de oppervlakte onder en/of boven
deze entresol te worden meegerekend, indien de vrije hoogte ten minste 1,50m bedraagt.~~ Voor
het meten van vertrekken die met elkaar in open verbinding staan, zie verderop.
“Alle tot de woning behorende losse en vaste kasten” lees de Huurcommissie als: “alle tot de
vertrekken behorende kasten”. De plaats van de deur van de kast bepaalt bij welk vertrek de kast
behoort. Dus een kast die in een vertrek uitkomt wordt, ongeacht de afmeting, bij dat vertrek
geteld. Dat geldt ook voor het waarderen van een kastenwand tussen twee vertrekken._

- _Van vaste kasten (kleiner dan 2m²) wordt de netto oppervlakte bepaald en bij de oppervlakte
  van het betreffende vertrek opgeteld;_
- _Een kast, (kleiner dan 2m²) waarvan de deur uitkomt op een verkeersruimte, wordt niet
  gewaardeerd;_
- _Losse kasten zijn niet van belang bij het meten. De oppervlakte van het vertrek wordt bepaald,
  incl. de oppervlakte die wordt ingenomen door een losse kast;_

> Binnen het woningwaarderingsstelsel mag onder bepaalde voorwaarden de oppervlakte van vaste kasten worden opgeteld bij de ruimte waar de deur van de kast zich bevindt. Als hier bij het inmeten geen rekening mee gehouden is, kan het attribuut `verbonden_ruimten` gebruikt worden om de met een ruimte verbonden vaste kasten mee te laten nemen in de waardering. Hiervoor is de VERA referentiedata binnen deze repository uitgebreid met ruimtedetailsoort Kast, code KAS.

2. _~~Als oppervlakte van een vertrek met een (ten dele) hellend of verlaagd plafond geldt dat
   alleen het gedeelte waarboven het plafond ten minste 1,50m hoog is wordt meegeteld bij de
   berekening van de oppervlakte.~~_

~~De Huurcommissie eist in geval van een (ten dele) hellend plafond dat de 1,50m-hoogte loopt tot
het dakbeschot of tot het zichtbare dakvlak of plafond. Met gordingen en balken wordt bij de
meting geen rekening gehouden.~~

3. ~~De vloeroppervlakte onder aanrechten, toestellen in de keuken, badkuip, lavet of douchebak,
   moederhaard, c.v.-ketel en boilerinstallatie, wordt meegeteld.~~

_~~De Huurcommissie gaat hier als volgt mee om. Indien zich in een vertrek, of in een kast in een
vertrek, een gas- en/of elektrameter bevindt, dan wordt de oppervlakte gewaardeerd onder aftrek
van 30 x 60 cm (minimale afmeting meterkast bestaande bouw).
De vloeroppervlakte onder radiatoren wordt meegeteld.~~_

4. _~~De oppervlakte die wordt ingenomen door schoorsteenkanalen, ventilatiekanalen of stand- of
   grondleidingen (tenzij horizontale leidingen, zie hierna) wordt niet meegeteld.~~_

_~~Bij een schoorsteenmantel en/of rookkanaal (die naar boven of beneden breed kan uitlopen) is de
oppervlakte op 1,50m-hoogte bepalend. De oppervlakte die wordt ingenomen door standleidin-
gen (verticale leidingen) wordt niet meegeteld.
De oppervlakte die wordt ingenomen door grondleidingen (horizontale leidingen), wordt wel
meegeteld.~~_

5. _Indien een toilet in een badruimte of doucheruimte is geplaatst, wordt de oppervlakte van die
   ruimte met één vierkante meter verminderd._

6. ~~_Van de oppervlakte onder een open dan wel gesloten vaste trap geldt dat gedeelte waar de
   ruimte tussen vloer en onderkant trap ten minste 1,50m hoog is._~~

7. _Afronding van de oppervlakte op hele vierkante meters vindt plaats na saldering van de
   oppervlakte van alle vertrekken; bij 0,5m² of meer wordt afgerond naar boven, bij minder dan
   0,5m² naar beneden. Waardering in punten vindt na saldering en afronding plaats._

_De Huurcommissie licht dit als volgt toe:
Afronding: eerst de oppervlakte per vertrek op 2 decimalen afronden en pas daarna de oppervlak-
te van alle vertrekken salderen en afronden op hele vierkante meters._

**_Voorbeeld:_**
_kamer : lengte 3,76m x breedte 4,12m = 15,4912 m², afgerond : 15,49 m²
keuken: lengte 2,95m x breedte 3,81m = 11,2395 m², afgerond : 11,24 m²
Totaal : 26,73 m² Afronding op hele m² : 27 m²._

8. ~~_Twee vertrekken die met elkaar in verbinding staan, worden in een bepaald geval als één
   vertrek gewaardeerd. Dit is het geval als zich tussen die twee vertrekken een opening bevindt,
   die breder is dan 50% van de muur, waarin deze opening zich bevindt (zie schets hieronder).
   Het moet hierbij gaan om een niet afsluitbare opening, die doorloopt tot aan de vloer. De muur
   wordt gemeten in het vertrek, waarin de tussenwand het smalst is._~~

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
