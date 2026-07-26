# zolder_vertrek

## Doel

Test dat alleen een zolder met vaste trap meetelt als vertrek; zolders met vlizotrap of zonder trap niet.

## Beleidsbron

- Implementatietoelichting: [§2.2.1 Vertrekken](../../../../../docs/implementatietoelichtingen/onzelfstandige-woonruimten.md#221-vertrekken)
- Beleidsboek (quote):
  "de zolderruimte moet bereikbaar zijn via een vaste trap"

## Handmatige berekening

| Zolder          | Soort          | Trap  | Oppervlakte | Punten        |
| --------------- | -------------- | ----- | ----------- | ------------- |
| Met vaste trap  | vertrek        | ja    | 10 m²       | 10            |
| Zonder trap     | vertrek        | nee   | 10 m²       | 0             |
| Met vlizotrap   | vertrek        | vlizo | 10 m²       | 0             |
| Overig met trap | overige ruimte | ja    | 1 m²        | 0 (rubriek 2) |
| **Totaal**      |                |       |             | **10**        |
