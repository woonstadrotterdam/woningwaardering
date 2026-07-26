# vertrek_verkoeld_en_verwarmd_onz

## Doel

Test extra verkoelingspunt (1) bovenop verwarmingspunten (2) voor een vertrek dat zowel verwarmd als verkoeld is. Gedeelde variant met verdeling over onzelfstandige woonruimten.

## Beleidsbron

- Implementatietoelichting: [§2.3.3 Extra punten bij verkoelingsfunctie](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#233-extra-punten-bij-verkoelingsfunctie)
- Beleidsboek (quote):
  "**Alleen vertrekken** komen in aanmerking voor een waardering door een verkoelingsfunctie. Er kan 1 punt worden behaald per vertrek tot een maximum van 2 punten."

## Handmatige berekening

| Onderdeel  | Aantal | Adressen | Onz. | Punten  |
| ---------- | ------ | -------- | ---- | ------- |
| Slaapkamer | —      | —        | 2    | 1       |
| Slaapkamer | —      | —        | 2    | 0.5     |
| **Totaal** |        |          |      | **1.5** |

## Opmerkingen

- Attributen `verwarmd` en `verkoeld` zijn project-specifieke uitbreidingen op het VERA-model (zie implementatietoelichting §2.3).
