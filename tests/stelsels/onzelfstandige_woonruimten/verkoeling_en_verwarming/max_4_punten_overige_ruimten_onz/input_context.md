# max_4_punten_overige_ruimten_onz

## Doel

Test maximering van 4 punten voor verwarmde overige ruimten.

## Beleidsbron

- Implementatietoelichting: [§2.3 Rubriek 3: Verwarming en verkoeling](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#23-rubriek-3-verwarming-en-verkoeling)
- Beleidsboek (quote):
  "2 punten per verwarmd gemeenschappelijk vertrek / onzelfstandige wooneenheden met toegang"
  "1 punt per verwarmde gemeenschappelijke overige ruimte of gemeenschappelijke verkeersruimte (tot maximaal 4 punten) / onzelfstandige wooneenheden met toegang en gebruiksrecht"
  "1 punt extra per verwarmd én verkoeld gemeenschappelijk vertrek (tot maximaal 2 punten) / onzelfstandige wooneenheden met toegang en gebruiksrecht"

## Handmatige berekening

| Onderdeel         | Aantal | Adressen | Onz. | Punten |
| ----------------- | ------ | -------- | ---- | ------ |
| Berging           | —      | —        | 2    | 0.5    |
| Berging2          | —      | —        | 2    | 0.5    |
| Berging3          | —      | —        | 2    | 0.5    |
| Berging4          | —      | —        | 2    | 0.5    |
| Berging5          | —      | —        | 2    | 0.5    |
| Maximaal 4 punten | —      |          |      | -0.5   |
| **Totaal**        |        |          |      | **2**  |

## Opmerkingen

- Attributen `verwarmd` en `verkoeld` zijn project-specifieke uitbreidingen op het VERA-model (zie implementatietoelichting §2.3).
