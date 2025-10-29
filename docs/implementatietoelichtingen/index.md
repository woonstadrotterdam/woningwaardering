# Implementatietoelichtingen

Deze sectie bevat gedetailleerde toelichtingen over de implementatie van de verschillende onderdelen:

1. [Zelfstandige Woonruimten](zelfstandige-woonruimten.md) - Toelichting op de implementatie van het beleidsboek zelfstandige woonruimten
2. [Onzelfstandige Woonruimten](onzelfstandige-woonruimten.md) - Toelichting op de implementatie van het beleidsboek onzelfstandige woonruimten
3. [Datamodel Uitbreidingen](datamodel-uitbreidingen.md) - Toelichting op de uitbreidingen op het VERA datamodel 

In deze toelichtingen wordt bijgehouden welke onderdelen van het beleidsboek wel en niet zijn geïmplementeerd per stelselgroep. De gepubliceerde tekst uit het beleidsboek wordt gekopieerd en wanneer een onderdeel niet in de code van de package is geïmplementeerd zal dit worden aangegeven met ~~doorgestreepte tekst~~.
De reden van het niet implementeren van een regelonderdeel is vrijwel altijd dat het technisch niet mogelijk is op basis van het inputmodel van de VERA-standaard. Een voorbeeld hiervan is dat voor oppervlakte van vertrekken de minimale breedte van een vertrek over de volledige lengte 1,5m moet zijn. Omdat wij de data van de minimale breedte over de volledige lengte niet binnenkrijgen via het inputmodel kunnen wij dit onderdeel van de regel niet implementeren. Dit betekent dat het aan de gebruiker is om met deze regelonderdelen rekening te houden bij het eenheid-inputmodel. Een deel van de deze regelonderdelen wordt al afgevangen indien het eenheid-inputmodel voldoet aan de NEN-norm. Regels die wel zijn geïmplementeerd zijn niet doorgestreept. Keuzes die zijn gemaakt en of interpretaties die zijn gedaan, worden in een gemarkeerd blok weergegeven zoals hieronder is gedaan.

> [!NOTE]
> Dit is een tekstblok waarmee commentaar van een developer wordt aangegeven in het beleidsboek.
