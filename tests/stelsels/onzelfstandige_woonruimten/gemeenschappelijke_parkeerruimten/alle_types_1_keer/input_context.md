# alle_types_1_keer

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

Gedeeld met 10 adressen en 2 onzelfstandige woonruimten (9 / 10 / 6 / 10 / 4 / 10 per type).

| Onderdeel                               | Aantal | Punten |
| --------------------------------------- | ------ | ------ |
| Type I (gedeeld /10 adressen /2 onz.)   | 1      | 0.45   |
| Type II (gedeeld /10 adressen /2 onz.)  | 1      | 0.3    |
| Type III (gedeeld /10 adressen /2 onz.) | 1      | 0.2    |
| Afronding                               |        | 0.05   |
| **Totaal**                              |        | **1**  |
