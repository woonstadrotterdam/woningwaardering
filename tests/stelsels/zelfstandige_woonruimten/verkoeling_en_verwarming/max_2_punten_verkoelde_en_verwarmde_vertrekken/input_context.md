# max_2_punten_verkoelde_en_verwarmde_vertrekken

## Doel

Test maximering van verkoelde vertrekken: 3 verwarmde én verkoelde slaapkamers leveren 6 pt verwarming + 3 pt verkoeling, maar verkoeling wordt afgetopt op **2 punten**; totaal **8 punten**.

## Beleidsbron

- Implementatietoelichting: [§2.3.3 Verkoelingsfunctie](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#233-extra-punten-bij-verkoelingsfunctie)
- Beleidsboek (quote): "Er kan 1 punt worden behaald per vertrek tot een maximum van 2 punten."

## Handmatige berekening

| Categorie                    | Bruto | Max | Netto |
| ---------------------------- | ----- | --- | ----- |
| Verwarmde vertrekken (3 × 2) | 6     | —   | 6     |
| Verkoelde vertrekken (3 × 1) | 3     | 2   | 2     |
| Correctie verkoeling         |       |     | −1    |
| **Totaal**                   |       |     | **8** |
