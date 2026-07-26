# zolder_vlizotrap_rondingsverschil_naar_beneden

## Doel

Test afronding van het totaaloppervlak naar beneden bij een zoldercorrectie: berging 6,0 m² + zolder 4,4 m² (vlizotrap) = 10,4 m² → 10 m² afgerond. Correctie −3 punten. Totaal **4,5 punten**.

## Beleidsbron

- Implementatietoelichting: [§2.2.2.1 Rekenregels overige ruimten](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#2221-rekenregels-vertrekken) en [§2.2.2.3 Zolderruimte zonder vaste trap](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#2223-zolderruimte-zonder-vaste-trap)
- Beleidsboek (quote):
  "Als het getal eindigt op 0,49 m² of lager wordt naar beneden afgerond. Bijvoorbeeld: 15,43 m² wordt 15 m²."

## Handmatige berekening

| Stap                  | Berekening                     | Uitkomst |
| --------------------- | ------------------------------ | -------- |
| Subtotaal oppervlakte | 6,0 + 4,4 = 10,4 m² → afgerond | 10 m²    |
| Punten subtotaal      | 10 × 0,75                      | 7,5      |
| Correctie vlizotrap   | min(5, (10−6) × 0,75)          | −3,0     |
| **Totaal**            |                                | **4,5**  |

## Opmerkingen

- De correctie wordt berekend op basis van afgeronde totaaloppervlakten, niet per ruimte afzonderlijk.
