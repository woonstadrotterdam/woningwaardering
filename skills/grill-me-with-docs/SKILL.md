---
name: grill-me-with-docs
description: >-
  Scherpt een plan voor een wijziging in de woningwaardering aan door de gebruiker één vraag
  tegelijk te interviewen en elk antwoord te toetsen aan wettekst, online beleidsboek,
  implementatietoelichting, CONTEXT.md en code. Gebruik vóór de implementatie wanneer een taak
  domeinlogica, puntberekening, waarschuwings- of foutgedrag of VERA-modellering wijzigt en de
  interpretatie van de beleidsregel of de gewenste uitkomst nog niet vaststaat, of wanneer de
  gebruiker vraagt om te grillen of een plan te toetsen. Niet voor typefouten, formatting,
  dependency-updates, releases of fixes waarvan de uitkomst al vastligt.
---

<!-- Herkomst: afgeleid van grill-with-docs uit mattpocock/skills (MIT); wordt zelfstandig onderhouden. -->

# Grill me with docs

Interview de gebruiker over het plan totdat jullie het eens zijn over wat er verandert, waarom, en op welke bron dat rust.

## Kernregels

1. Stel één vraag tegelijk en wacht op het antwoord. Geef bij elke vraag je aanbevolen antwoord, met de bron waarop het rust.
2. Zoek feiten zelf op: wat de code nu doet en wat wettekst, online beleidsboek of implementatietoelichting letterlijk zeggen. Stel daar geen vraag over.
3. Leg beslissingen voor: de interpretatie van een beleidsregel, het gewenste gedrag, wat binnen de taak valt. Neem die niet zelf, ook niet wanneer de code één kant op wijst.
4. Werk beslissingen af in volgorde van afhankelijkheid: eerst de keuze waar andere keuzes van afhangen.
5. Schrijf geen code voordat de gebruiker het samengevatte plan heeft bevestigd.

## Toets elk antwoord

**Aan de domeintaal.** Wijkt een term af van `CONTEXT.md`, benoem dat direct. "Je noemt 'Oppervlakte van vertrekken' hier een stelselgroep, maar binnen 'Gemeenschappelijke vertrekken, overige ruimten en voorzieningen' is het een subgroep. Welke bedoel je?" Kan een term meer dan één ding betekenen, vraag dan welke: "Je zegt 'gedeelde keuken'. Gedeeld met andere onzelfstandige woonruimten op hetzelfde adres, of met meerdere adressen? Dat bepaalt de deler."

**Aan de bronnen.** Volg de Domeinregels in `AGENTS.md` voor de volgorde van autoriteit en voor waar je elke bron vindt. Citeer de passage letterlijk met regelnummer of artikel en met de link naar de pagina waar de tekst staat, zodat de gebruiker op de tekst reageert en niet op jouw samenvatting.

**Aan de code.** Zegt de gebruiker hoe iets werkt, controleer of de code dat ook doet en leg een verschil voor: "Je zegt dat een zolder zonder vaste trap altijd 5 punten aftrek krijgt, maar de code past dat alleen toe wanneer de zolder een overige ruimte is (beleidsboek 2.2.2.3). Welke van de twee bedoel je?"

**Aan een concreet geval.** Reken een woonruimte door die op de grens van de regel ligt, zoals een ruimte die door drie onzelfstandige woonruimten wordt gedeeld of een waarde precies op een drempel in een lookuptabel, en vraag of de uitkomst is wat de gebruiker verwacht.

## Wanneer bronnen niet sluiten

- Spreken bronnen elkaar tegen, toon dan beide citaten en zeg welke volgens de volgorde van autoriteit leidend is.
- Geven wettekst en online beleidsboek geen uitsluitsel, vraag de gebruiker dan de huurprijscheck te controleren en wacht op de uitkomst. Vul die uitkomst niet zelf in.
- Kan VERA of het inputmodel de regel niet volledig dragen, zeg dat en leg de keuze voor: een modeluitbreiding, of een gedocumenteerde interpretatie.

## Afronden

Vat het plan samen wanneer er geen open beslissing meer is: wat er verandert, de bron met citaat, de geraakte stelselgroepen, de tests en de docs die mee moeten. Vraag om bevestiging. De sessie is klaar wanneer de gebruiker dat plan heeft bevestigd.

## Vastleggen

Stel de tekst voor en schrijf die na akkoord van de gebruiker:

- Een interpretatie van een beleidsregel of een wijziging in wat wel of niet is geïmplementeerd: de relevante pagina in `docs/implementatietoelichtingen/`, met bronverwijzing en citaat.
- Een duurzaam verduidelijkte domeinterm: `CONTEXT.md`, volgens de werkafspraak onderaan dat bestand.
- Een ontwikkelaarsafspraak: `docs/voor-ontwikkelaars/`.
