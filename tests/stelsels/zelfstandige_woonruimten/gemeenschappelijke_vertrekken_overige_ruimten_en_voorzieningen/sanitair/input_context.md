# sanitair

## Doel

Test de waardering van sanitair en extra voorzieningen in een gemeenschappelijke badruimte, gedeeld met 2 adressen.

De input bevat een badruimte (10 m²) met bad, wastafel en diverse extra voorzieningen. Verwacht totaal: **11,5 punten** (oppervlakte + sanitair, inclusief maximeringen).

## Beleidsbron

- Implementatietoelichting: [§2.9.2 Punten voor voorzieningen in gemeenschappelijke ruimten](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#292-punten-voor-voorzieningen-in-gemeenschappelijke-ruimten)
- Beleidsboek (quote): "Punten voor voorzieningen, zoals verkoeling en verwarming, keuken en sanitair, die zich bevinden in gemeenschappelijke vertrekken en overige ruimten worden gewaardeerd volgens het woningwaarderingsstelsel. Het puntenaantal moet vervolgens per rubriek worden gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft tot de ruimte."

## Handmatige berekening

| Component                      | Punten (na / 2 adressen) |
| ------------------------------ | ------------------------ |
| Oppervlakte badruimte (10 m²)  | 5,0                      |
| Wastafel                       | 0,5                      |
| Bad                            | 3,0                      |
| Extra voorzieningen (met caps) | 3,0                      |
| **Totaal**                     | **11,5**                 |

## Opmerkingen

- Sanitairpunten en extra-voorzieningenpunten worden per rubriek gedeeld door het aantal adressen; maximeringen (kastruimte, verdubbeling bad/douche) zijn in de output zichtbaar als correctieregels.
