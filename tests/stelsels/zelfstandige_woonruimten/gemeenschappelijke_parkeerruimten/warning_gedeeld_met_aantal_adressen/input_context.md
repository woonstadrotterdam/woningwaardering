# warning_gedeeld_met_aantal_adressen

## Doel

Test dat gemeenschappelijke parkeerruimten zonder `gedeeldMetAantalAdressen` een waarschuwing geven en niet worden gewaardeerd.

De input bevat een carport met laadpaal en een parkeerplek buiten, beide zonder `gedeeldMetAantalAdressen`. Verwacht: **0 punten** en een `UserWarning` over het ontbrekende attribuut.

## Beleidsbron

- Implementatietoelichting: [§2.10.4 Rekenmethode](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2104-rekenmethode)
- Beleidsboek (quote): "Het puntenaantal moet worden berekend door het puntenaantal per gemeenschappelijke parkeerplek te delen door aantal adressen dat toegang en gebruiksrecht heeft."

## Opmerkingen

- Zonder `gedeeldMetAantalAdressen` kan de verdeling niet worden berekend; de implementatie geeft een waarschuwing en slaat de ruimten over.
- Activeer `warnings.simplefilter("default", UserWarning)` om de warning zichtbaar te maken bij handmatig draaien.
