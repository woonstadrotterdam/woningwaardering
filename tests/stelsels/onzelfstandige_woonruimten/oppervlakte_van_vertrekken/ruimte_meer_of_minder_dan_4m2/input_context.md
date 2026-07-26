# ruimte_meer_of_minder_dan_4m2

## Doel

Test dat een ruimte kleiner dan 4 m² niet als vertrek meetelt; verwacht totaal 8 punten voor overige vertrekken.

## Beleidsbron

- Implementatietoelichting: [§2.2.1 Vertrekken](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#221-vertrekken)
- Beleidsboek (quote):
  "minimaal 4,00 m² groot zijn (een oppervlakte van 3,50 m² of 3,95 m² is onvoldoende)"

## Handmatige berekening

| Ruimte          | Oppervlakte | Meetelt als vertrek? | Punten |
| --------------- | ----------- | -------------------- | ------ |
| Keuken          | 2 m²        | ja (altijd vertrek)  | 2      |
| Slaapkamer      | 3 m²        | nee (< 4 m²)         | 0      |
| Slaapkamer      | 4 m²        | ja                   | 4      |
| Badkamer/toilet | 2 m²        | ja (altijd vertrek)  | 2      |
| **Totaal**      |             |                      | **8**  |
