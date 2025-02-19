# Opzet woningwaardering package

## Implementatie beleidsboek huurcommissie

Voor het berekenen van een woningwaardering worden de [beleidsboeken van de Nederlandse Huurcommissie](https://www.huurcommissie.nl/huurcommissie-helpt/beleidsboeken) voor de waarderingstelsels voor zelfstandige en onzelfstandige woningen gevolgd.
De beleidsboeken van de Huurcommissie Nederland volgen Nederlandse wet- en regelgeving zoals beschreven in [Artikel 14 van het "Besluit huurprijzen woonruimte"](https://wetten.overheid.nl/BWBR0003237/2024-01-01#Artikel14).

Om berekeningen te maken met betrekking tot een woningwaardering wordt het gepubliceerde beleid vertaald naar Python-code.
Een woningwaardering wordt gemaakt op basis van woningelementen.
De stelselgroepen waarop gescoord wordt, zijn vastgelegd in het [woningwaarderingstelselgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP) op www.coraveraonline.nl.
Deze worden aangehouden in de opzet van de `woningwaardering`-package.
Voor elke stelselgroep wordt een apart Python-object gemaakt met een naam die overeenkomt met [woningwaarderingstelselgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP).

De woningwaardering package volgt de [beleidsboeken van de Nederlandse Huurcommissie](https://www.huurcommissie.nl/huurcommissie-helpt/beleidsboeken) en daarmee de Nederlandse wet en regelgeving m.b.t. het waarderen van woningen. Tijdens de ontwikkeling van deze package komt het voor dat we inconsistenties in de beleidsboeken vinden of dat er ruimte is voor interpretatie. Daarnaast kan het voorkomen dat dat de VERA modellen, met eventuele uitbreidingen, niet toereikend zijn om de stelselgroep voglens het beleidsboek tot op de letter nauwkeurig te implementeren. In [implementatietoelichting-beleidsboeken](https://woningwaardering.readthedocs.io/nl/latest/implementatietoelichting-beleidsboeken/zelfstandige_woonruimten.html#beleidsboek-zelfstandige-woonruimten) onderbouwen wij hoe elke stelselgroep is geïmplementeerd en welke keuzes daarin gemaakt zijn.  
In deze documenten wordt bijgehouden welke onderdelen van het beleidsboek wel en niet zijn geïmplementeerd per stelselgroep. De gepubliceerde tekst uit het beleidsboek wordt gekopieerd en wanneer een onderdeel niet in de code van de package is geïmplementeerd zal dit worden aangegeven met ~~doorgestreepte tekst~~.  
De reden van het niet implementeren van een regelonderdeel is vrijwel altijd dat het technisch niet mogelijk is op basis van het inputmodel van de VERA-standaard. Een voorbeeld hiervan is dat voor oppervlakte van vertrekken de minimale breedte van een vertrek over de volledige lengte 1,5m moet zijn. Omdat wij de data van de minimale breedte over de volledige lengte niet binnenkrijgen via het inputmodel kunnen wij dit onderdeel van de regel niet implementeren. **Dit betekent dat het aan de gebruiker is om met deze regelonderdelen rekening te houden bij het eenheid-inputmodel.** Een deel van de deze regelonderdelen wordt al afgevangen indien het eenheid-inputmodel voldoet aan de NEN-norm.
Regels die wel zijn geïmplementeerd zijn niet doorgestreept.
Keuzes die zijn gemaakt en of interpretaties die zijn gedaan, worden in een gemarkeerd blok weergegeven zoals hieronder is gedaan.

> Dit is een tekstblok waarmee commentaar van een developer wordt aangegeven in het beleidsboek.

## Repository-structuur

De repository-structuur is ingedeeld volgens de [referentiedata van stelselgroepen van de VERA-standaard](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP); eerst de stelsels (bijvoorbeeld _zelfstandig_, _onzelfstandig_) en vervolgens de stelselgroepen (bijvoorbeeld _Energieprestatie_, _Wasgelegenheid_).
In de folders van de stelselgroepen bevindt zich de code voor het berekenen van de punten per stelselgroep. Indien bepaalde logica voor zowel zelfstandige als onzelfstandige woningen gelden, dan bevinden deze regels zich in de folder _gedeelde_logcia_.

## Design

Het design van de `woningwaardering`-package is zo gekozen dat stelselgroep-objecten en bijbehorende regels modulair zijn.

## Lookup tabellen

In lookup tabellen worden constanten en variabelen opgeslagen die nodig zijn bij het berekenen van de punten voor een stelselgroep.
In de `woningwaardering` package wordt CSV gebruikt als bestandstype voor het opslaan van een lookup tabel.
De keuze is op CSV gevallen omdat lookup data soms bestaat uit meerdere datarijen waardoor dit vaak minder leesbaar wordt wanneer dit bijvoorbeeld in json of yaml wordt opgeslagen.

## Warnings

In de `woningwaardering` package worden `UserWarnings` gegenereerd wanneer de inputdata niet volledig of correct wordt aangeleverd.
Deze waarschuwingen worden gegeven met een warning bericht en een type warning, bijvoorbeeld:

```python
warnings.warn("Dit is een warning", UserWarning)
```

Standaard genereert de `woningwaardering` package een error wanneer een `UserWarning` wordt gegeven.
Hoewel de package kan werken met incomplete data, is ervoor gekozen om standaard te falen bij incomplete inputdata, zodat de gebruiker hiervan op de hoogte wordt gebracht.
Het is echter ook mogelijk om het warning filter terug te zetten naar de standaardinstellingen, waardoor een warning m.b.t. incomplete data niet leidt tot een error, maar slechts een _warning_:

```python
warnings.simplefilter("default", UserWarning)
```

Alle waarschuwingen die worden gegenereerd met `warnings.warn()`, worden standaard gelogd met `logger.warning()` en weergegeven in het standaardfout bestand.
Mocht door de gebruiker logging worden uitgezet, dan zullen de UserWarnings altijd te zien zijn voor de gebruiker in de output van de _stderr_.

### Warning vs Exception

Er wordt doorgaans in de stelgroepversies gebruik gemaakt van `warnings.warn()` in plaats van het raisen van een exception.
Hierdoor bestaat de mogelijkheid om stelselgroepen te berekenen voor stelselgroepen waarvoor de data wel compleet genoeg is, mits de `warnings.simplefilter` naar `default` is gezet.

## Criterium ID's

De `CriteriumId` class wordt gebruikt om ID's te genereren voor criteria in de woningwaardering. Deze ID's worden opgebouwd uit verschillende onderdelen die worden samengevoegd met dubbele underscores (`__`).

De opbouw van een criterium ID kan de volgende onderdelen bevatten:

- Stelselgroep (verplicht, bijvoorbeeld 'buitenruimten' of 'energieprestatie')
- Ruimte ID (optioneel, bijvoorbeeld 'Space_108014713')
- Criterium (optioneel, bijvoorbeeld 'factor_II' of 'woz_waarde')
- Gedeeld met aantal (optioneel, voor gedeelde voorzieningen)
- Gedeeld met soort (optioneel, 'adressen' of 'onzelfstandige_woonruimten')
- Totaal indicator (optioneel)

Voorbeelden van gegenereerde ID's:

- `buitenruimten__Space_108014713` (voor een specifieke ruimte)
- `buitenruimten__totaal__prive` (voor een privé totaal)
- `gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__totaal__gedeeld_met__4__adressen` (voor gedeelde voorzieningen)

Bij gedeelde voorzieningen wordt automatisch 'prive' toegevoegd als het aantal 1 of minder is, en anders wordt het aantal en soort toegevoegd (bijvoorbeeld `gedeeld_met__4__adressen`).

Met deze ID's kan gerefereerd worden aan specifieke criteria in de output van de woningwaardering.

### Criteriumsleutels

Bij sommige stelselgroepen heb je een aantal criteria die een gemeenschappelijke groep vormen. Bijvoorbeeld bij _verkoeling en verwarming_ mag je maximaal 2 extra punten krijgen voor vertrekken die verkoeld én verwarmd zijn. Daarnaast mag je ook maximaal 4 punten krijgen voor het aantal verwarmde overige- en verkeersruimten. Om te kunnen berekenen wat de som is van een subgroep en bijvoorbeeld maximering toe te passen maken wij gebruik van zogenoemde `criteriumSleutels`. Indien een waardering onderdeel is van een subgroep, dan wordt aan deze waardering in het veld `bovenliggendCriterium` de `id` toegevoegd van de waardering die hoort bij de subgroep. In het voorbeeld hieronder is bijvoorbeeld de subgroep `Verwarmde vertrekken` binnen `verkoeling en verwarming` duidelijk te zien in de output-tabel. Voorgedefinieerde criteriumsleutels vind je in `woningwaardering/stelsels/criteriumsleutels.py`. Momenteel ondersteunen wij nog geen meerdere niveau's van subgroepen. Een criterium dat voor een ander criterium een bovenliggend criterium is, mag zelf geen bovenliggend criterium hebben.
