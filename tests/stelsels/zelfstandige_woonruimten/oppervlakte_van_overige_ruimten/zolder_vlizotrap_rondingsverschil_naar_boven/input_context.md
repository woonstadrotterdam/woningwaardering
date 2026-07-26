# zolder_vlizotrap_rondingsverschil_naar_boven

## Doel

Test afronding van het totaaloppervlak naar boven bij een zoldercorrectie: berging 6,85 m² + zolder 2,67 m² (vlizotrap) = 9,52 m² → 10 m² afgerond. Correctie −2,25 punten. Totaal **5,25 punten**.

## Beleidsbron

- Implementatietoelichting: [§2.2.2.1 Afronding op hele m²](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2221-afronding-op-hele-m²) en [§2.2.2.3 Zolderruimte zonder vaste trap](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2223-zolderruimte-zonder-vaste-trap)
- Beleidsboek (quote): "Als het getal op 0,50 m² of meer eindigt: rond af omhoog."

## Handmatige berekening

| Stap                  | Berekening                       | Uitkomst |
| --------------------- | -------------------------------- | -------- |
| Subtotaal oppervlakte | 6,85 + 2,67 = 9,52 m² → afgerond | 10 m²    |
| Punten subtotaal      | 10 × 0,75                        | 7,5      |
| Correctie vlizotrap   | min(5, (10−7) × 0,75)            | −2,25    |
| **Totaal**            |                                  | **5,25** |

## Opmerkingen

- Complement op `zolder_vlizotrap_rondingsverschil_naar_beneden`: hier stuurt afronding omhoog het totaal en daarmee de correctie.
