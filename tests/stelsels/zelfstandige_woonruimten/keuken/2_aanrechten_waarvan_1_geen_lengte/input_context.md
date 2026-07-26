# 2_aanrechten_waarvan_1_geen_lengte

## Doel

Test dat bij twee aanrechten alleen het aanrecht met een opgegeven lengte meetelt. Het tweede aanrecht zonder lengte wordt overgeslagen; het eerste aanrecht van 2000 mm levert **7 punten** op.

## Beleidsbron

- Implementatietoelichting: [§2.5.2 Punten voor basisvoorzieningen keuken](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#252-punten-voor-basisvoorzieningen-keuken)
- Beleidsboek (quote): "Langer dan 2 meter" aanrechtblad levert 7 punten op.

## Handmatige berekening

| Onderdeel              | Lengte    | Punten |
| ---------------------- | --------- | ------ |
| Aanrecht 1             | 2000 mm   | 7      |
| Aanrecht 2 (genegeerd) | ontbreekt | —      |

## Opmerkingen

- Zonder lengte kan het aanrecht niet gewaardeerd worden; de implementatie geeft een waarschuwing.
