# max_2_punten_verkoelde_en_verwarmde_vertrekken_onz

## Doel

Test maximering van 2 punten voor verkoelde én verwarmde vertrekken.

## Beleidsbron

- Implementatietoelichting: [§2.3 Rubriek 3: Verwarming en verkoeling](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#23-rubriek-3-verwarming-en-verkoeling)
- Beleidsboek (quote): "2 punten per verwarmd privévertrek, 1 punt per verwarmde privé overige ruimte (max. 4), en 1 extra punt per verwarmd én verkoeld privévertrek (max. 2)."

## Handmatige berekening

| Onderdeel         | Aantal | Punten |
| ----------------- | ------ | ------ |
| Slaapkamer1       | —      | 1      |
| Slaapkamer2       | —      | 1      |
| Slaapkamer3       | —      | 1      |
| Slaapkamer1       | —      | 0.5    |
| Slaapkamer2       | —      | 0.5    |
| Slaapkamer3       | —      | 0.5    |
| Maximaal 2 punten | —      | -0.5   |

## Opmerkingen

- Attributen `verwarmd` en `verkoeld` zijn project-specifieke uitbreidingen op het VERA-model (zie implementatietoelichting §2.3).
