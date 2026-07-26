# vertrek_wordt_overige_ruimte

## Doel

Test dat een vertrek (`Ruimtesoort.vertrek`) met oppervlakte tussen 2 en 4 m² (hier: slaapkamer 3 m²) in rubriek 2 als overige ruimte wordt gewaardeerd. 3 m² × 0,75 = **2,25 punten**.

## Beleidsbron

- Implementatietoelichting: [§2.2.2.2 De voorwaarden van een overige ruimte](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2222-de-voorwaarden-van-een-overige-ruimte)
- Beleidsboek (quote): "Een ruimte met `Ruimtesoort` `vertrek` komt in aanmerking voor waardering in de rubriek 'Oppervlakte van overige ruimten' als de oppervlakte minder dan 4 m² en minimaal 2 m² is."

## Handmatige berekening

| Ruimte     | Ingeschoten als | Oppervlakte | Punten              |
| ---------- | --------------- | ----------- | ------------------- |
| Slaapkamer | vertrek         | 3 m²        | 3 × 0,75 = **2,25** |

## Opmerkingen

- Complement op `ruimte_meer_of_minder_dan_4m2` in rubriek 1: dezelfde slaapkamer van 3 m² telt daar niet mee.
