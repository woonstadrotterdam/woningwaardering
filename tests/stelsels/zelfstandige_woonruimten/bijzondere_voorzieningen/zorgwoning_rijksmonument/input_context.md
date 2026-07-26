# zorgwoning_rijksmonument

## Doel

Test dat de zorgwoning-puntenverhoging (35%) hetzelfde uitvalt wanneer de eenheid tevens als rijksmonument is aangemerkt.

De input combineert `doelgroep` Zorg, `monumenten` rijksmonument en een woonkamer. Verwacht wordt **14,25 punten** — identiek aan de testcase `zorgwoning` zonder monument.

## Beleidsbron

- Implementatietoelichting: [§2.12 Rubriek 12: Bijzondere voorzieningen](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#212-rubriek-12-bijzondere-voorzieningen)
- Beleidsboek (quote): "Als sprake is van een zorgwoning, dan wordt het puntentotaal die de woning krijgt op basis van de rubrieken 1 t/m 11.1 van het Bhw met 35% verhoogd."

## Handmatige berekening

| Component                        | Berekening                         | Punten |
| -------------------------------- | ---------------------------------- | ------ |
| Basispuntentotaal rubrieken 1–11 | (zelfde als testcase `zorgwoning`) | 40,71  |
| Zorgwoning 35%                   | 40,71 × 0,35                       | 14,25  |

## Opmerkingen

- Monumentstatus heeft geen invloed op de berekening van de zorgwoning-puntenverhoging in rubriek 12; monumentcorrecties spelen in andere rubrieken (bijv. energieprestatie, opslagen).
