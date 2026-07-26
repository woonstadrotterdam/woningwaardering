# maximering

## Doel

Test de maximering van buitenruimtepunten op 15 punten wanneer privé-buitenruimten samen meer punten opleveren.

De input bevat een privétuin (30 m²) en een balkon (15 m²). Het ongecappeerde totaal overschrijdt 15 punten; verwacht eindtotaal: **15 punten**.

## Beleidsbron

- Implementatietoelichting: [§2.8.1 Punten voor privé-buitenruimte](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#281-punten-voor-privé-buitenruimte), [§2.8.8 Rekenmethode](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#287-rekenmethode)
- Beleidsboek (quote): "Voor de aanwezigheid van privé-buitenruimte(n) worden 2 punten toegekend en vervolgens per vierkante meter 0,35 punt."

## Handmatige berekening

| Component                      | Berekening | Punten    |
| ------------------------------ | ---------- | --------- |
| Privé oppervlakte (30 + 15 m²) | 45 × 0,35  | 15,75     |
| Vast bedrag privé-buitenruimte |            | 2,00      |
| Subtotaal privé                |            | 17,75     |
| Maximering (cap 15)            | 15 − 17,75 | −2,75     |
| **Totaal**                     |            | **15,00** |

## Opmerkingen

- Privé- en gemeenschappelijke categorieën worden afzonderlijk berekend voordat de cap wordt toegepast; zie [§2.8.8](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#287-rekenmethode).
