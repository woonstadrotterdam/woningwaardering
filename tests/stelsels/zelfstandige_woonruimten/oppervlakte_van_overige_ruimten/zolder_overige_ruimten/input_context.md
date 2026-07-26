# zolder_overige_ruimten

## Doel

Test waardering van zolders als overige ruimte: alleen zolders met trap of vlizotrap en ≥ 2 m² tellen mee. Correctie van 5 punten voor zolder met vlizotrap. Totaal **10 punten**.

## Beleidsbron

- Implementatietoelichting: [§2.2.2.3 Zolderruimte zonder vaste trap](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2223-zolderruimte-zonder-vaste-trap)
- Beleidsboek (quote): "Als een zolderruimte niet voldoet aan de vereisten voor waardering als een 'vertrek', maar wel als overige ruimte kan worden aangemerkt en er is geen vaste trap naar de zolder, dan worden er 5 punten afgetrokken van de waarde die aan het vloeroppervlak wordt toegekend."

## Handmatige berekening

| Zolder         | Trap  | Oppervlakte | Meetelt?           |
| -------------- | ----- | ----------- | ------------------ |
| Met vaste trap | ja    | 10 m²       | ja                 |
| Zonder trap    | nee   | 10 m²       | nee                |
| Met vlizotrap  | vlizo | 10 m²       | ja (met correctie) |
| **Totaal**     |       | **10**      |                    |

## Opmerkingen

- Een zolder zonder enige trap wordt niet gewaardeerd als overige ruimte.
