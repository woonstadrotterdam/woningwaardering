# Projectcontext

Dit project is een open-source Python-package voor het berekenen van punten volgens het woningwaarderingsstelsel (WWS). De package vertaalt gepubliceerde beleidsregels van de Nederlandse Huurcommissie naar herleidbare Python-code en gebruikt de VERA-standaard voor input en output.

De primaire context is de publieke `woningwaardering`-package. Lokale of organisatie-interne datastromen vallen buiten deze context, tenzij ze expliciet in de repositorydocumentatie zijn opgenomen.

## Bronnen Van Waarheid

- `README.md` beschrijft het doel, de juridische disclaimer, de actuele beleidsboekreferentie en de gebruikte VERA-versies.
- `pyproject.toml` bevat de package-metadata, Python-versie en vastgelegde VERA-databronnen.
- `docs/index.md` beschrijft conceptueel de package-opzet voor gebruikers (warnings-gedrag, outputstructuur).
- `docs/voor-ontwikkelaars/` bevat ontwikkelaarsafspraken over installatie, repository-structuur, naamgeving, tests, data, logging, releases en de criteriumstrategie (builders).
- `docs/implementatietoelichtingen/` legt per stelselgroep vast welke beleidsboekregels wel of niet zijn geïmplementeerd en waarom.
- Het online beleidsboek van de Huurcommissie is de officiële, actuele bron: [zelfstandige woonruimte](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-zelfstandige-woonruimte) en [onzelfstandige woonruimte](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-onzelfstandige-woonruimte). Vanaf deze pagina's klik je door naar de algemene toelichting en de stelselgroepen.
- [Wettekst](https://wetten.overheid.nl/BWBR0003237/2026-01-01) (Besluit huurprijzen woonruimte)

Controleer deze bronnen bij wijzigingen in domeinlogica. Voor puntberekeningen geldt de volgende volgorde van autoriteit: **wettekst > online beleidsboek > implementatietoelichting**. De implementatietoelichting is een kopie van het online beleidsboek en kan achterlopen; bij twijfel of tegenstrijdigheid is de hoger geplaatste bron leidend. Tegenstrijdigheden moeten altijd worden vermeld. Zie de definities _Beleidsboek_ en _Implementatietoelichting_ hieronder voor hun relatie.

## Projectgrenzen

- De package berekent woningwaarderingen op basis van een digitale representatie van een woonruimte.
- De berekening volgt het beleidsboek van de Huurcommissie.
- De input en output volgen de VERA-standaard, met de concrete versies vastgelegd in `pyproject.toml`.
- Aan berekeningen en output kunnen geen rechten worden ontleend. Gebruikers moeten documentatie, implementatietoelichtingen en openstaande issues raadplegen om resultaten goed te interpreteren.
- Wanneer VERA of beschikbare inputdata een beleidsregel niet volledig kan dragen, wordt de gekozen interpretatie in de implementatietoelichtingen beschreven.

## Begrippen

### Woningwaardering

De berekening van punten voor een woonruimte volgens het WWS. In dit project verwijst `Woningwaardering` ook naar de publieke API-klasse waarmee gebruikers een VERA-eenheid laten waarderen.

### WWS

Het woningwaarderingsstelsel: het puntensysteem waarmee de kwaliteit van woonruimte wordt gewaardeerd. De package implementeert regels uit de beleidsboeken van de Huurcommissie.

### Woonruimte

De woning of wooneenheid die we waarderen. De package onderscheidt stelsels voor zelfstandige en onzelfstandige woonruimten.

### Eenheid

De digitale representatie van een woonruimte in het VERA BVG-model, meestal `EenhedenEenheid`. Een eenheid bevat de gegevens waarop we de waardering baseren.

### Stelsel

Een waarderingsregime voor zelfstandige of onzelfstandige woonruimten. In code heten deze stelsels `zelfstandige_woonruimten` en `onzelfstandige_woonruimten`, conform de VERA-referentiedata `Woningwaarderingstelsel`. Een stelsel bepaalt welke stelselgroepen worden toegepast en welke regels geldig zijn.

### Stelselgroep

Een onderdeel van het WWS waarop afzonderlijk punten worden berekend, zoals energieprestatie, buitenruimten of sanitair. De package volgt hiervoor de VERA-referentiedata `Woningwaarderingstelselgroep`.

### Peildatum

De datum waarop de waardering wordt bepaald. De peildatum bepaalt onder meer of de berekening en het bijbehorende energielabel op die datum geldig zijn.

### Beleidsboek

De door de Huurcommissie gepubliceerde uitleg van de [wet van het WWS](https://wetten.overheid.nl/BWBR0003237/2026-01-01). Het online beleidsboek is de officiële, actuele bron: [zelfstandige woonruimte](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-zelfstandige-woonruimte) en [onzelfstandige woonruimte](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-onzelfstandige-woonruimte). De tekst van het beleidsboek vormt de inhoudelijke basis voor de implementatie, maar kan ruimte laten voor interpretatie of botsen met technische beperkingen.

### Implementatietoelichting

Een markdown-kopie van het online beleidsboek met onze interpretaties en doorhalingen. Per stelselgroep leggen we vast hoe beleidsboekregels zijn vertaald naar code. Niet-geïmplementeerde passages worden doorgestreept; keuzes en interpretaties lichten we toe in aparte blokken. Deze toelichtingen staan in `docs/implementatietoelichtingen/`. De kopie kan achterlopen op het online beleidsboek; raadpleeg daarom bij puntberekeningen altijd ook het actuele online beleidsboek en de wettekst. Wijkt het online beleidsboek af, dan is dat leidend en is de afwijking een signaal dat onze toelichting moet worden bijgewerkt.

### VERA

De sectorstandaard van Aedes voor gegevensuitwisseling in de corporatiesector. Dit project gebruikt VERA voor de structuur van input, output en referentiedata.

### BVG

Het VERA-domein voor vastgoed- en eenheidsgegevens. De gegenereerde BVG-modellen vormen de basis voor de inputmodellen van de package.

### Referentiedata

Door VERA gepubliceerde enumeraties en codetabellen, zoals `Woningwaarderingstelsel` en `Woningwaarderingstelselgroep`. Naamgeving in code volgt deze referentiedata zo veel mogelijk.

### Modeluitbreiding

Een lokale uitbreiding op gegenereerde VERA-modellen wanneer de standaard onvoldoende informatie bevat voor de WWS-implementatie. Deze uitbreidingen worden toegelicht in `docs/implementatietoelichtingen/datamodel-uitbreidingen.md`.

### Lookuptabel

Een CSV-bestand met constanten of tabulaire regeldata die nodig zijn voor puntberekeningen. CSV wordt gebruikt wanneer tabeldata in code, JSON of YAML minder leesbaar zou zijn.

### Criterium-id

Een samengestelde identifier voor een criterium in de output. Het is een pad-id: de id wordt afgeleid uit de plek in de hiërarchie, waarbij elk segment met `__` aan de id van het bovenliggende criterium wordt gekoppeld. Zie `docs/index.md` voor de gebruikersgerichte uitleg van de outputstructuur en `docs/voor-ontwikkelaars/criteriumstrategie.md` voor de builders.

### bovenliggendeCriterium

Verwijzing van een waardering naar het bovenliggende criterium binnen dezelfde stelselgroep (JSON: `bovenliggendeCriterium`). Dit veld gebruikt het generieke VERA-"Sleutels"-referentietype (`id`, `idExtern`, `idGegevensbeheerder`), zoals ook `EenheidSleutels` of `AdresSleutels` dat doen voor andere entiteiten. Zie `Structuurterminologie` hieronder voor hoe deze relatie de hiërarchie opbouwt.

### Maximering

Een waardering waarop een maximum van toepassing is. Als die waardering zelf gedeeld wordt én de naam een numeriek puntental bevat (bijv. `Maximaal 4 punten`), heet die in de output `Maximering` (of `Maximering voor …` wanneer het onderwerp onderscheidend is). Beschrijvende maximeringen zonder puntental (bijv. `Maximaal evenveel punten als aanrecht`) blijven ongewijzigd. Een maximering die alleen op het al gedeelde totaal geldt (zoals buitenruimten max. 15) behoudt ook het puntental in de naam.

### Structuurterminologie

De samenhang tussen waarderingen in de output loopt via een keten van `bovenliggendeCriterium`-verwijzingen: elke regel is een waardering met een `criterium`, en een criterium kan onderliggende criteria hebben. Het onderscheid tussen beide is scherp: een **criterium** draagt de identiteit, naam en plek in de hiërarchie (`id`, `naam`, `bovenliggendeCriterium`, `meeteenheid`) en heeft nooit punten; `punten` en `aantal` zitten op de **waardering**. Een groeperende regel (zoals een gedeeld-met- of subgroepregel) is daarom in essentie een criterium zonder punten; een regel met toegekende punten is een waardering. In de regel dragen groeperende regels geen punten, maar bij uitzondering doet een subgroep dat wel — bijvoorbeeld in de oppervlakte-stelselgroepen, waar de punten over het afgeronde groepstotaal op de subgroep zelf worden gezet; het criterium-object blijft ook dan puntenloos. Een **subgroep** is een groeperend criterium binnen een stelselgroep — het is géén stelselgroep, maar kan wel dezelfde naam dragen als de subgroep in een gemeenschappelijke stelselgroep wordt gewaardeerd (bijvoorbeeld 'Oppervlakte van vertrekken' binnen 'Gemeenschappelijke vertrekken, overige ruimten en voorzieningen'). Beschrijf de structuur met deze domeintaal — **waardering**, **criterium**, **subgroep**, **bovenliggende** en **onderliggende** — en niet met informatica-boomjargon als "knoop", "node", "leaf", "wortel", "root", "boom", "kind", "ouder" of "tree". De waardering boven een andere is de _bovenliggende_; een waardering zonder bovenliggende staat _direct onder de stelselgroep_.

### UserWarning

Een waarschuwing voor incomplete of onjuiste inputdata. De package faalt standaard op `UserWarning`, zodat gebruikers op de hoogte worden gebracht van de incomplete of onjusiste inputdata. Gebruikers kunnen het warningfilter aanpassen zodat er alsnog een woningwaarderingresultaat volgt.

### DeprecationWarning

Een waarschuwing voor verouderde input die nog wel wordt geaccepteerd. In tegenstelling tot `UserWarning` leidt dit niet tot een error; de waarschuwing wordt wel getoond en gelogd.

## Werkafspraak Voor Nieuwe Domeintermen

Voeg alleen termen toe aan dit bestand als ze betekenisvol zijn voor domeinexperts of terugkerend nodig zijn om code en documentatie te begrijpen. Implementatiedetails horen in de ontwikkelaarsdocs of in codecommentaar, niet in deze projectcontext.
