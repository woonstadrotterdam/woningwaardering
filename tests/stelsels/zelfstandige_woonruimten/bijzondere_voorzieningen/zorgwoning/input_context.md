# zorgwoning

## Doel

Test dat een eenheid met doelgroep `Zorg` een puntenverhoging van 35% krijgt over het totaal van rubrieken 1 t/m 11.

De input bevat `doelgroep.code` `ZOR` en een woonkamer. Verwacht wordt één waarderingsregel **Zorgwoning 35% puntenverhoging** met **14,25 punten** (35% van het berekende basispuntentotaal uit de overige rubrieken voor deze minimale input).

## Beleidsbron

- Implementatietoelichting: [§2.12 Rubriek 12: Bijzondere voorzieningen](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#212-rubriek-12-bijzondere-voorzieningen)
- Beleidsboek (quote): "Als sprake is van een zorgwoning, dan wordt het puntentotaal die de woning krijgt op basis van de rubrieken 1 t/m 11.1 van het Bhw met 35% verhoogd."

## Handmatige berekening

| Component                        | Berekening                                            | Punten    |
| -------------------------------- | ----------------------------------------------------- | --------- |
| Basispuntentotaal rubrieken 1–11 | (afgeleid uit overige stelselgroepen voor deze input) | 40,71     |
| Zorgwoning 35%                   | 40,71 × 0,35                                          | 14,25     |
| **Totaal**                       |                                                       | **14,25** |

## Opmerkingen

- Wanneer `doelgroep` Zorg is, wordt de eenheid automatisch als zorgwoning gewaardeerd; de overige zorgwoningvoorwaarden uit het beleidsboek worden niet gecontroleerd (zie [§2.12.1](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2121-voorwaarden-zorgwoning)).
- Punten uit rubriek 11.2 (WOZ-cap) tellen niet mee in de basis voor de 35%-verhoging.
