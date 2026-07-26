# woz_rekenvoorbeeld_beleidsboek

## Doel

Test het rekenvoorbeeld uit het beleidsboek voor rubriek 11: WOZ-waarde € 300.000 (peildatum 1 januari 2025) en 60 m² oppervlakte van vertrekken en overige ruimten levert **36,25 punten** op.

## Beleidsbron

- Implementatietoelichting: [§2.11.2 Punten voor de WOZ-waarde](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#2112-punten-voor-de-woz-waarde-taxatiewaarde-of-minimum-woz-waarde)
- Beleidsboek (quote): "De WOZ-waarde van een woning is op 1 januari 2026 vastgesteld op € 300.000, met de waardepeildatum 1 januari 2025. De oppervlakte van de vertrekken en overige ruimten van de woning is 60 m²."

## Handmatige berekening

| Onderdeel | Berekening                | Punten    |
| --------- | ------------------------- | --------- |
| I         | € 300.000 / € 16.954      | 17,6949…  |
| II        | € 300.000 / 60 m² / € 268 | 18,6567…  |
| Totaal    | afgerond op kwart punt    | **36,25** |
