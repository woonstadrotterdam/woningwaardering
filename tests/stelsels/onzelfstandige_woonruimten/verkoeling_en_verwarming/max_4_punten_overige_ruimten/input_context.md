# max_4_punten_overige_ruimten

## Doel

Test maximering van 4 punten voor verwarmde overige ruimten.

## Beleidsbron

- Implementatietoelichting: [§2.3 Rubriek 3: Verwarming en verkoeling](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#23-rubriek-3-verwarming-en-verkoeling)
- Beleidsboek (quote):
  "2 punten per verwarmd privévertrek"
  "1 punt per verwarmde privé overige ruimte of privé verkeersruimte (tot maximaal 4 punten)"
  "1 punt extra per verwarmd én verkoeld privévertrek (tot maximaal 2 punten)"

## Handmatige berekening

| Onderdeel         | Aantal | Punten |
| ----------------- | ------ | ------ |
| Berging           | —      | 1      |
| Berging2          | —      | 1      |
| Berging3          | —      | 1      |
| Berging4          | —      | 1      |
| Berging5          | —      | 1      |
| Maximaal 4 punten | —      | -1     |

## Opmerkingen

- Attributen `verwarmd` en `verkoeld` zijn project-specifieke uitbreidingen op het VERA-model (zie implementatietoelichting §2.3).
