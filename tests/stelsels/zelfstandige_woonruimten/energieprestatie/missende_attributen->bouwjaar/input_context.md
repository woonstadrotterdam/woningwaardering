# missende_attributen->bouwjaar

## Doel

Test dat een energieprestatie zonder geldig `soort`-attribuut niet als label/index wordt geaccepteerd en dat de waardering terugvalt op het bouwjaar.

De input bevat een meergezinswoning (bouwjaar 1921) met een energieprestatie zonder `soort`. Verwacht: **−15 punten** onder **Bouwjaar 1921**.

## Beleidsbron

- Implementatietoelichting: [§2.4.5 Punten energieprestatie zonder geldig energielabel of energie-index](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#245-punten-energieprestatie-zonder-geldig-energielabel-of-energie-index)
- Beleidsboek (quote): "Als een woonruimte geen (geldig) energielabel of energie-index heeft, bepaalt het bouwjaar van de woning het aantal punten voor de energieprestatie."

## Handmatige berekening

| Gegeven    | Waarde               |
| ---------- | -------------------- |
| Woningtype | Meergezinswoning     |
| Bouwjaar   | 1921 (1976 of ouder) |
| Punten     | −15                  |
