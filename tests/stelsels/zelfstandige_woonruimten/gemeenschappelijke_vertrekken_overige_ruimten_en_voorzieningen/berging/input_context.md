# berging

## Doel

Test de waardering van een gemeenschappelijke berging (overige ruimte) gedeeld met 5 adressen.

De input bevat twee bergingen (5 en 6 adressen); de verwachte output bevat alleen de berging gedeeld met 5 adressen. Verwacht: **1,5 punten**.

## Beleidsbron

- Implementatietoelichting: [§2.9 Rubriek 9: Gemeenschappelijke vertrekken, overige ruimten en voorzieningen](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#29-rubriek-9-gemeenschappelijke-vertrekken-overige-ruimten-en-voorzieningen)
- Beleidsboek (quote): "Een vertrek krijgt 1 punt per vierkante meter en een gemeenschappelijke overige ruimte wordt gewaardeerd met 0,75 punt per vierkante meter. Voor beide type ruimtes geldt dat het puntenaantal per ruimte moet worden gedeeld door het aantal adressen dat exclusieve toegang en gebruiksrecht heeft."

## Handmatige berekening

| Ruimte  | Type           | Oppervlakte | Adressen | Berekening      | Punten |
| ------- | -------------- | ----------- | -------- | --------------- | ------ |
| Berging | Overige ruimte | 10 m²       | 5        | (0,75 × 10) / 5 | 1,5    |

## Opmerkingen

- De tweede berging (6 adressen) staat in de input maar niet in `output.json`; de testcase valideert alleen de groep met 5 adressen.
