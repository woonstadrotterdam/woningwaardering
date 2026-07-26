# voorbeeld_beleidsboek

## Doel

Rekenvoorbeeld uit het beleidsboek: vijf carports (type II) met laadpaal en twee parkeerplekken buiten (type III), allemaal gedeeld met 10 adressen.

Verwacht totaal: **4,75 punten**.

## Beleidsbron

- Implementatietoelichting: [§2.10.3 Punten per soort parkeerplek](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2103-punten-per-soort-parkeerplek), [§2.10.5 Laadpalen](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2105-laadpalen)
- Beleidsboek (quote): "Het puntenaantal moet worden berekend door het puntenaantal per gemeenschappelijke parkeerplek te delen door aantal adressen dat toegang en gebruiksrecht heeft."

## Handmatige berekening

| Component            | Aantal | Punten/stuk | Adressen | Berekening   | Punten   |
| -------------------- | ------ | ----------- | -------- | ------------ | -------- |
| Type II carport      | 5      | 6           | 10       | (6 × 5) / 10 | 3,0      |
| Laadpaal bij carport | 5      | 2           | 10       | (2 × 5) / 10 | 1,0      |
| Type III buiten      | 2      | 4           | 10       | (4 × 2) / 10 | 0,8      |
| **Totaal**           |        |             |          |              | **4,75** |

## Opmerkingen

- Laadpalen worden per carport als bouwkundig element meegeteld; het aantal volgt `Eenhedenruimte.aantal`.
