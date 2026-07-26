# A->C

## Doel

Test dat bij een energie-index het puntenaantal wordt bepaald door de indexwaarde, niet door de labelklasse op het afschrift.

De input bevat een eengezinswoning met energie-index waarde 1,48 en label A. De waarde 1,48 valt in de C-klasse (1,4 < EI ≤ 1,8). Verwacht: **22 punten** (label **A → C (Energie-index)**).

## Beleidsbron

- Implementatietoelichting: [§2.4.4 Punten voor geldige energieprestaties](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#244-punten-voor-geldige-energieprestaties)
- Beleidsboek (quote): "Bij een energie-index wordt het puntenaantal bepaald door het relevante cijfer."

## Handmatige berekening

| Gegeven                        | Waarde          |
| ------------------------------ | --------------- |
| Woningtype                     | Eengezinswoning |
| Energie-index                  | 1,48            |
| Klasse (EI 1,4–1,8)            | C               |
| Punten eengezinswoning label C | 22              |
| **Totaal**                     | **22**          |
