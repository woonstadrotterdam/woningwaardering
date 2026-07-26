# woon_slaap_met_aanrecht

## Doel

Test dat een aanrecht (≥ 1000 mm) in diverse vertrektypes als impliciete keuken wordt gewaardeerd: woonkamer/keuken, woonkamer, woon-/slaapkamer en slaapkamer met aanrecht tellen mee; een slaapkamer zonder aanrecht niet. Totaal **22 punten**.

## Beleidsbron

- Implementatietoelichting: [§2.5.2 Punten voor basisvoorzieningen keuken](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#252-punten-voor-basisvoorzieningen-keuken)
- Beleidsboek (quote): "Het aantal punten hangt af van de lengte van het waterdichte aanrechtblad, volgens de onderstaande tabel:"

## Handmatige berekening

| Ruimte                     | Aanrechtlengte | Punten |
| -------------------------- | -------------- | ------ |
| Woonkamer/keuken           | 2000 mm        | 7      |
| Woonkamer                  | 1000 mm        | 4      |
| Woon-/slaapkamer           | 2000 mm        | 7      |
| Slaapkamer                 | 1000 mm        | 4      |
| Slaapkamer zonder aanrecht | —              | 0      |
| **Totaal**                 |                | **22** |

## Opmerkingen

- Per ruimte wordt het langste geldige aanrecht gewaardeerd; ruimtes zonder aanrecht ≥ 1 m worden overgeslagen.
