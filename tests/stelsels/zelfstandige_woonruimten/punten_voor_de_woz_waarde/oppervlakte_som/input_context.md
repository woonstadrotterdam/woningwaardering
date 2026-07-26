# oppervlakte_som

## Doel

Test dat voor onderdeel II de som van vertrekken en overige ruimten wordt afgerond op hele m² (hier 30 m²) en dat de WOZ-berekening daarop gebaseerd **20,25 punten** oplevert.

## Beleidsbron

- Implementatietoelichting: [§2.11.2 Punten voor de WOZ-waarde](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2112-punten-voor-de-woz-waarde-taxatiewaarde-of-minimum-woz-waarde)
- Beleidsboek (quote):
  "Bereken eerst het aantal m² van de vertrekken (rubriek 1), overige ruimtes (rubriek 2) en parkeerplekken type I (rubriek 10)."
  (...)
  "Rond hierna de oppervlakte af op hele vierkante meters."

## Handmatige berekening

| Onderdeel | Berekening                | Punten    |
| --------- | ------------------------- | --------- |
| I         | € 100.000 / € 15.329      | 6,52      |
| II        | € 100.000 / 30 m² / € 242 | 13,77     |
| Totaal    | afgerond op kwart punt    | **20,25** |
