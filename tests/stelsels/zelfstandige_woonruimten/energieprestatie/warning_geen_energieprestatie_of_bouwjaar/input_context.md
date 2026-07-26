# warning_geen_energieprestatie_of_bouwjaar

## Doel

Test dat een waarschuwing volgt wanneer er geen bruikbare energieprestatie én geen bouwjaar beschikbaar is. Zonder label/index is bouwjaar de beleidsfallback; ontbreekt die ook, dan is warning + 0 punten implementatiegedrag bij incomplete input.

## Beleidsbron

- Implementatietoelichting: [§2.4.5 Punten energieprestatie zonder geldig energielabel of energie-index](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#245-punten-energieprestatie-zonder-geldig-energielabel-of-energie-index)
- Beleidsboek (quote): "Als een woonruimte geen (geldig) energielabel of energie-index heeft, bepaalt het bouwjaar van de woning het aantal punten voor de energieprestatie."
