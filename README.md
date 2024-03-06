# woningwaardering

De `woningwaardering` package is een opensource package met daarin functionaliteiten voor het berekenen van een woningwaardering op basis van het woningwaarderingstelsel.
Dit porject is een initiatief van Woonstad Rotterdam.

## Implementatie Beleidshandboek
Voor het berekenen van een woningwaardering worden de [beleidsboeken van de Nederlande Huurcommisie](https://www.huurcommissie.nl/huurcommissie-helpt/beleidsboeken) voor de waarderingstelsels voor zelfstandige en onzelfstandige woningen gevolgd.
De beleidsboeken van de huurcommissie Nederland volgen Nederlandse wet en regelgeving.

Om berekening te maken met betrekking tot een woningwaardering wordt het gepubliceerde beleid vertaald naar python code. 
Een woningwaardering wordt gemaakt op basis van woning elementen.
De groepen waarop gescored wordt, zijn vastgelegd in het [woningwaarderingstelgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP) op www.coraveraonline.nl.
Deze worden aangehouden in de opzet van de `woningwaardering` package.
Voor elke groep wordt een apart python object gemaakt met de een naam die overeenkomt met [woningwaarderingstelgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP).
Elk groep-object zal mee veranderen met nieuw gepubliceerde wet en regelgeving, welke opgenomen is in de [beleidsboeken van de Nederlande Huurcommisie](https://www.huurcommissie.nl/huurcommissie-helpt/beleidsboeken)

### Naamconventie: CORA

## woningwaardering: Generiek & modular

## Contributing
### Setup
### Testing
