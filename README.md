# woningwaardering

De `woningwaardering` package is een opensource package met daarin functionaliteiten voor het berekenen van een woningwaardering op basis van het gepubliceerde woningwaarderingstelsel door de Nederlandse huurcomissie.
Dit project is een initiatief van Woonstad Rotterdam.

## Implementatie Beleidsboek Huurcommissie
Voor het berekenen van een woningwaardering worden de [beleidsboeken van de Nederlande Huurcommisie](https://www.huurcommissie.nl/huurcommissie-helpt/beleidsboeken) voor de waarderingstelsels voor zelfstandige en onzelfstandige woningen gevolgd.
De beleidsboeken van de huurcommissie Nederland volgen Nederlandse wet en regelgeving zoals beschreven in [Artikel 14 van het "Besluit huurprijzen woonruimte"](https://wetten.overheid.nl/BWBR0003237/2024-01-01#Artikel14).

Om berekening te maken met betrekking tot een woningwaardering wordt het gepubliceerde beleid vertaald naar python code. 
Een woningwaardering wordt gemaakt op basis van woning elementen.
De groepen waarop gescored wordt, zijn vastgelegd in het [woningwaarderingstelgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP) op www.coraveraonline.nl.
Deze worden aangehouden in de opzet van de `woningwaardering` package.
Voor elke groep wordt een apart python object gemaakt met de een naam die overeenkomt met [woningwaarderingstelgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP).
Elk groep-object zal mee veranderen met nieuw gepubliceerde wet en regelgeving, welke opgenomen is in de [beleidsboeken van de Nederlande Huurcommisie](https://www.huurcommissie.nl/huurcommissie-helpt/beleidsboeken).

### CORA Naamconventie groep-object
elk beleids onderdeel eigen class -> naming

## Opzet woningwaardering package
Het design van de `woningwaardering` package is zo gekozen dat groep-objecten en bijbehorende regels modular zijn.
Dit houdt in dat regels in een groep-object vervangbaar en inwisselbaar zijn met als resultaat dat op basis van de geven input de woningwaardering berekend wordt met de juiste set aan groep-objecten en bijbehorende regels.
Ook wanneer een wet verandert met ingang op een bepaalde datum.
De `woningwaardering` package selecteert op basis van een peildatum de juiste set aan regels die voglens de Nederlandse wet gelden voor de desbetreffende peildatum.
Hieronder is het modulaire prinicipe op basis van een peildatum schematisch weergegeven voor de het groep-object `OppervlakteVanVertrekken`.
Voor de duidelijkheid, onderstaand voorbeeld is niet gebaseerd op een echte verandering in het beleidshandboek.
Onderstaand voorbeeld laat zien hoe de berekening van de `OppervlakteVanVertrekken` afhangt van de peildatum.
Op basis van de peildatum wordt voor de bovenste beleids regel gekozen omdat die berekening geldig is voor de gegeven peildatum.

![Voorbeeld modulare oppervlakte van vertrekken](./docs/afbeeldingen/oppervlakte_van_vertrekken.png)

### Refenrentie Data
Onder referentie data worden constanten, variabelen en tabellen verstaand die nodig zijn in het berekenen van een score.
In de package wordt csv gebruikt als bestandtype voor het opslaan van referentie data.
De keuze op csv is gevallen omdat referentie data soms bestaat uit meerdere data rijen.
Daarnaast, in de package wordt een peildatum gebruikt om de juiste waarde van bijvoorbeeld een variable te selecteren.
Hierdoor heeft een variabele altijd een peildatum nodig en zal deze ook geregistreed moeten worden.
Het gevolg hiervan is dat er altijd een peildatum kolom onstaat in het csv bestand.
Aan te raden is voor vscode gebruikers om de extentie Excel Viewer van GrapeCity te downloaden.
Doormiddel van deze extentie kunnen csv-bestanden als tabel weergegeven worden in vscode.
Hieronder is een voorbeeld tabel te zien zoals deze met excel viewer in vscode wordt weergegeven.

![Excel Viewer](./docs/afbeeldingen/excel_viewer.png)

## Contributing
### Setup
Hoe kan je contributen

### Testing
framework: pytest
test naam conventies
