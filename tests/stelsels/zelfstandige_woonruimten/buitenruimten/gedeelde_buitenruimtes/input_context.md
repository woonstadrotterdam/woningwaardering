# gedeelde_buitenruimtes

## Doel

Test de waardering van twee gedeelde tuinen met verschillende `gedeeldMetAantalAdressen`-waarden.

De input bevat een tuin als buitenruimte gedeeld met 2 adressen en een tuin als gemeenschappelijke ruimte gedeeld met 3 adressen. Verwacht totaal: **3,75 punten**.

## Beleidsbron

- Implementatietoelichting: [§2.8.2 Punten voor een gemeenschappelijke buitenruimte](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#282-punten-voor-een-gemeenschappelijke-buitenruimte)
- Beleidsboek (quote): "Voor gemeenschappelijk buitenruimten worden 0,75 punten per vierkante meter toegekend, gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft."

## Handmatige berekening

| Buitenruimte         | Oppervlakte | Adressen | Berekening     | Punten   |
| -------------------- | ----------- | -------- | -------------- | -------- |
| Tuin (gedeeld met 2) | 6 m²        | 2        | (0,75 × 6) / 2 | 2,25     |
| Tuin (gedeeld met 3) | 6 m²        | 3        | (0,75 × 6) / 3 | 1,50     |
| **Totaal**           |             |          |                | **3,75** |

## Opmerkingen

- Beide tuinen voldoen aan de minimumafmeting (lengte 10 m, breedte 2–3 m).
