# zolder_vertrek

## Doel

Test welke zolderruimten als vertrek meetellen: alleen een zolder ingeschoten als `Ruimtesoort.vertrek` met vaste trap én oppervlakte ≥ 4 m² wordt gewaardeerd. Van de vier zolders in de input levert alleen "Zolder vertrek met trap" (10 m²) **10 punten** op.

## Beleidsbron

- Implementatietoelichting: [§2.2.1.3 Zolderruimte als vertrek](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2213-zolderruimte-als-vertrek)
- Beleidsboek (quote): "de zolderruimte moet bereikbaar zijn via een vaste trap en"

## Handmatige berekening

| Zolder          | Soort          | Trap  | Oppervlakte | Punten        |
| --------------- | -------------- | ----- | ----------- | ------------- |
| Met vaste trap  | vertrek        | ja    | 10 m²       | 10            |
| Zonder trap     | vertrek        | nee   | 10 m²       | 0             |
| Met vlizotrap   | vertrek        | vlizo | 10 m²       | 0             |
| Overig met trap | overige ruimte | ja    | 1 m²        | 0 (rubriek 1) |
| **Totaal**      |                |       |             | **10**        |

## Opmerkingen

- Zolders zonder vaste trap of als overige ruimte ingeschoten vallen onder rubriek 2; zie `zolder_overige_ruimten`.
