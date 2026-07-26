# parkeervak<12m2

## Doel

Test dat een parkeervak met oppervlakte kleiner dan 12 m² niet wordt gewaardeerd.

De input bevat twee parkeerplekken buiten (type III) van 11 m², gedeeld met 10 adressen. Verwacht: **0 punten**, geen waarderingsregels.

## Beleidsbron

- Implementatietoelichting: [§2.10.3 Punten per soort parkeerplek](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2103-punten-per-soort-parkeerplek)
- Beleidsboek (quote): "Een parkeerplek is een afgebakend vak en heeft een oppervlakte van minimaal 12 m² waarin een gangbare personenauto in zijn geheel past."

## Opmerkingen

- Breedte × lengte (3 × 4 m) zou 12 m² zijn, maar de opgegeven `oppervlakte` is 11 m²; die waarde is leidend.
