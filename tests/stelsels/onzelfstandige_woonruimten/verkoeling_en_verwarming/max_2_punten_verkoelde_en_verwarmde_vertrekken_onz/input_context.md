# max_2_punten_verkoelde_en_verwarmde_vertrekken_onz

## Doel

Test maximering van 2 punten voor verkoelde én verwarmde vertrekken.

## Beleidsbron

- Implementatietoelichting: [§2.3 Rubriek 3: Verwarming en verkoeling](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#23-rubriek-3-verwarming-en-verkoeling)
- Beleidsboek (quote):
  "2 punten per verwarmd gemeenschappelijk vertrek / onzelfstandige wooneenheden met toegang"
  "1 punt per verwarmde gemeenschappelijke overige ruimte of gemeenschappelijke verkeersruimte (tot maximaal 4 punten) / onzelfstandige wooneenheden met toegang en gebruiksrecht"
  "1 punt extra per verwarmd én verkoeld gemeenschappelijk vertrek (tot maximaal 2 punten) / onzelfstandige wooneenheden met toegang en gebruiksrecht"

## Handmatige berekening

| Onderdeel         | Aantal | Adressen | Onz. | Punten |
| ----------------- | ------ | -------- | ---- | ------ |
| Slaapkamer1       | —      | —        | 2    | 1      |
| Slaapkamer2       | —      | —        | 2    | 1      |
| Slaapkamer3       | —      | —        | 2    | 1      |
| Slaapkamer1       | —      | —        | 2    | 0.5    |
| Slaapkamer2       | —      | —        | 2    | 0.5    |
| Slaapkamer3       | —      | —        | 2    | 0.5    |
| Maximaal 2 punten | —      |          |      | -0.5   |
| **Totaal**        |        |          |      | **4**  |

## Opmerkingen

- Attributen `verwarmd` en `verkoeld` zijn project-specifieke uitbreidingen op het VERA-model (zie implementatietoelichting §2.3).
