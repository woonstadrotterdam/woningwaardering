# max_2_punten_verkoelde_en_verwarmde_vertrekken

## Doel

Test maximering van 2 punten voor verkoelde én verwarmde vertrekken.

## Beleidsbron

- Implementatietoelichting: [§2.3 Rubriek 3: Verwarming en verkoeling](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#23-rubriek-3-verwarming-en-verkoeling)
- Beleidsboek (quote):
  "2 punten per verwarmd privévertrek"
  "1 punt per verwarmde privé overige ruimte of privé verkeersruimte (tot maximaal 4 punten)"
  "1 punt extra per verwarmd én verkoeld privévertrek (tot maximaal 2 punten)"

## Handmatige berekening

| Onderdeel         | Aantal | Punten |
| ----------------- | ------ | ------ |
| Slaapkamer1       | —      | 2      |
| Slaapkamer2       | —      | 2      |
| Slaapkamer3       | —      | 2      |
| Slaapkamer1       | —      | 1      |
| Slaapkamer2       | —      | 1      |
| Slaapkamer3       | —      | 1      |
| Maximaal 2 punten | —      | -1     |

## Opmerkingen

- Attributen `verwarmd` en `verkoeld` zijn project-specifieke uitbreidingen op het VERA-model (zie implementatietoelichting §2.3).
