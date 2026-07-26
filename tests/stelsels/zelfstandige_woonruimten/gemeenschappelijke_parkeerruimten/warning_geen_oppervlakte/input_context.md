# warning_geen_oppervlakte

## Doel

Test dat een gemeenschappelijke parkeerplek zonder `oppervlakte` een waarschuwing geeft en niet wordt gewaardeerd (minimum 12 m² kan niet worden gecontroleerd).

De input bevat twee parkeerplekken buiten (type III) met lengte en breedte maar zonder oppervlakte. Verwacht: **0 punten** en een `UserWarning`.

## Beleidsbron

- Implementatietoelichting: [§2.10.3 Punten per soort parkeerplek](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2103-punten-per-soort-parkeerplek)
- Beleidsboek (quote): "Een parkeerplek is een afgebakend vak en heeft een oppervlakte van minimaal 12 m² waarin een gangbare personenauto in zijn geheel past."

## Opmerkingen

- Lengte (4 m) × breedte (3 m) zou 12 m² kunnen opleveren, maar zonder `oppervlakte` wordt de parkeerplek niet gewaardeerd.
- Activeer `warnings.simplefilter("default", UserWarning)` om de warning zichtbaar te maken bij handmatig draaien.
