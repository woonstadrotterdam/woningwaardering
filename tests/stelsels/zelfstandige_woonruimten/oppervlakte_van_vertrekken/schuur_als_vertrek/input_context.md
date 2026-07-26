# schuur_als_vertrek

## Doel

Test dat een schuur die als vertrek is ingeschoten (`Ruimtesoort.vertrek`, oppervlakte ≥ 4 m²) wordt gewaardeerd met 1 punt per m². Schuur 6 m² levert **6 punten** op.

## Beleidsbron

- Implementatietoelichting: [§2.2.1 Vertrekken](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#221-vertrekken)
- Beleidsboek (quote): "Een vertrek wordt gewaardeerd met 1 punt per vierkante meter in rubriek 1."

## Handmatige berekening

| Ruimte             | Oppervlakte | Punten |
| ------------------ | ----------- | ------ |
| Schuur als vertrek | 6 m²        | 6      |
| **Totaal**         |             | **6**  |

## Opmerkingen

- De ruimte moet als `Ruimtesoort.vertrek` zijn ingeschoten en voldoen aan de minimale oppervlakte van 4 m².
