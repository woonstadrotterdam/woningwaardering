# vertrek_verkoeld_en_verwarmd_onz

## Doel

Test extra verkoelingspunt (1) bovenop verwarmingspunten (2) voor een vertrek dat zowel verwarmd als verkoeld is. Gedeelde variant met verdeling over onzelfstandige woonruimten.

## Beleidsbron

- Implementatietoelichting: [§2.3.3 Extra punten bij verkoelingsfunctie](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#233-extra-punten-bij-verkoelingsfunctie)
- Beleidsboek (quote): "2 punten per verwarmd privévertrek, 1 punt per verwarmde privé overige ruimte (max. 4), en 1 extra punt per verwarmd én verkoeld privévertrek (max. 2)."

## Handmatige berekening

| Onderdeel  | Aantal | Punten |
| ---------- | ------ | ------ |
| Slaapkamer | —      | 1      |
| Slaapkamer | —      | 0.5    |

## Opmerkingen

- Attributen `verwarmd` en `verkoeld` zijn project-specifieke uitbreidingen op het VERA-model (zie implementatietoelichting §2.3).
