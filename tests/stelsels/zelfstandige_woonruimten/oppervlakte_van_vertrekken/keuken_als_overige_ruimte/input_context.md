# keuken_als_overige_ruimte

## Doel

Test dat een keuken (`Ruimtedetailsoort.keuken`) altijd als vertrek wordt gewaardeerd in rubriek 1, ook wanneer de ruimte is ingeschoten als `Ruimtesoort.overige_ruimte` en kleiner is dan 4 m². Oppervlakte 1 m² levert **1 punt** op.

## Beleidsbron

- Implementatietoelichting: [§2.2.1 Vertrekken](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#221-vertrekken)
- Beleidsboek (quote): "een ruimte die uitsluitend als keuken, badkamer of doucheruimte is bestemd altijd een vertrek is. Een vertrek wordt gewaardeerd met 1 punt per vierkante meter in rubriek 1."

## Handmatige berekening

| Ruimte                                  | Oppervlakte | Punten (1 p/m²) |
| --------------------------------------- | ----------- | --------------- |
| Keuken (als overige ruimte ingeschoten) | 1,00 m²     | 1               |

## Opmerkingen

- De gespecificeerde ruimtesoort in VERA is leidend voor classificatie, maar keuken-detailsoort overschrijft de minimale oppervlakte-eis voor vertrekken.
