# ruimte_meer_of_minder_dan_4m2

## Doel

Test de grens van 4 m² voor reguliere vertrekken versus uitzonderingen: keuken en badkamer tellen altijd mee; slaapkamer ≥ 4 m² wel, slaapkamer 3 m² niet. Totaal **8 punten**.

## Beleidsbron

- Implementatietoelichting: [§2.2.1.2 De voorwaarden van een vertrek](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2212-de-voorwaarden-van-een-vertrek)
- Beleidsboek (quote): "minimaal 4,00 m² groot zijn" en "een ruimte die uitsluitend als keuken, badkamer of doucheruimte is bestemd altijd een vertrek is."

## Handmatige berekening

| Ruimte          | Oppervlakte | Meetelt als vertrek? | Punten |
| --------------- | ----------- | -------------------- | ------ |
| Keuken          | 2 m²        | ja (altijd vertrek)  | 2      |
| Slaapkamer      | 3 m²        | nee (< 4 m²)         | 0      |
| Slaapkamer      | 4 m²        | ja                   | 4      |
| Badkamer/toilet | 2 m²        | ja (altijd vertrek)  | 2      |
| **Totaal**      |             |                      | **8**  |

## Opmerkingen

- De slaapkamer van 3 m² kan in rubriek 2 als overige ruimte meetellen; zie `vertrek_wordt_overige_ruimte`.
