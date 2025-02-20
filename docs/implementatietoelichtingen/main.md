# Beleidsboeken

Onderstaande beleidsboeken bevatten ontwikkelaarsnotities over de implementatie van elke stelselgroep en de gemaakte keuzes.
De tekst is gekopieerd uit het officiële beleidsboek van de Huurcommissie, waarna ontwikkelaars aanvullende keuzes en notities hebben toegevoegd.

In deze documenten wordt bijgehouden welke onderdelen van het beleidsboek wel en niet zijn geïmplementeerd per stelselgroep. De gepubliceerde tekst uit het beleidsboek wordt gekopieerd en wanneer een onderdeel niet in de code van de package is geïmplementeerd zal dit worden aangegeven met ~~doorgestreepte tekst~~.  
De reden van het niet implementeren van een regelonderdeel is vrijwel altijd dat het technisch niet mogelijk is op basis van het inputmodel van de VERA-standaard. Een voorbeeld hiervan is dat voor oppervlakte van vertrekken de minimale breedte van een vertrek over de volledige lengte 1,5m moet zijn. Omdat wij de data van de minimale breedte over de volledige lengte niet binnenkrijgen via het inputmodel kunnen wij dit onderdeel van de regel niet implementeren. **Dit betekent dat het aan de gebruiker is om met deze regelonderdelen rekening te houden bij het eenheid-inputmodel.** Een deel van de deze regelonderdelen wordt al afgevangen indien het eenheid-inputmodel voldoet aan de NEN-norm.
Regels die wel zijn geïmplementeerd zijn niet doorgestreept.
Keuzes die zijn gemaakt en of interpretaties die zijn gedaan, worden in een gemarkeerd blok weergegeven zoals hieronder is gedaan.

:::{note}
it is een notitieblok waarmee commentaar van een developer wordt aangegeven in het beleidsboek.
:::

```{toctree}
:maxdepth: 1
implementatietoelichting-beleidsboeken/zelfstandige_woonruimten
implementatietoelichting-beleidsboeken/onzelfstandige_woonruimten
```

# Datamodel Uitbreidingen

Tijdens de ontwikkeling van de woningwaardering-package komt het voor dat de VERA modellen niet toereikend zijn om de punten voor een stelselgroep te berekenen.
Daarom kunnen er indien nodig uitbreidingen gemaakt worden op de VERA modellen. In deze sectie onderbouwen en documenteren wij deze uitbreidingen.
In de [documentatie over datamodellen (VERA)](https://woningwaardering.readthedocs.io/nl/latest/contribute.html#datamodellen) wordt uitgelegd hoe uitbreidingen toegevoegd kunnen worden als contributor van dit project.

```{toctree}
:maxdepth: 2
datamodel_uitbreidingen
```

