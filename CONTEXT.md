# Projectcontext

Dit project is een open-source Python-package voor het berekenen van punten volgens het woningwaarderingsstelsel (WWS). De package vertaalt gepubliceerde beleidsregels van de Nederlandse Huurcommissie naar herleidbare Python-code en gebruikt de VERA-standaard voor input en output.

De primaire context is de publieke `woningwaardering`-package. Lokale of organisatie-interne datastromen vallen buiten deze context, tenzij ze expliciet in de repositorydocumentatie zijn opgenomen.

## Bronnen Van Waarheid

- `README.md` beschrijft het doel, de juridische disclaimer, de actuele beleidsboekreferentie en de gebruikte VERA-versies.
- `pyproject.toml` bevat de package-metadata, Python-versie en vastgelegde VERA-databronnen.
- `docs/introductie/opzet.md` beschrijft de repository-opzet, waarschuwingen, lookup-tabellen en criterium-id's.
- `docs/implementatietoelichtingen/` legt per stelselgroep vast welke beleidsboekregels wel of niet zijn geïmplementeerd en waarom.
- Het online beleidsboek van de Huurcommissie is de officiële, actuele bron: [zelfstandige woonruimte](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-zelfstandige-woonruimte) en [onzelfstandige woonruimte](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-onzelfstandige-woonruimte). Vanaf deze pagina's klik je door naar de algemene toelichting en de stelselgroepen.
- `docs/voor-ontwikkelaars/` bevat ontwikkelaarsafspraken over installatie, naamgeving, tests, data, logging en releases.
- [Wettekst](https://wetten.overheid.nl/BWBR0003237/2026-01-01) (Besluit huurprijzen woonruimte)

Controleer deze bronnen bij wijzigingen in domeinlogica. Voor puntberekeningen is de volgorde van autoriteit: **wettekst > online beleidsboek > implementatietoelichting**. De implementatietoelichting is een kopie van het online beleidsboek en kan achterlopen; bij twijfel of tegenstrijdigheid gaat de hoger geplaatste bron voor, maar tegenstrijdigheden dienen altijd vermeld te worden. Zie de definities _Beleidsboek_ en _Implementatietoelichting_ hieronder voor hun relatie.

## Projectgrenzen

- De package berekent woningwaarderingen op basis van een digitale representatie van een woonruimte.
- De berekening volgt het beleidsboek van de Huurcommissie, met januari 2026 als actuele ankerdatum in de bestaande documentatie.
- De input en output volgen de VERA-standaard, met de concrete versies vastgelegd in `pyproject.toml`.
- Aan berekeningen en output kunnen geen rechten worden ontleend. Gebruikers moeten documentatie, implementatietoelichtingen en openstaande issues raadplegen om resultaten goed te interpreteren.
- Wanneer VERA of beschikbare inputdata een beleidsregel niet volledig kan dragen, wordt de gekozen interpretatie in de implementatietoelichtingen beschreven.

## Begrippen

### Woningwaardering

De berekening van punten voor een woonruimte volgens het WWS. In dit project verwijst `Woningwaardering` ook naar de publieke API-klasse waarmee gebruikers een VERA-eenheid laten waarderen.

### WWS

Het woningwaarderingsstelsel: het puntensysteem waarmee de kwaliteit van woonruimte wordt gewaardeerd. De package implementeert regels uit de beleidsboeken van de Huurcommissie.

### Woonruimte

De woning of wooneenheid die gewaardeerd wordt. De package onderscheidt stelsels voor zelfstandige en onzelfstandige woonruimten.

### Eenheid

De digitale representatie van een woonruimte in het VERA BVG-model, meestal `EenhedenEenheid`. Een eenheid bevat de gegevens waarop de waardering wordt gebaseerd.

### Stelsel

Een waarderingsregime voor zelfstandige of onzelfstandige woonruimten. In code heten deze stelsels `zelfstandige_woonruimten` en `onzelfstandige_woonruimten`, conform de VERA-referentiedata `Woningwaarderingstelsel`. Een stelsel bepaalt welke stelselgroepen worden toegepast en welke regels geldig zijn.

### Stelselgroep

Een onderdeel van het WWS waarop afzonderlijk punten worden berekend, zoals energieprestatie, buitenruimten of sanitair. De package volgt hiervoor de VERA-referentiedata `Woningwaarderingstelselgroep`.

### Peildatum

De datum waarop de waardering wordt bepaald. De peildatum bepaalt onder meer of de berekening en het bijbehorende energielabel op die datum geldig zijn.

### Beleidsboek

De door de Huurcommissie gepubliceerde uitleg van de [wet van het WWS](https://wetten.overheid.nl/BWBR0003237/2026-01-01). Het online beleidsboek is de officiële, actuele bron: [zelfstandige woonruimte](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-zelfstandige-woonruimte) en [onzelfstandige woonruimte](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-onzelfstandige-woonruimte). Beleidsboektekst is de inhoudelijke basis voor de implementatie, maar kan interpretatieruimte of technische beperkingen bevatten.

### Implementatietoelichting

Een markdown-kopie van het online beleidsboek met onze interpretaties en doorhalingen. Per stelselgroep staat hoe beleidsboekregels zijn vertaald naar code. Niet-geïmplementeerde passages worden doorgestreept; keuzes of interpretaties staan in toelichtende blokken. Deze staan in `docs/implementatietoelichtingen/`. De kopie kan achterlopen op het online beleidsboek; raadpleeg daarom bij puntberekeningen zowel de implementatietoelichting als het actuele online beleidsboek, naast de wettekst. Wijkt het online beleidsboek af, dan is dat leidend en is de afwijking een signaal dat onze toelichting bijgewerkt moet worden.

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

### CriteriumId

Een criteriumid als pad van bovenliggendcriteriumids. Regel: `onderliggendcriteriumid == bovenliggendcriteriumid + "__" + criteriumid_toevoeging`. Gedeeld-met gebruikt één toevoeging, bijv. `gedeeld_met_4_adressen`. Zie `docs/introductie/opzet.md`.

### bovenliggendeCriterium

Verwijzing van een waardering naar het directe bovenliggende criterium binnen dezelfde stelselgroep-groep (JSON: `bovenliggendeCriterium`). Geneste bovenliggendcriteria zijn toegestaan.

### UserWarning

Een waarschuwing voor incomplete of onjuiste inputdata. De package faalt standaard op `UserWarning`, zodat gebruikers ontbrekende invoer bewust moeten behandelen. Gebruikers kunnen het warning-filter aanpassen zodat er sowieso een woningwaarderinguitkomst volgt.

## Werkafspraak Voor Nieuwe Domeintermen

Voeg alleen termen toe aan dit bestand als ze betekenisvol zijn voor domeinexperts of terugkerend nodig zijn om code en documentatie te begrijpen. Implementatiedetails horen in de ontwikkelaarsdocs of in codecommentaar, niet in deze projectcontext.
