# 2_aanrechten_waarvan_1_geen_detailsoort

## Doel

Test dat bij twee aanrechten in één keuken alleen het aanrecht met `detailSoort` aanrecht meetelt. Het tweede element zonder detailsoort wordt genegeerd; het overgebleven aanrecht van 2000 mm levert **7 punten** op.

## Beleidsbron

- Implementatietoelichting: [§2.5.2 Punten voor basisvoorzieningen keuken](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#252-punten-voor-basisvoorzieningen-keuken)
- Beleidsboek (quote): "Langer dan 2 meter" aanrechtblad levert 7 punten op.

## Handmatige berekening

| Onderdeel              | Lengte  | Detailsoort | Punten |
| ---------------------- | ------- | ----------- | ------ |
| Aanrecht 1             | 2000 mm | AAN         | 7      |
| Aanrecht 2 (genegeerd) | 2000 mm | ontbreekt   | —      |

## Opmerkingen

- Elk geldig aanrecht wordt afzonderlijk gewaardeerd; een element zonder detailsoort kan niet als aanrecht worden herkend.
