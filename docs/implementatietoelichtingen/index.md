# Implementatietoelichtingen

Deze sectie bevat gedetailleerde toelichtingen over de implementatie van de verschillende onderdelen:

1. [Zelfstandige Woonruimten](zelfstandige-woonruimten.md) - Toelichting op de implementatie van het beleidsboek zelfstandige woonruimten
2. [Onzelfstandige Woonruimten](onzelfstandige-woonruimten.md) - Toelichting op de implementatie van het beleidsboek onzelfstandige woonruimten
3. [Datamodel Uitbreidingen](datamodel-uitbreidingen.md) - Toelichting op de uitbreidingen op het VERA datamodel 

In deze toelichtingen wordt bijgehouden welke onderdelen van het beleidsboek wel en niet zijn geïmplementeerd per stelselgroep. De gepubliceerde tekst uit het beleidsboek wordt gekopieerd en wanneer een onderdeel niet in de code van de package is geïmplementeerd zal dit worden aangegeven met ~~doorgestreepte tekst~~. Deze kopie kan achterlopen op het online beleidsboek; bij twijfel is het online beleidsboek ([zelfstandig](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-zelfstandige-woonruimte), [onzelfstandig](https://www.huurcommissie.nl/support/beleidsboeken/waarderingsstelsel-onzelfstandige-woonruimte)) leidend.
De reden van het niet implementeren van een regelonderdeel is vrijwel altijd dat het technisch niet mogelijk is op basis van het inputmodel van de VERA-standaard. Een voorbeeld hiervan is dat voor oppervlakte van vertrekken de minimale breedte van een vertrek over de volledige lengte 1,5m moet zijn. Omdat wij de data van de minimale breedte over de volledige lengte niet binnenkrijgen via het inputmodel kunnen wij dit onderdeel van de regel niet implementeren. Dit betekent dat het aan de gebruiker is om met deze regelonderdelen rekening te houden bij het eenheid-inputmodel. Een deel van de deze regelonderdelen wordt al afgevangen indien het eenheid-inputmodel voldoet aan de NEN-norm. Regels die wel zijn geïmplementeerd zijn niet doorgestreept.

Een note, het gemarkeerde blok zoals hieronder, legt een keuze van de package vast en staat:

- waar de package afwijkt van de beleidsboektekst erboven, zoals het bouwjaar in plaats van hoogniveaurenovatie bij 2.11.5;
- waar wettekst en beleidsboek een keuze openlaten die de package invult;
- waar bronnen elkaar tegenspreken; de note citeert dan de afwijkende bron letterlijk en zegt welke bron de package volgt.

Een note noemt alleen wat afwijkt van of ontbreekt in de beleidsboektekst erboven; waar de code die tekst volgt, is de tekst zelf de toelichting. Rekenvolgorde en andere codedetails staan in codecommentaar, een controle met de huurprijscheck in de pull request. De huurprijscheck staat alleen in een note als hij de bron is, omdat wettekst en beleidsboek niet sluitend zijn (zie [bronnen](../voor-ontwikkelaars/bronnen.md)), of als de package bewust een andere uitkomst geeft dan de huurprijscheck. De note noemt dan de datum en het tijdvak van de meting.

> [!NOTE]
> Dit is een tekstblok waarmee commentaar van een developer wordt aangegeven in het beleidsboek.
