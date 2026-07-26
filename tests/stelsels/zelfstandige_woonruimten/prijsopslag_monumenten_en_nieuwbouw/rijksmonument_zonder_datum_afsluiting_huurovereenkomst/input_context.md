# rijksmonument_zonder_datum_afsluiting_huurovereenkomst

## Doel

Test het fallback-gedrag wanneer `datumAfsluitenHuurovereenkomst` ontbreekt bij een rijksmonument: er verschijnt een `UserWarning`, de peildatum wordt als surrogaat gebruikt en bij peildatum op of na 1 juli 2024 volgt **35%** opslag.

## Beleidsbron

- Implementatietoelichting: [§2.13.3 Rijksmonumenten](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2134-rijksmonumenten)
- Beleidsboek (quote): "als de huurovereenkomst is afgesloten op of na het tijdstip van inwerkingtreding van de Wet betaalbare huur (vanaf 1 juli 2024) dan wordt de maximale huurprijs vermeerderd met 35%."

## Handmatige berekening

| Criterium     | Datum overeenkomst | Fallback             | Opslag     |
| ------------- | ------------------ | -------------------- | ---------- |
| Rijksmonument | ontbreekt          | peildatum 2026-01-01 | 35% (0,35) |

## Opmerkingen

- Zonder datum wordt een waarschuwing gegeven; zie `output.log`.
- De implementatie gebruikt de peildatum alleen als de huurovereenkomstdatum ontbreekt — niet als expliciet beleid uit het beleidsboek.
