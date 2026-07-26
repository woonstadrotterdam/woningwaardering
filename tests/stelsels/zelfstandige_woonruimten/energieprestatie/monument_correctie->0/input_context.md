# monument_correctie->0

## Doel

Test de monumentcorrectie voor energieprestatie: een rijksmonument zonder geldig energielabel krijgt op basis van bouwjaar minpunten, maar de monumentcorrectie brengt het totaal naar 0.

De input bevat een rijksmonument (meergezinswoning, bouwjaar 1921) zonder energieprestaties. Verwacht: **0 punten** (bouwjaar −15 + correctie monument +15).

## Beleidsbron

- Implementatietoelichting: [§2.4.6.1 Energieprestatie van monumenten](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2461-energieprestatie-van-monumenten)
- Beleidsboek (quote): "Hiervoor worden geen minpunten toegekend voor de energielabels E, F en G en daarmee samenhangende energie-indexen en bouwjaren. De puntentoekenning voor de energieprestatie is dan 0 punten."

## Handmatige berekening

| Component                        | Punten |
| -------------------------------- | ------ |
| Bouwjaar 1921 (meergezinswoning) | −15    |
| Correctie monument               | +15    |
| **Totaal**                       | **0**  |
