# alle_types_gedeeld_veschillende_bovenliggende_criteriums

## Doel

Test waardering van alle parkeertypes (I, II, III) in één testcase.

## Beleidsbron

- Implementatietoelichting: [§2.10 Rubriek 10: Gemeenschappelijk parkeerruimten](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#210-rubriek-10-gemeenschappelijke-parkeerruimten)
- Beleidsboek (quote): "| Type I: een parkeerplek in een afgesloten parkeergarage behorende tot het complex | 9 |"
  (...)
  "| Type II: een parkeerplek buiten behorende tot het complex of de woning met dak (hieronder telt een carport) | 6 |"
  (...)
  "| Type III: een parkeerplek buiten behorende tot het complex of de woning zonder dak | 4 |"

## Handmatige berekening

| Onderdeel  | Aantal | Punten   |
| ---------- | ------ | -------- |
| Type I     | 1      | 1.5      |
| Type II    | 1      | 0.5      |
| Type III   | 1      | 0.27     |
| Afronding  |        | -0.02    |
| **Totaal** |        | **2.25** |
