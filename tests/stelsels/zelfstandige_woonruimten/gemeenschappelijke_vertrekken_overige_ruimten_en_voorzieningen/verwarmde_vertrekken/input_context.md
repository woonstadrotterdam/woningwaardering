# verwarmde_vertrekken

## Doel

Test dat verwarmde gemeenschappelijke vertrekken ook punten opleveren in rubriek 3 (verwarming), gedeeld door het aantal adressen.

De input bevat een verwarmde slaapkamer (5 adressen) en een verwarmde woonkamer (6 adressen). Verwacht totaal: **4,5 punten** (oppervlakte + verwarming).

## Beleidsbron

- Implementatietoelichting: [§2.9.2 Punten voor voorzieningen in gemeenschappelijke ruimten](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#292-punten-voor-voorzieningen-in-gemeenschappelijke-ruimten)
- Beleidsboek (quote): "Punten voor voorzieningen, zoals verkoeling en verwarming, keuken en sanitair, die zich bevinden in gemeenschappelijke vertrekken en overige ruimten worden gewaardeerd volgens het woningwaarderingsstelsel. Het puntenaantal moet vervolgens per rubriek worden gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft tot de ruimte."

## Handmatige berekening

| Component              | Berekening | Punten  |
| ---------------------- | ---------- | ------- |
| Slaapkamer oppervlakte | 10 / 5     | 2,0     |
| Slaapkamer verwarmd    | 2 / 5      | 0,4     |
| Woonkamer oppervlakte  | 10 / 6     | 1,67    |
| Woonkamer verwarmd     | 2 / 6      | 0,33    |
| **Totaal**             |            | **4,5** |
