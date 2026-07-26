# gedeelde_keuken

## Doel

Test dat een keuken die gedeeld is met vier adressen (`gedeeldMetAantalAdressen: 4`) niet wordt gewaardeerd in rubriek 5 (keuken) en **0 punten** oplevert in deze stelselgroep.

## Beleidsbron

- Implementatietoelichting: [§2.9.2 Punten voor voorzieningen in gemeenschappelijke ruimten](../../../../../docs/implementatietoelichtingen/zelfstandige-woonruimten.md#292-punten-voor-voorzieningen-in-gemeenschappelijke-ruimten)
- Beleidsboek (quote):
  "Punten voor voorzieningen, zoals verkoeling en verwarming, keuken en sanitair, die zich bevinden in gemeenschappelijke vertrekken en overige ruimten worden gewaardeerd volgens het woningwaarderingsstelsel."
  (...)
  "Het puntenaantal moet vervolgens per rubriek worden gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft tot de ruimte."

## Handmatige berekening

| Onderdeel                                          | Waardering in rubriek 5 |
| -------------------------------------------------- | ----------------------- |
| Gedeelde keuken (aanrecht 3150 mm + voorzieningen) | 0 punten                |

## Opmerkingen

- De keuken zou in rubriek 9 (gemeenschappelijke vertrekken) gedeeld door het aantal adressen worden gewaardeerd; die stelselgroep valt buiten deze testcase.
