# open_keukens

## Doel

Test dat een open keuken en het aangrenzende vertrek afzonderlijk verwarmingspunten krijgen.

## Beleidsbron

- Implementatietoelichting: [§2.3.2 Open keuken in een vertrek of overige ruimte](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#232-open-keuken-in-een-vertrek-of-overige-ruimte)
- Beleidsboek (quote):
  "Zowel de open keuken als het vertrek of overige ruimte waarmee de open verbinding bestaat, wordt voor deze rubriek namelijk individueel gewaardeerd met punten indien deze verwarmd zijn."
  (...)
  "Een privé verwarmde woonkamer met open keuken wordt dus gewaardeerd met 4 punten."

## Handmatige berekening

| Onderdeel                  | Aantal | Punten |
| -------------------------- | ------ | ------ |
| Verwarmde woonkamer        | —      | 2      |
| Verwarmde keuken           | —      | 2      |
| Verwarmde slaapkamer       | —      | 2      |
| Verwarmde woonkamer/keuken | —      | 2      |
| Verwarmde woonkamer        | —      | 2      |
| Verwarmde slaapkamer       | —      | 2      |
| Verwarmde woonkamer/keuken | —      | 2      |

## Opmerkingen

- Attributen `verwarmd` en `verkoeld` zijn project-specifieke uitbreidingen op het VERA-model (zie implementatietoelichting §2.3).
